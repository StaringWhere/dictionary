from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class Dictionary(QMainWindow):
    def __init__(self):

        # 建立QWidget对象，不然Timer绑定的对象函数不执行
        super().__init__()
        # 渲染窗口
        self.initUI()
        # 监听剪贴板
        self.initClip()

    # 渲染窗口
    def initUI(self):

        # 设置窗口标题
        self.setWindowTitle(u'读论文可太难了')
        # 窗口大小
        self.resize(600, 800)
        # 窗口置顶
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # 建立QWebEngineView对象
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        
        # 展示窗口
        self.show()
    
    def initClip(self):

        # 建立剪贴板
        self.cb = QApplication.clipboard()
        # 初始化剪贴板单词
        self.last_word = self.word = self.cb.mimeData().text()
        # 声明定时器
        self.timer_clipboard = QTimer()
        # 定时器触发间隔，并开始
        self.timer_clipboard.start(200) 
        # 定时器触发方法
        self.timer_clipboard.timeout.connect(self.is_clipboard_change) 

        # 监听剪贴板，与QWebEngineView().load(QUrl)一起失效，原因未知
        # self.cb.dataChanged.connect(test)

    # 检查剪贴板变化
    def is_clipboard_change(self):
        
        # 获取剪贴板内容
        data = self.cb.mimeData()
        # 内容为文本
        if data.hasText():
            self.last_word = self.word
            self.word = data.text()
            if self.word != self.last_word:
                print(self.word)
                # 查询单词
                url = 'http://youdao.com/w/{}/'.format(self.word)
                self.browser.load(QUrl(url))

if __name__ == '__main__':

    # 创建应用
    app = QApplication(sys.argv)
    # 创建主窗口
    dict = Dictionary()
    # 运行应用，监听事件
    sys.exit(app.exec_())