# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import sys
import designer
import tweepy
import twpy


class Example(QtGui.QMainWindow, designer.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.textEdit.setText("test textEdit")

    def clicked(self):
        self.textEdit.setText("")
        results = []
        temp = twpy.api.search(q="#メモ",count = 10)
        for i in temp:
            results.append(i.text)
        print len(results)
        for i in range(len(results)):
            self.textEdit.append(results[i] + "\n")

def main():
    app = QtGui.QApplication(sys.argv)
    form = Example()
    form.setWindowTitle("tweet memo")
    form.show()

    form.btn1.clicked.connect(lambda: form.clicked())
    form.btn2.clicked.connect(app.quit)

    app.exec_()

if __name__ ==  "__main__":
    main()
