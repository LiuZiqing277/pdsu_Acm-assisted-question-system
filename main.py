# -*- coding: utf-8 -*-
import base64
import csv
import json
import os
import random
import sys
import time
from queue import Queue
from threading import Thread

import ddddocr
import openai
import requests
import zhipuai
from PySide6.QtCore import QUrl, Slot, Qt, QTimer, Signal, QObject
from PySide6.QtGui import QDesktopServices, QPixmap, QColor, QFont, QIcon
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from easy_ernie import FastErnie
from lxml import etree
from qfluentwidgets import FluentIcon as FIF, isDarkTheme
from qfluentwidgets import MessageBox, Flyout, InfoBarIcon, InfoBar, InfoBarPosition, SegmentedWidget
from selenium import webdriver
from selenium.common import UnexpectedAlertPresentException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import images
from ui import Ui_MainWindow

try:
    import pyi_splash

    pyi_splash.close()
except ImportError:
    pass
if getattr(sys, 'frozen', False):
    absPath = os.path.dirname(os.path.abspath(sys.executable))
elif __file__:
    absPath = os.path.dirname(os.path.abspath(__file__))

print(absPath)
# 程序初始化
Language = "C"
Username = None
Password = None
friend_username = None
friend_password = None
ai = None
ThreadStatus = None
file_path = None
GPT_API_KEY = None
ZHIPU_API_KEY = None
WENXIN_BAIDUID = None
WENXIN_BDUSS_BFESS = None
q_half_automatic = Queue()


class WebEngineView(QWebEngineView):
    def createWindow(self, QWebEnginePage_WebWindowType):
        page = WebEngineView(self)
        page.urlChanged.connect(self.on_url_changed)
        return page

    def on_url_changed(self, url):
        self.setUrl(url)


class MyWindow(QMainWindow, Ui_MainWindow, QObject):
    LoginError = Signal(str, str)
    WriteInfo = Signal(str, str, int)

    def __init__(self):
        super().__init__()
        self.threadHalf = None
        self.threadCopy = None
        self.threadAuto = None
        self.config_file_path = r"{}/config.json".format(absPath)
        self.setupUi(self)
        self.load_or_create_config()

        # 按钮的信号和槽
        self.pushButton.clicked.connect(self.Copy_Mode)
        self.pushButton_2.clicked.connect(self.Auto_Mode)
        self.pushButton_3.clicked.connect(self.update_config1)
        self.pushButton_5.clicked.connect(self.update_config2)
        self.ButtonOpenAcm.clicked.connect(self.Half_automatic_Open)
        self.ButtonInputCode.clicked.connect(self.Half_automatic_Input)
        self.radioButtonGpt35.clicked.connect(self.on_radio_button_clicked3)
        # self.radioButtonZhiPu.clicked.connect(self.on_radio_button_clicked2)
        self.radioButtonWenXin.clicked.connect(self.on_radio_button_clicked1)
        # self.listWidget_2.itemClicked.connect(self.showMessageBox)
        self.listWidget.itemClicked.connect(self.change_page)
        self.listWidget_2.itemClicked.connect(self.change_page)
        self.LoginError.connect(self.show_Message_box)
        self.WriteInfo.connect(self.WriteInformation)

        # 创建设置 QListWidgetItem 对象其图标
        color = QColor(206, 206, 206) if isDarkTheme() else QColor(96, 96, 96)
        self.listWidget.item(0).setIcon(FIF.HOME.icon(color=color))
        self.listWidget.item(1).setIcon(FIF.COPY.icon(color=color))
        self.listWidget.item(2).setIcon(FIF.ROBOT.icon(color=color))
        self.listWidget.item(3).setIcon(FIF.ERASE_TOOL.icon(color=color))
        self.listWidget.item(4).setIcon(FIF.PENCIL_INK.icon(color=color))
        self.listWidget.item(5).setIcon(FIF.CHAT.icon(color=color))
        self.listWidget.item(6).setIcon(FIF.GLOBE.icon(color=color))
        self.listWidget.item(7).setIcon(FIF.VIEW.icon(color=color))
        self.listWidget.item(8).setIcon(FIF.FULL_SCREEN.icon(color=color))
        self.listWidget_2.item(0).setIcon(FIF.HEART.icon(color=color))
        self.listWidget_2.item(1).setIcon(FIF.HELP.icon(color=color))
        self.listWidget_2.item(2).setIcon(FIF.FEEDBACK.icon(color=color))

        """
        添加和AI聊聊界面的导航
        """
        self.webEngineView_3.setUrl("http://39.106.228.241/")
        self.webEngineView_2.setUrl("https://cn.bing.com/?mkt=zh-CN&mkt=zh-CN")
        self.webEngineView.setUrl("https://www.dotcpp.com/run/")
        self.pivot = SegmentedWidget(self)  # 顶部导航栏部件
        self.stackedWidget_2 = QStackedWidget(self)  # 顶部导航栏下的页面部件
        self.AI1 = QWebEngineView(self)  # 三个浏览器窗口部件
        self.AI2 = QWebEngineView(self)
        self.AI3 = QWebEngineView(self)
        self.AI4 = QWebEngineView(self)
        self.AI5 = QWebEngineView(self)
        self.AI1.setUrl("https://chat18.aichatos.xyz/")  # 设定访问的网站
        self.AI2.setUrl("https://yiyan.baidu.com/")
        self.AI3.setUrl("https://faucet.openkey.cloud/")
        self.AI4.setUrl("https://share.wendaalpha.net/?model=gpt-4")
        self.AI5.setUrl("https://chatforai.store/")

        # add items to pivot
        self.addSubInterface(self.AI1, 'GPTInterface', 'ChatGPT-3.5')
        self.addSubInterface(self.AI2, 'WENInterface', '文心一言')
        self.addSubInterface(self.AI3, 'ZHIInterface', "获取GPT令牌")
        self.addSubInterface(self.AI4, 'DOUInterface', 'ChatGPT-4')
        self.addSubInterface(self.AI5, 'ZIDINGInterface', 'ChatGPT-3.5自定义')

        self.vBoxLayout.addWidget(self.pivot)
        self.vBoxLayout.addWidget(self.stackedWidget_2)
        self.vBoxLayout.setContentsMargins(10, 10, 10, 1)

        self.stackedWidget_2.currentChanged.connect(self.onCurrentIndexChanged)
        self.stackedWidget_2.setCurrentWidget(self.AI1)
        self.pivot.setCurrentItem(self.AI1.objectName())

        # 解码图片数据
        image_data = base64.b64decode(images.money)
        pixmap = QPixmap()  # 创建 QPixmap 并在 QLabel 中显示图片
        pixmap.loadFromData(image_data)
        self.label_10.setPixmap(pixmap)
        self.label_10.setScaledContents(True)  # 让图片自适应大小

        # 笑话
        self.get_random_joke()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.get_random_joke)
        self.timer.start(100000)  # 5分钟刷新一次

        # 使用带颜色的文本设置一个欢迎语句
        self.WriteInfo.emit('event', "欢迎使用平顶山学院Acm辅助解题系统，输入账号密码开始使用。",1)
        self.statusBar.showMessage('Hello~ Welcome。🤗', 50000)  # 在状态栏中添加标签

    def load_or_create_config(self):
        global Username, Password, friend_username, friend_password, file_path
        global WENXIN_BAIDUID, WENXIN_BDUSS_BFESS, GPT_API_KEY
        default_config = {
            "Language": "C",
            "Username": None,
            "Password": None,
            "friend_username": None,
            "friend_password": None,
            "file_path": None,
            "GPT_API_KEY": None,
            "WENXIN_BAIDUID": None,
            "WENXIN_BDUSS_BFESS": None
        }
        if not os.path.exists(self.config_file_path):
            with open(self.config_file_path, 'w') as f:
                json.dump(default_config, f, indent=4)  # 设置缩进为4个空格
                print("已创建新的配置文件：{}".format(self.config_file_path))

        with open(self.config_file_path, 'r') as f:
            config_data = json.load(f)
            print("成功加载配置文件中的数据：")
            Username = config_data.get("Username")
            Password = config_data.get("Password")
            friend_username = config_data.get("friend_username")
            friend_password = config_data.get("friend_password")
            file_path = config_data.get("file_path")
            GPT_API_KEY = config_data.get("GPT_API_KEY")
            WENXIN_BAIDUID = config_data.get("WENXIN_BAIDUID")
            WENXIN_BDUSS_BFESS = config_data.get("WENXIN_BDUSS_BFESS")
            self.lineEdit_11.setText(GPT_API_KEY)
            self.lineEdit_8.setText(WENXIN_BAIDUID)
            self.lineEdit_10.setText(WENXIN_BDUSS_BFESS)
            print(config_data)

    def update_config1(self):
        key = "GPT_API_KEY"
        value = self.lineEdit_11.text()
        with open(self.config_file_path, 'r') as f:
            config_data = json.load(f)

        if key in config_data:
            config_data[key] = value

            with open(self.config_file_path, 'w') as f:
                json.dump(config_data, f, indent=4)  # 写入更新后的数据

            print("成功更新配置文件中的数据：")
            self.ShowSuccessInfoBar("更新GPT_API_KEY数据成功！")
            print(config_data)
            global GPT_API_KEY
            GPT_API_KEY = value
        else:
            print("指定的键值不存在于配置文件中")

    def update_config2(self):
        global WENXIN_BAIDUID, WENXIN_BDUSS_BFESS
        keys = ["WENXIN_BAIDUID", "WENXIN_BDUSS_BFESS"]
        values = [f"{self.lineEdit_8.text()}", f"{self.lineEdit_10.text()}"]
        if values[0] == "" or values[1] == "":
            print("有空的选项")
            self.ShowErrorInfoBar("文心一言的两个空格都要填写！")
            return
        with open(self.config_file_path, 'r') as f:
            config_data = json.load(f)
        for key in keys:
            config_data[key] = values[0] if key == "WENXIN_BAIDUID" else values[1]
        with open(self.config_file_path, 'w') as f:
            json.dump(config_data, f, indent=4)  # 写入更新后的数据
        WENXIN_BAIDUID = values[0]
        WENXIN_BDUSS_BFESS = values[1]
        print("成功更新配置文件中的数据：")
        self.ShowSuccessInfoBar("更新文心一言数据成功！")
        print(config_data)

    @Slot(str, str, int)
    def WriteInformation(self, Using, text, num=None):

        if Using == "normal":
            """公共方法，用于在 QTextBrowser 中添加文本"""
            if num == 2:
                self.textBrowser_2.append(text)
                self.textBrowser_2.ensureCursorVisible()  # 游标可用
                cursor = self.textBrowser_2.textCursor()  # 设置游标
                pos = len(self.textBrowser_2.toPlainText())  # 获取文本尾部的位置
                cursor.setPosition(pos)  # 游标位置设置为尾部
                self.textBrowser_2.setTextCursor(cursor)  # 滚动到游标位置

            else:
                self.textBrowser.append(text)
                self.textBrowser.ensureCursorVisible()  # 游标可用
                cursor = self.textBrowser.textCursor()  # 设置游标
                pos = len(self.textBrowser.toPlainText())  # 获取文本尾部的位置
                cursor.setPosition(pos)  # 游标位置设置为尾部
                self.textBrowser.setTextCursor(cursor)  # 滚动到游标位置
        elif Using == "event":
            text = f"<html><body><p style='color:red;'>{text}</p>"
            if num == 2:
                self.textBrowser_2.append(text)
                self.textBrowser_2.ensureCursorVisible()  # 游标可用
                cursor = self.textBrowser_2.textCursor()  # 设置游标
                pos = len(self.textBrowser_2.toPlainText())  # 获取文本尾部的位置
                cursor.setPosition(pos)  # 游标位置设置为尾部
                self.textBrowser_2.setTextCursor(cursor)  # 滚动到游标位置
            else:
                self.textBrowser.append(text)
                self.textBrowser.ensureCursorVisible()  # 游标可用
                cursor = self.textBrowser.textCursor()  # 设置游标
                pos = len(self.textBrowser.toPlainText())  # 获取文本尾部的位置
                cursor.setPosition(pos)  # 游标位置设置为尾部
                self.textBrowser.setTextCursor(cursor)  # 滚动到游标位置
        elif Using == "info":
            text = f"<p style='color:blue;'>{text}</p></body></html><br>"
            if num == 2:
                self.textBrowser_2.append(text)
                self.textBrowser_2.ensureCursorVisible()  # 游标可用
                cursor = self.textBrowser_2.textCursor()  # 设置游标
                pos = len(self.textBrowser_2.toPlainText())  # 获取文本尾部的位置
                cursor.setPosition(pos)  # 游标位置设置为尾部
                self.textBrowser_2.setTextCursor(cursor)  # 滚动到游标位置
            else:
                self.textBrowser.append(text)
                self.textBrowser.ensureCursorVisible()  # 游标可用
                cursor = self.textBrowser.textCursor()  # 设置游标
                pos = len(self.textBrowser.toPlainText())  # 获取文本尾部的位置
                cursor.setPosition(pos)  # 游标位置设置为尾部
                self.textBrowser.setTextCursor(cursor)  # 滚动到游标位置

    @Slot()
    def addSubInterface(self, widget: QWebEngineView, objectName, text):
        widget.setObjectName(objectName)
        # widget.setAlignment(Qt.AlignCenter)
        self.stackedWidget_2.addWidget(widget)
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget_2.setCurrentWidget(widget),
        )

    @Slot()
    def onCurrentIndexChanged(self, index):
        widget = self.stackedWidget_2.widget(index)
        self.pivot.setCurrentItem(widget.objectName())

    @Slot()
    def change_page(self, item):

        # 获取第二个列表的索引
        current_index = self.listWidget_2.row(item)
        if current_index not in [-1]:
            # 处理索引为 -1 的情况
            print("current_index:", current_index)
            if item.text() == "捐献":
                self.statusBar.showMessage('Give me money ! ! 😍', 80000)

            elif item.text() == "使用帮助":
                self.statusBar.showMessage('Oh my god ! ! Help me ! ! ', 50000)

            elif item.text() == "关于作者":
                self.statusBar.showMessage('About LIUKAI😋', 50000)
                self.textBrowserXiao.clear()
                self.get_random_joke()

            self.stackedWidget.setCurrentIndex(current_index + 8)

        else:
            # 处理索引为 不为-1 的情况
            index = self.listWidget.row(item)
            if item.text() == "最大化":
                self.showFullScreen()
                self.listWidget.item(8).setIcon(FIF.CANCEL.icon())
                self.statusBar.showMessage('看的好清啊~~', 50000)
                item.setText("恢复")
                return
            elif item.text() == "恢复":
                self.showNormal()
                self.listWidget.item(8).setIcon(FIF.FULL_SCREEN.icon())
                self.statusBar.showMessage('要有距离感！', 50000)
                item.setText("最大化")
                return
            elif item.text() == "Home":
                self.statusBar.showMessage('Hi~ Welcome。', 50000)

            elif item.text() == "Copy 模式":
                self.statusBar.showMessage('This is Copy mode。💯', 50000)

            elif item.text() == "AI 模式":
                self.statusBar.showMessage('This is AI mode。', 50000)

            elif item.text() == "半自动模式":
                self.statusBar.showMessage('This is Half_automatic mode。', 50000)

            elif item.text() == "写作业了！":
                self.statusBar.showMessage('Come on ! !', 50000)

            elif item.text() == "和AI聊聊？":
                self.statusBar.showMessage('Chat with AI ?', 50000)

            elif item.text() == "上网查查！":
                self.statusBar.showMessage('Search in the web。', 50000)
                self.ShowInformationBar('右键菜单"back"可返回上一标签页')

            elif item.text() == "测试代码":
                self.statusBar.showMessage('Test the code!', 50000)
                self.ShowInformationBar('可以将你的代码放在这里测试运行，如果你自己写题的话。')

            # self.statusBar.addPermanentWidget(self.statusLabel)
            print(index)
            self.stackedWidget.setCurrentIndex(index)

    @Slot()
    def on_radio_button_clicked1(self):
        global ai

        ai = 1
        self.pushButton_2.setEnabled(True)  # 启用按钮
        self.pushButton_2.setText("提交并运行")
        print("选择 文心一言")

    @Slot()
    def on_radio_button_clicked3(self):
        global ai
        ai = 3
        self.pushButton_2.setEnabled(True)  # 启用按钮
        self.pushButton_2.setText("提交并运行")
        print("选择 ChatGPT3.5-turbo")

    @Slot()
    def showMessageBox(self):
        w = MessageBox(
            '支持作者🥰',
            '个人开发不易，如果这个程序帮助到了你，可以考虑请作者喝一瓶快乐水🥤。你的支持就是作者开发和维护程序的动力🚀',
            self
        )
        w.yesButton.setText('来啦老弟')
        w.cancelButton.setText('下次一定')

        if w.exec():
            QDesktopServices.openUrl(QUrl("http://www.li-yian.site/"))

    @Slot(str, str)
    def show_Message_box(self, title, text):
        # 创建信息消息框
        w = MessageBox(
            f'{title}',
            f'{text}',
            self
        )
        w.exec()

    @Slot()
    def ShowGoodInfoBar(self, text):
        Flyout.create(
            icon=InfoBarIcon.SUCCESS,
            title='good',
            content="{}".format(text),
            target=self.pushButton,
            parent=self,
            isClosable=False
        )

    @Slot()
    def ShowErrorInfoBar(self, text):
        InfoBar.error(
            title='错了',
            content="{}".format(text),
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_RIGHT,
            duration=-1,  # won't disappear automatically
            parent=self
        )

    @Slot()
    def ShowInformationBar(self, text):
        content = "{}".format(text)
        w = InfoBar(
            icon=InfoBarIcon.INFORMATION,
            title='提示',
            content=content,
            orient=Qt.Vertical,  # vertical layout
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=9000,
            parent=self
        )
        # w.addWidget(PushButton('Action'))
        w.show()

    @Slot()
    def ShowSuccessInfoBar(self, text):
        # convenient class mothod
        InfoBar.success(
            title='success',
            content="{}".format(text),
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            # position='Custom',   # NOTE: use custom info bar manager
            duration=2000,
            parent=self
        )

    @Slot()
    def Copy_Mode(self):
        global Username, Password
        global friend_username, friend_password
        global ThreadStatus
        ThreadStatus = True
        Username = self.lineEdit.text()
        Password = self.lineEdit2.text()
        friend_username = self.lineEdit_3.text()
        friend_password = self.lineEdit_4.text()
        if Username is None or Password is None or friend_username is None or friend_password is None or Username == "" or Password == "" or friend_username == "" or friend_password == "":
            # 检查是否有空值
            self.show_Message_box('关爱🥰', '我的朋友，你是不是没输入账号密码？')
            return
        else:
            self.pushButton.setEnabled(False)  # 禁用按钮
            self.threadCopy = Thread(target=Copy_mode)
            self.threadCopy.daemon = True
            self.threadCopy.start()

    @Slot()
    def Auto_Mode(self):
        global Username, Password
        Username = self.lineEdit_2.text()
        Password = self.lineEdit2_2.text()
        global ThreadStatus
        ThreadStatus = True
        if Username is None or Password is None or Username == "" or Password == "":
            # 检查是否有空值
            self.ShowErrorInfoBar('不给账号密码，怎么给你办事？')
            return
        if ai == 1:
            if WENXIN_BAIDUID is None or WENXIN_BDUSS_BFESS is None:
                self.WriteInfo.emit("normal", "请先在config.json中配置WENXIN_BAIDUID和WENXIN_BDUSS_BFESS", 2)
                self.LoginError.emit("缺少文心一言身份数据！",
                                     "请先在config.json或程序的 帮助&配置 窗口中配置 WENXIN_BAIDUID 和 WENXIN_BDUSS_BFESS ")
                return
            else:
                self.ShowGoodInfoBar("文心一言启动！")
        elif ai == 2:
            self.ShowErrorInfoBar("智谱清言修复中，请转用ChatGPT3.5或文心一言")
            return
        if ai == 3:
            self.ShowGoodInfoBar("ChatGPT3.5-turbo启动！")
        elif ai is None:
            self.ShowErrorInfoBar("朋友，你还没有选择AI。")
            return

        self.threadAuto = Thread(target=Full_automatic)
        self.threadAuto.daemon = True
        self.threadAuto.start()
        # self.ShowInformationBar("由于技术原因，开辟的工作线程不稳定，运行一段时间后，线程可能会崩溃，没办法，多试几次吧。")
        self.pushButton_2.setEnabled(False)  # 禁用按钮
        self.pushButton_2.setText("正在运行中")

    @Slot()
    def Half_automatic_Open(self):
        global Username, Password
        Username = self.lineEdit_5.text()
        Password = self.lineEdit_6.text()
        global ThreadStatus
        ThreadStatus = True
        if Username is None or Password is None or Username == '' or Password == '':
            # 检查是否有空值
            self.ShowErrorInfoBar('不给账号密码，怎么给你办事？')
            return
        self.threadHalf = Thread(target=Half_automatic)
        self.threadHalf.daemon = True
        self.threadHalf.start()
        self.ButtonOpenAcm.setEnabled(False)  # 禁用按钮
        self.ButtonOpenAcm.setText("正在运行中")

    @Slot()
    def Half_automatic_Input(self):
        answer = self.plainTextEdit_2.toPlainText()
        print(answer)
        if answer == "":
            self.ShowErrorInfoBar(text="不给答案，我给你提交什么？")
            return
        q_half_automatic.put(self.plainTextEdit_2.toPlainText())

    @Slot()
    def get_random_joke(self):
        response = requests.get(
            "https://www.mxnzp.com/api/jokes/list?page=1&app_id=bckhoutcylitmpkb&app_secret=LH6luW3KKikKJWEgcvEkapSYerd7tECe")
        cc = json.loads(response.content.decode("utf-8"))  # 将字节码转换为Python对象
        jokes_list = cc['data']['list']
        # 创建一个新的字体对象，设置字体大小为14
        font = QFont()
        font.setPointSize(14)
        # 将新的字体应用到 text browser
        self.textBrowserXiao.setFont(font)
        random_joke = random.choice(jokes_list)
        self.textBrowserXiao.append('听个笑话吧~😋(1分种换一个)\n')
        self.textBrowserXiao.append(random_joke['content'])
        self.textBrowserXiao.append('')  # 添加空行


def login(num=None):
    def decorator(func):
        def login_wrapper(*args, **kwargs):

            if func.__name__ in ['copy_answer_thread']:
                User = friend_username
                Pass = friend_password
            else:
                User = Username
                Pass = Password

            start_time = time.time()
            url = "http://39.106.228.241/"
            # 创建 Chrome 浏览器驱动对象
            driver = webdriver.Edge()
            # 设置等待时间
            driver.implicitly_wait(1)
            record = 0
            # 访问网页
            while True:
                driver.get(url)
                window.WriteInfo.emit('event','--------------------开始执行登录操作--------------------',num)
                print(driver.title)
                window.WriteInfo.emit("normal", '当前登录页面：' + driver.title, num)
                # 移动鼠标到指定元素上
                driver.find_element("xpath", '//*[@id="profile"]').click()
                # 点击登录界按钮
                driver.find_element("xpath", '//*[@id="navbar"]/ul[2]/li/ul/li[1]/a').click()
                # 进入登录界面成功
                driver.find_element("xpath", '//*[@id="login"]/div[1]/div/input').send_keys(f'{User}')
                # 输入账号成功！
                driver.find_element("xpath", '//*[@id="login"]/div[2]/div/input').click()
                driver.switch_to.active_element.send_keys(f'{Pass}')
                # 点击密码框成功！开始解决验证码问题！
                img_code = driver.find_element("xpath", '//*[@id="login"]/div[3]/div[2]/img')
                catch = verify_code(img_code=img_code)
                driver.find_element("xpath", '//*[@id="login"]/div[3]/div[1]/input').click()
                window.WriteInfo.emit("normal", str('验证码识别结果：' + catch), num)
                driver.switch_to.active_element.send_keys(catch)  # 将识别到的验证码输入到框内
                # print('验证码输入成功！')
                driver.find_element("xpath", '//*[@id="login"]/div[4]/div[1]/button').click()
                # 点击登录按钮
                try:
                    driver.find_element("xpath", '//*[@id="navbar"]/ul[1]/li[3]/a').click()  # 这个是登录界面的登录按钮
                    window.WriteInfo.emit("event", '--------------------登录操作执行成功--------------------', num)
                    window.WriteInfo.emit("normal", ' ', num)
                    func(driver)
                    driver.quit()
                except UnexpectedAlertPresentException as e:
                    if record > 2:
                        driver.quit()
                        global ThreadStatus
                        ThreadStatus = False
                        window.LoginError.emit('登录失败！', '老弟，你的账号密码是不是输错了，检查下吧')
                        break
                    print(
                        '----------------------------------验证码识别失败，正在重试！-------------------------------------')
                    window.WriteInfo.emit("event", '--------------------验证码识别失败，正在重试--------------------',
                                          num)
                    record += 1
                    continue
                break

            window.WriteInfo.emit("info", '耗时:{}秒'.format(str(time.time() - start_time)), num)
            print()
            if func.__name__ not in ['put_answer_thread', 'copy_answer_thread', 'record_true_id']:
                pass
                # press_any_key()

        return login_wrapper

    return decorator


def 题目拼接(html):
    timu = '题目描述' + '\n'
    题目描述 = html.xpath('/html/body/div[1]/div/div[1]//text()')
    for a in range(len(题目描述)):
        题目描述[a] = 题目描述[a].strip()
        timu = timu + 题目描述[a] + '\n'
    输入描述 = html.xpath('/html/body/div[1]/div/div[2]//text()')
    for b in range(len(输入描述)):
        输入描述[b] = 输入描述[b].strip()
        timu = timu + '输入描述' + '\n' + 输入描述[b] + '\n'
    输出描述 = html.xpath('/html/body/div[1]/div/div[3]//text()')
    for c in range(len(输出描述)):
        输出描述[c] = 输出描述[c].strip()
        timu = timu + '输出描述' + '\n' + 输出描述[c] + '\n'
    样例输入 = html.xpath('/html/body/div[1]/div/pre[1]//text()')
    for d in range(len(样例输入)):
        样例输入[d] = 样例输入[d].strip()
        timu = timu + '样例输入' + '\n' + 样例输入[d] + '\n'
    样例输出 = html.xpath('/html/body/div[1]/div/pre[2]//text()')
    for e in range(len(样例输出)):
        样例输出[e] = 样例输出[e].strip()
        timu = timu + '样例输出' + '\n' + 样例输出[e] + '\n'
    提示 = html.xpath('/html/body/div[1]/div/div[4]/p//text()')
    for f in range(len(提示)):
        提示[f] = 提示[f].strip()
        timu = timu + '提示' + '\n' + 提示[f]
    cleaned_text = ''
    for char in timu:
        if char.isalpha() or char.isspace() or char == '\n':  # 检查字符是否为字母、空格或换行符
            cleaned_text += char
    return timu


def verify_code(img_code):
    # 获取当前脚本所在目录
    current_dir_v = os.path.dirname(os.path.abspath(__file__))
    # 拼接验证码图片路径
    image_path = os.path.join(current_dir_v, "code.png")
    # 删除旧的验证码图片
    if os.path.exists(image_path):
        os.remove(image_path)
    # 截取当前验证码图片
    img_code.screenshot(image_path)
    # 创建 OCR 对象
    ocr = ddddocr.DdddOcr()
    with open(image_path, "rb") as fp:
        # 读取验证码图片内容
        image = fp.read()
        # 使用 OCR 进行验证码识别
        catch = ocr.classification(image)
        if catch and len(catch) == 4 and catch.isdigit():
            print("验证码识别结果：", catch)
            fp.close()  # 确保在不需要使用文件时关闭文件
            return catch
        else:
            # print("验证码识别失败")
            # 点击刷新验证码
            img_code.click()
            fp.close()  # 确保在不需要使用文件时关闭文件
            catch = verify_code(img_code)
            return catch


def input_code(driver, question_class):
    # 将代码按指定长度分割
    answer = question_class.get_answer()
    lines = answer.splitlines()  # 将代码按行拆分成列表
    cleaned_lines = [line.lstrip() for line in lines]  # 去除每一行开头的空格
    answer = '\n'.join(cleaned_lines)  # 将处理后的行重新连接成字符串
    print(5)
    print(answer)
    code_segments = [answer[i:i + 1] for i in range(0, len(answer), 1)]

    print(code_segments)
    # 在特定输入框中粘贴每个段落的代码
    for segment in code_segments:
        if segment == "{":
            driver.switch_to.active_element.send_keys('{')
            driver.switch_to.active_element.send_keys(Keys.SPACE)
        elif segment == ";":
            driver.switch_to.active_element.send_keys(segment)
            # driver.switch_to.active_element.send_keys(Keys.ENTER)
            # elif 0x4E00 <= ord(segment) <= 0x9FFF:  # 检测字符是否是汉字  # 检测字符是否是汉
        elif segment == "}":
            driver.switch_to.active_element.send_keys(segment)
            # driver.switch_to.active_element.send_keys(Keys.ENTER)
        elif segment == '>':
            driver.switch_to.active_element.send_keys(segment)
            # driver.switch_to.active_element.send_keys(Keys.ENTER)
        elif segment == '(':
            driver.switch_to.active_element.send_keys('()')
            driver.switch_to.active_element.send_keys(Keys.BACKSPACE)
        else:
            driver.switch_to.active_element.send_keys(segment)
    print("粘贴代码成功！")
    return True


def text_pocessing(text, delimiter, ab=False):
    # 如果传入的是一个列表
    if isinstance(text, list):
        text = ''.join(text)  # 将列表内容拼接成字符串
    # 定义分隔符
    # 找到指定元素前的文本和后面的文本
    if delimiter in text:
        before_text, after_text = text.split(delimiter, 1)
        # 输出: 后面的文本
        if ab:
            result = after_text
            return f"{delimiter}" + result
        elif not ab:
            # 输出: 前面的文本
            result = before_text
            return result
    else:
        return text


def extract_unique_data(file_a, file_b, file_c):
    data_a = set()
    with open(file_a, 'r+', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_a.add((row['id'], row['language']))

    data_b = []
    with open(file_b, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (row['id'], row['language']) not in data_a:
                data_b.append(row)

    header = ['id', 'title', 'body', 'language', 'answer', 'grade', 'status']  # 定义表头
    with open(file_c, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data_b)


def check_duplicate(new_data):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == new_data['id'] and row['language'] == new_data['language']:
                return True
    return False


def write_to_csv(data):
    header = ['id', 'title', 'body', 'language', 'answer', 'grade', 'status']  # 定义表头
    is_duplicate = check_duplicate(data)
    if not is_duplicate:
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writerow(data)


def write_question_dic_csv(new_question_list_dict):  # 这里应当接受字典组成的列表
    header = ['id', 'title', 'body', 'language', 'answer', 'grade', 'status']
    with open(file_path, 'w', encoding='utf-8', newline='') as file_instance:
        rows = csv.DictWriter(file_instance, header)
        rows.writeheader()
        rows.writerows(new_question_list_dict)


def sort_question_data(question_list_dic):
    # 使用sorted()函数和lambda函数对字典列表进行排序
    new_question_list_dict = sorted(question_list_dic, key=lambda k: int(k['grade']), reverse=True)
    return new_question_list_dict


def Chatgpt3_5(timu):
    print(
        '-----当前实时响应由<Chatgpt3.5-turbo>提供！-----\n')
    text = "当前实时响应由【Chatgpt3.5-turbo】提供"
    window.WriteInfo.emit('event', "  ", 2)
    window.WriteInfo.emit('event', text, 2)
    # openai.api_base = "https://api.openai.com/v1" # 换成代理，一定要加v1
    openai.api_base = "https://openkey.cloud/v1"  # 换成代理，一定要加v1
    # openai.api_key = "API_KEY"
    openai.api_key = GPT_API_KEY
    answer = []
    www = ""
    for resp in openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"{timu}"}
            ],
            # 流式输出
            stream=True):
        if 'content' in resp.choices[0].delta:
            text = resp.choices[0].delta.content
            print(text, end="", flush=True)
            answer.append(text)
    for a in answer[::-1]:
        www = a + www
    return www


def wenxin(timu):
    print('文心一言不提供实时响应，请耐心等待！\n正在获取答案...\n\n')
    text = "当前响应由【文心一言】提供！"
    window.WriteInfo.emit('event', text, 2)
    window.WriteInfo.emit('event', "  ", 2)
    text = "文心一言不提供实时响应，请耐心等待！"
    window.WriteInfo.emit("normal", text, 2)
    window.WriteInfo.emit('normal', "正在获取答案...正常耗时10秒以内。", 2)
    window.WriteInfo.emit('normal', "  ", 2)
    # 调用文心一言的接口，以便于获取答案
    fastErnie = FastErnie('{}'.format(WENXIN_BAIDUID),
                          '{}'.format(WENXIN_BDUSS_BFESS))
    try:
        answer_text = fastErnie.ask(f'{timu}').get('answer')
        print(answer_text)
        window.WriteInfo.emit("normal", "获取响应成功！答案如下", 2)
        window.WriteInfo.emit('normal', answer_text, 2)
        return answer_text  # 返回文本
    except Exception as e:
        print(e)
        text = """
        文心一言获取响应失败，{请求失败,用户访问被限制}当你遇到这个错误时，意味着这个文心一言的账户遭到了限制，这是由于短时间内多个请求从同一个账号发出，
        账号产生的异常流量遭到平台检测,而被限制访问导致的，你可能需要过一段时间再使用该账号，或者换一个文心一言访问令牌，。
        
        """
        window.ShowErrorInfoBar(text=text)
        time.sleep(1)
        window.ShowErrorInfoBar(text=text)
    # fastErnie.close()


def zhipu(timu):
    zhipuai.api_key = ZHIPU_API_KEY
    response = zhipuai.model_api.sse_invoke(
        model="chatglm_turbo",
        prompt=[
            {"role": "user", "content": "你好"},
            {"role": "assistant", "content": f"我是一位{Language}语言解题大师，我擅长用代码解题。"},
            {"role": "user", "content": f"我会给你提供一些{Language}语言题目，你要给我提供代码，记住只要代码！"},
            {"role": "assistant", "content": f"好的，我记住了，我会仅给你提供符合要求的{Language}语言代码"},
            {"role": "user", "content": f"{timu}"},
        ],
        temperature=0.95,
        top_p=0.5,
        incremental=True
    )
    '''
      说明：
      add: 事件流开启
      error: 平台服务或者模型异常，响应的异常事件
      interrupted: 中断事件，例如：触发敏感词
      finish: 数据接收完毕，关闭事件流
    '''
    print(
        '-----当前实时响应由<智谱Ai>提供！-----\n')
    text = "----------当前实时响应由【智谱Ai】提供！----------"
    window.WriteInfo.emit('event', text, 2)
    window.WriteInfo.emit('event', "  ", 2)
    question.answer = []  # 这个是一个question类的answer列表内容，包含空格和换行\n
    for event in response.events():
        if event.event == "add":
            print(event.data, end="")
            window.WriteInfo.emit('normal', event.data, 2)
            question.answer.append(event.data)
        elif event.event == "error" or event.event == "interrupted":
            print(event.data)
            window.WriteInfo.emit('normal', event.data, 2)
        elif event.event == "finish":
            print(event.data)
            window.WriteInfo.emit('normal', event.data, 2)
            # print(event.meta)
        else:
            print(event.data)
            window.WriteInfo.emit('normal', event.data, 2)
    a = ''  # 定义一个空字符串,question.answer是一个列表,拼接列表中的字符串，为长文本字符串。好像不是单行，里面由\n隔开的
    for i in question.answer:
        a = a + i
    return a  # 返回纯文本


@login(num=None)
def Half_automatic(driver2):
    text = "朋友，欢迎使用本系统，\
    在使用之前，我要告诉你基本的使用方法，你要手动在当前界面进入一个题目的写代码界面，然后返回“辅助系统”的【半自动模式】界面，\
    在输入框中输入这个题目的答案，点击提交，\
    本系统会自行提交答案，你只需要注意答案的正确性，和界面展开的正确性，如果界面打开错误，程序无法正常工作！，不要一次性提交多个答案，\
    程序使用多线程，除非你的手速过快，不然会出现奇奇怪怪的错误，现在一题一题的开始吧！"
    js_code = 'alert("{}")'.format(text)
    driver2.execute_script(js_code)
    while 1:
        while q_half_automatic.empty():
            time.sleep(2)
            print("{}等待答案。。。。。。".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        print("等待答案中.......")
        answer = q_half_automatic.get()
        question = Question(question_answer=answer)
        driver2.switch_to.window(driver2.window_handles[-1])
        driver2.find_element("xpath", '//*[@id="source"]').click()
        input_code(driver2, question)
        # 调用识别函数，并返回验证码
        img_code1 = driver2.find_element("xpath", '//*[@id="vcode"]')  # 验证码图片元素对象
        element = driver2.find_element("xpath", '//*[@id="language_span"]/input')  # 这个是提交答案的验证码输入框
        # 调用识别函数并返回验证码,这里是提交的验证码
        catch1 = verify_code(img_code=img_code1)
        element.click()
        driver2.switch_to.active_element.send_keys(Keys.CONTROL, 'a')
        driver2.switch_to.active_element.send_keys(Keys.DELETE)
        driver2.switch_to.active_element.send_keys(catch1)  # 将识别到的验证码输入到框内
        # 直接点击提交代码按钮
        element = driver2.find_element("xpath", '//*[@id="Submit"]')
        element.click()
        continue


def Copy_mode():
    q = Queue()
    record_id = set()

    @login(num=None)
    def record_true_id(driver_copy):

        driver_copy.find_element('xpath', '//*[@id="navbar"]/ul[2]/li/a/span[2]').click()  # 这个是登录成功后的个人中心按钮
        driver_copy.find_element('xpath',
                                 '/html/body/div[1]/nav/div/div[2]/ul[2]/li/ul/li[4]/a/span').click()  # 这个是我的提交按钮
        last_html_id = []
        # print(Fore.RED + '-------------------开始记录正确的答案id，避免重复输入-------------------' + Fore.RESET)
        print('正在记录正确的答案id，避免重复输入，请稍等！')
        window.WriteInfo.emit('normal',
                              '-------------------开始记录正确的答案id，避免重复输入-------------------', 1)
        window.WriteInfo.emit('normal', '正在记录正确的答案id，避免重复输入，请稍等！', 1)
        page = 0
        while True:
            page += 1
            html = driver_copy.page_source
            html_tree = etree.HTML(html)
            now_html_id = html_tree.xpath(f'//*[@id="result-tab"]/tbody/tr/td[3]/div/a/text()')
            for index in range(1, 21):
                question_status = html_tree.xpath(f'//*[@id="result-tab"]/tbody/tr[{index}]/td[4]/span[2]/text()')
                if question_status:
                    question_status = question_status[0]
                if question_status in ['正确', '*正确']:
                    question_id = html_tree.xpath(f'//*[@id="result-tab"]/tbody/tr[{index}]/td[3]/div/a/text()')[0]
                    record_id.add(question_id)
                    text = "第%s页第%s题是正确的，%s ！" % (page, index, question_id)
                    print(text)
                    window.WriteInfo.emit("normal", text, 1)
                else:
                    continue
            else:
                if now_html_id == last_html_id:
                    print('已经到达最后一页！')
                    window.WriteInfo.emit('normal', '已经到达最后一页！', 1)
                    break
                else:
                    last_html_id = now_html_id
                    driver_copy.find_element('xpath', '//*[@id="center"]/a[3]').click()
                    # print('进入下一页！')
        print('答案id记录完成！共计%s道正确题目！' % len(record_id))
        window.WriteInfo.emit('event',
                              '[%s]答案id记录完成！共计%s道正确题目！' % (
                                  time.strftime("%H:%M:%S", time.localtime()), len(record_id)), 1)
        print(record_id)

    @login(num=None)
    def copy_answer_thread(driver):

        driver.find_element('xpath', '//*[@id="navbar"]/ul[2]/li/a/span[2]').click()  # 这个是登录成功后的个人中心按钮
        driver.find_element('xpath',
                            '/html/body/div[1]/nav/div/div[2]/ul[2]/li/ul/li[4]/a/span').click()
        question_list = []
        page = 0
        driver.maximize_window()
        cookies = driver.get_cookies()  # 获取当前会话的cookie
        # 构造cookie字典
        cookie_dict = {}
        for cookie in cookies:
            cookie_dict[cookie['name']] = cookie['value']
        # 创建requests会话
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/88.0.4324.150 Safari/537.36'})
        session.cookies.update(cookie_dict)
        last_id_list = []
        dog = set()

        while True:
            now_id_list = []
            page += 1
            html = driver.page_source
            html_tree = etree.HTML(html)
            # 使用CSS选择器选择所有的行
            rows = html_tree.cssselect('tbody tr.evenrow, tbody tr.oddrow')
            # 循环遍历每一行
            count = 0
            for row in rows:
                # 提取所需的信息
                if row.cssselect('.btn.btn-success'):
                    count = count + 1
                    input_record = row.cssselect('td')[0].text
                    idd = row.cssselect('td div.center a')[0].text
                    dog.add(idd)
                    now_id_list.append(idd)
                    two_response = session.get('http://39.106.228.241/every_do_problem.php?id={0}'.format(idd)).text
                    two_tree = etree.HTML(two_response)
                    q_title = two_tree.cssselect('div.jumbotron title')[0].text
                    q_body = 题目拼接(two_tree)
                    print("正在解析第%s页第%s题：%s" % (page, idd, q_title))
                    window.WriteInfo.emit('normal', "正在解析第%s页第%s题：%s" % (page, idd, q_title), 1)
                    answer_url = f"http://39.106.228.241/submitpage.php?id={idd}&sid={input_record}"
                    response = session.get(answer_url).text
                    tree = etree.HTML(response)
                    question_answer = tree.cssselect('pre#source')[0].text
                    question_list.append(
                        Question(question_id=idd, question_answer=question_answer, question_title=q_title,
                                 question_body=q_body, question_language=Language,
                                 question_owner=Username))
                else:
                    continue
            js = "window.scrollTo(0,700);"
            driver.execute_script(js)
            next_page_url = html_tree.cssselect('div#center a:contains("Next Page")')[0].get('href')
            next_page_url = 'http://39.106.228.241/' + next_page_url

            if now_id_list == last_id_list:
                window.WriteInfo.emit('event',
                                      f'朋友{friend_username}的答案数据已全部保存至本地！共计{len(question_list)}题！', 1)
                print()
                break
            else:
                # 结束解析一页
                print()
                last_id_list = now_id_list
                driver.get(next_page_url)

        for qq in question_list:
            q.put(qq)
        print("剔除重复题目，剩余{}".format(len(question_list)))

        window.WriteInfo.emit('event', '[{}]-------------------Copy线程结束-------------------'.format(
            time.strftime('%H:%M:%S')), 1)

    @login(num=None)
    def put_answer_thread(driver):

        while not q.empty():
            question_item = q.get()
            try:
                element = driver.find_element('xpath',
                                              '/html/body/div[1]/div/center/table[1]/tbody/tr/td[2]/form/input')
                element.send_keys(question_item.get_id())
                driver.find_element('xpath', '/html/body/div[1]/div/center/table[1]/tbody/tr/td[2]/form/button').click()
            except AttributeError:
                element = driver.find_element('xpath',
                                              '/html/body/div/div/center/table[1]/tbody/tr/td[2]/form/input')
                element.send_keys(question_item.get_id())
                driver.find_element('xpath', '/html/body/div[1]/div/center/table[1]/tbody/tr/td[2]/form/button').click()
            except NoSuchElementException:
                element = driver.find_element(By.CSS_SELECTOR, '.form-control.search-query')
                element.send_keys(question_item.get_id())
                driver.find_element('xpath', '/html/body/div[1]/div/center/table[1]/tbody/tr/td[2]/form/button').click()
            # 这里是选择题单的界面
            try:
                driver.find_element('xpath', '/html/body/div/div/a[1]').click()
                driver.find_element('xpath', '/html/body/div/div/center[2]/a[1]').click()  # 进入写代码页面,点的是提交按钮
                driver.find_element('xpath', '//*[@id="source"]/div[2]/div').click()  # 点击输入框
            except NoSuchElementException:
                driver.find_element('xpath', '/html/body/div/div/center[2]/a[1]').click()  # 进入写代码页面,点的是提交按钮
                driver.find_element('xpath', '//*[@id="source"]/div[2]/div').click()  # 点击输入框
            window.WriteInfo.emit('normal', "正在粘贴第{}题：{}".format(question_item.get_id(), question_item.get_title()), 1)
            input_code(driver, question_item)
            window.WriteInfo.emit('event', "粘贴代码成功！", 1)
            # 调用识别函数，并返回验证码
            img_code1 = driver.find_element("xpath", '//*[@id="vcode"]')  # 验证码图片元素对象
            element = driver.find_element("xpath", '//*[@id="language_span"]/input')  # 这个是提交答案的验证码输入框
            # 调用识别函数并返回验证码,这里是提交的验证码
            catch1 = verify_code(img_code=img_code1)
            element.click()
            driver.switch_to.active_element.send_keys(catch1)  # 将识别到的验证码输入到框内
            # 直接点击提交代码按钮
            element = driver.find_element("xpath", '//*[@id="Submit"]')
            element.click()
            time.sleep(5)
            if len(driver.window_handles) > 2:
                # 获取所有标签页的句柄列表
                driver.execute_script(f"window.open('http://39.106.228.241/problemset.php', '_blank')")
                handles = driver.window_handles
                # 关闭第一个标签页（索引为 0）
                driver.switch_to.window(handles[0])
                driver.close()
                driver.switch_to.window(driver.window_handles[-1])
            else:
                driver.execute_script(f"window.open('http://39.106.228.241/problemset.php', '_blank')")
                driver.switch_to.window(driver.window_handles[-1])
        window.WriteInfo.emit('event',
                              '[{}]-------------------粘贴线程结束!bye bye-------------------'.format(
                                  time.strftime("%Y-%m-%d %H:%M:%S")), 1)

    record_true_id()
    if ThreadStatus is True:
        copy_answer_thread()
    if ThreadStatus is True:
        put_answer_thread()
    window.pushButton.setEnabled(True)  # 恢复按钮
    window.pushButton.setText("再次运行")


@login(num=2)
def Full_automatic(driver):
    global ai
    cookies = driver.get_cookies()  # 获取当前会话的cookie
    # 构造cookie字典
    cookie_dict = {}
    for cookie in cookies:
        cookie_dict[cookie['name']] = cookie['value']
    # 创建requests会话
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.150 Safari/537.36'})
    session.cookies.update(cookie_dict)
    # 判断题目数据是否为空，如果为空，或者太小那么就重新获取
    q_ai = Queue()
    All_list = []

    def get_data(num):
        html2 = session.get(f'http://39.106.228.241/problemset.php?page={num}').text
        html_tree = etree.HTML(html2)  # 改用lxml识别
        id_list = html_tree.xpath('//*[@id="problemset"]/tbody/tr/td[2]/div/text()')
        title_list = html_tree.xpath('//*[@id="problemset"]/tbody/tr/td[3]/div/a/text()')
        grade_list = html_tree.xpath('//*[@id="problemset"]/tbody/tr/td[5]/div/a/text()')
        status_list = html_tree.xpath('//*[@id="problemset"]/tbody/tr/td[1]/div/text()')
        # 创建Problem对象列表
        problem_list = [
            Question(question_id=id_, question_title=title_, question_grade=grade_, question_status=status_)
            for
            id_, title_, grade_, status_ in
            zip(id_list, title_list, grade_list, status_list)]  # 用列表推导式创建对象
        q_ai.put(problem_list)

    # 创建线程列表
    threads = []
    # 启动21个线程
    for ii in range(21):
        thread = Thread(target=get_data, args=(ii,))
        thread.setName(f't{ii}')
        thread.start()
        threads.append(thread)
    # 等待所有线程结束
    for thread in threads:
        thread.join()

    for list_class_question in q_ai.queue:  # 把队列中的数据添加到列表中
        # 用列表推导式从object中提取属性创建字典列表
        new_list = [
            {'id': q.id, 'title': q.title, 'grade': q.grade, 'status': q.status} for
            q in list_class_question]  # 用列表推导式从object中提取属性创建字典列表
        All_list.extend(new_list)
    # 将字典添加到列表中
    new_ai_question_list = sort_question_data(All_list)
    print('\n21个线程全部结束！共计{}个可做题目！\n'.format(len(new_ai_question_list)))
    text = '21个线程全部结束！共计{}个可做题目'.format(len(new_ai_question_list))
    window.WriteInfo.emit('event', text, 2)
    count1 = 0
    for row_dic in new_ai_question_list:

        waiting_addressed_question_id = row_dic['id']
        waiting_addressed_question_title = row_dic['title']
        waiting_addressed_question_grade = row_dic['grade']
        waiting_addressed_question_status = row_dic['status']
        if waiting_addressed_question_status in ['Y', '正确', '*正确']:
            continue
        count1 += 1
        waiting_addressed_question_url = f"http://39.106.228.241/problem.php?id={waiting_addressed_question_id}"
        window.WriteInfo.emit('normal', "  ", 2)
        current_time = time.strftime("%H:%M:%S", time.localtime())
        window.WriteInfo.emit('normal', f" {current_time} ".center(70, '-'), 2)
        window.WriteInfo.emit('normal', "  ", 2)
        text = '【任务{}】当前问题为：{} {}'.format(count1, waiting_addressed_question_id,
                                                 waiting_addressed_question_title)
        print(text)
        window.WriteInfo.emit('normal', "  ", 2)
        window.WriteInfo.emit('event', text, 2)
        window.WriteInfo.emit('normal', "  ", 2)
        text = "有{}人解决了这个题目, 问题描述如下：".format(waiting_addressed_question_grade)
        print(text)
        window.WriteInfo.emit('info', "  ", 2)

        driver.execute_script(f"window.open('{waiting_addressed_question_url}', '_blank')")
        driver.switch_to.window(driver.window_handles[-1])
        '''
        以下代码是用来获取题目的所有信息
        '''
        response = session.get(waiting_addressed_question_url)  # 响应对象
        html = etree.HTML(response.text)  # 解析响应为dom树
        timu = 题目拼接(html=html)
        window.WriteInfo.emit('normal', timu, 2)
        qu_text = (
            f"""你是一位{Language}语言题目解题大师，你擅长解题，现在你参加了一场考试，你需要通过我给定的题目生成满足我的要求的{Language}语言代码，
                此外还有考试要求你要遵守：\n
                1,我会直接把题目描述和输入描述，输出描述以及样例输入，样例输出和要求，直接提供给你，而你应当依据题目描述，输入描述和输出描述以及要求所描述的内容，生成正确的符合题意的{Language}语言代码.\n
                2,记住，你只需要生成代码，一定不能出现 printf("请输入x的值：");类似的代码，因为你是在考试，不需要在代码里写请输入之类的语句，你也不可以提问我.\n
                3,代码里严禁出现注释！！代码里不能出现注释！！代码里不能出现注释！！\n
                4,代码的格式在保证代码正确的前提下，尽量减少换行的出现\n
                现在我将提供给你第一个题目：\n""")
        qu_text = qu_text + timu
        print(timu)
        """
        这个地方选择调用哪个Ai模型
        """
        if ai == 1:  # 调用文心一言的接口，以便于获取答案
            answer_text = wenxin(qu_text)
            window.WriteInfo.emit('normal', answer_text, 2)
            answer = text_pocessing(answer_text, delimiter="#include <stdio.h>", ab=True)  # 处理文本前的不需要字符
            answer = text_pocessing(answer, delimiter="```")  # 处理文本后的不需要字符，得到正确格式的答案
        elif ai == 2:  # 从智谱Ai获取答案
            answer_text = zhipu(qu_text)  # 智谱Ai的响应
            answer = text_pocessing(answer_text, delimiter="#include <stdio.h>", ab=True)  # 处理文本前的不需要字符
            answer = text_pocessing(answer, delimiter="```")  # 处理文本后的不需要字符，得到正确格式的答案
        elif ai == 3:  # 从ChatGPT3.5获取答案
            try:
                answer_text = Chatgpt3_5(qu_text)  # ChatGPT的响应
                window.WriteInfo.emit('normal', answer_text, 2)
                answer = text_pocessing(answer_text, delimiter="#include <stdio.h>", ab=True)  # 处理文本前的不需要字符
                answer = text_pocessing(answer, delimiter="```")  # 处理文本后的不需要字符，得到正确格式的答案
            except openai.error.APIError as e:
                print("An API error occurred:", e)
                window.WriteInfo.emit('event', "  ", 2)
                current_time = time.strftime("%H:%M:%S", time.localtime())
                window.WriteInfo.emit('event', "{}发生了一个API错误！".format(current_time), 2)
                window.LoginError.emit("API错误！", "ChatGPT的API额度耗尽,更换新的API令牌！")
                break
            except openai.error.ServiceUnavailableError as e:
                print("发生了一个GPT服务错误:", e)
                window.WriteInfo.emit('event', "  ", 2)
                current_time = time.strftime("%H:%M:%S", time.localtime())
                window.WriteInfo.emit('event', "{}发生了一个GPT服务错误！".format(current_time), 2)
                window.LoginError.emit("GPT服务错误！",
                                       "出现这个错误，表示GPT服务器的载荷过大，你需要等一段时间后重试！".format(
                                           current_time))
                break
            except openai.error.AuthenticationError as e:
                print("令牌过期！", e)
                window.WriteInfo.emit('event', "  ", 2)
                current_time = time.strftime("%H:%M:%S", time.localtime())
                window.WriteInfo.emit('event', "{}；令牌过期！".format(current_time), 2)
                window.LoginError.emit("令牌过期！", "更换新的API令牌！")
        driver.find_element("xpath", '/html/body/div[1]/div/center[2]/a[1]').click()  # 点击提交按钮
        # 代码文本框

        text_input = driver.find_element("xpath", '//*[@id="source"]/div[2]/div')
        text_input.click()  # 点击代码输入框，获取焦点
        # print('代码输入框聚焦成功！')

        question.set_answer(answer)
        # 输入答案
        input_code(driver=driver, question_class=question)  # 这里传递的是个Question对象
        window.WriteInfo.emit('event', "粘贴代码成功！", 2)
        # 调用识别函数，并返回验证码
        img_code = driver.find_element("xpath", '//*[@id="vcode"]')  # 验证码图片元素对象
        element = driver.find_element("xpath", '//*[@id="language_span"]/input')  # 这个是提交答案的验证码输入框
        # 验证码识别
        catch = verify_code(img_code=img_code)
        element.click()
        driver.switch_to.active_element.send_keys(catch)  # 将识别到的验证码输入到框内
        # 直接点击提交代码按钮
        element = driver.find_element("xpath", '//*[@id="Submit"]')
        element.click()
        time.sleep(5)
        if len(driver.window_handles) > 2:
            # 获取所有标签页的句柄列表
            handles = driver.window_handles
            # 关闭第一个标签页（索引为 0）
            driver.switch_to.window(handles[0])
            driver.close()
            driver.switch_to.window(driver.window_handles[-1])
    window.pushButton_2.setEnabled(True)  # 恢复按钮
    window.pushButton_2.setText("提交并运行")  # 恢复文本


class Question:
    def __init__(self, question_id=None, question_title=None, question_body=None, question_language=None,
                 question_answer=None, question_grade=None,
                 question_status=None, question_owner=None):
        self.id = question_id
        self.title = question_title
        self.body = question_body
        self.language = question_language
        self.answer = question_answer
        self.grade = question_grade
        self.status = question_status
        self.owner = question_owner

    def get_id(self):
        return self.id

    def set_id(self, question_id):
        self.id = question_id

    def get_title(self):
        return self.title

    def set_title(self, question_title):
        self.title = question_title

    def get_body(self):
        return self.body

    def set_body(self, question_body):
        self.body = question_body

    def get_language(self):
        return self.language

    def set_language(self, question_language):
        self.language = question_language

    def get_answer(self):
        return self.answer

    def set_answer(self, question_answer):
        self.answer = question_answer

    def get_grade(self):
        return self.grade

    def set_grade(self, question_grade):
        self.grade = question_grade

    def get_status(self):
        return self.status

    def set_status(self, question_status):
        self.status = question_status


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    # 设置窗口图标
    # 假设 images.money 包含了 base64 编码的图片数据
    image_ico = base64.b64decode(images.main_ico)
    pixmap = QPixmap()
    # 将解码后的图片数据转换为 QPixmap 对象
    pixmap.loadFromData(image_ico)
    # 将 QPixmap 对象转换为 QIcon 对象，并设置为窗口图标
    icon = QIcon(pixmap)
    window.setWindowIcon(icon)
    window.show()
    question = Question()
    app.exec()
