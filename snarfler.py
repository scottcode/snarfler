from __future__ import print_function
import requests
from IPython.display import HTML, IFrame

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from PyQt4 import QtCore, QtGui, QtWebKit
from lxml import html


class WebPage(QtWebKit.QWebPage):
    """from http://stackoverflow.com/a/21918243/1789708"""
    def __init__(self):
        QtWebKit.QWebPage.__init__(self)
        self.mainFrame().loadFinished.connect(self.handleLoadFinished)

    def process(self, items):
        self._items = iter(items)
        self.fetchNext()

    def fetchNext(self):
        try:
            self._url, self._func = next(self._items)
            self.mainFrame().load(QtCore.QUrl(self._url))
        except StopIteration:
            return False
        return True

    def handleLoadFinished(self):
        self._func(self._url, self.mainFrame().toHtml())
        if not self.fetchNext():
            print('# processing complete')
            QtGui.qApp.quit()


class Render(QWebPage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()

# r = requests.get(url1)
# rendered = Render(url1)
#result is a QString.
# result = rendered.frame.toHtml()


def rendered_html_from_url(url):
    rendered = Render(url)
    return rendered.frame.toHtml()


def table_from_url(url):
    pass


def partname_from_url(url):
    pass


def price_from_url(url):
    pass

