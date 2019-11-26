"""Original from
http://stackoverflow.com/a/21918243/1789708

"""

import sys, signal
from bs4 import BeautifulSoup
from bs4.dammit import UnicodeDammit
from PyQt4 import QtCore, QtGui, QtWebKit

class WebPage(QtWebKit.QWebPage):
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


def funcA(url, html):
    print('# processing:', url, len(html), unicode(html)[100:200])
    # soup = BeautifulSoup(UnicodeDammit(html).unicode_markup)
    # do stuff with soup...

def funcB(url, html):
    print('# processing:', url, len(html), unicode(html)[100:200])
    # soup = BeautifulSoup(UnicodeDammit(html).unicode_markup)
    # do stuff with soup...

if __name__ == '__main__':

    items = [
        ('http://stackoverflow.com', funcA),
        ('http://google.com', funcB),
        ]

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    print('Press Ctrl+C to quit\n')
    app = QtGui.QApplication(sys.argv)
    webpage = WebPage()
    webpage.process(items)
    sys.exit(app.exec_())