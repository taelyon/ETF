# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stock.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1900, 990)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_control = QtWidgets.QFrame(self.centralwidget)
        self.frame_control.setGeometry(QtCore.QRect(0, 0, 200, 991))
        self.frame_control.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_control.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_control.setObjectName("frame_control")
        self.groupBox_update = QtWidgets.QGroupBox(self.frame_control)
        self.groupBox_update.setGeometry(QtCore.QRect(10, 10, 181, 111))
        self.groupBox_update.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_update.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_update.setObjectName("groupBox_update")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_update)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 14, 307, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_update1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_update1.setObjectName("btn_update1")
        self.horizontalLayout_5.addWidget(self.btn_update1)
        self.btn_update2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_update2.setObjectName("btn_update2")
        self.horizontalLayout_5.addWidget(self.btn_update2)
        self.btn_update3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_update3.setObjectName("btn_update3")
        self.horizontalLayout_5.addWidget(self.btn_update3)
        self.btn_stop1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_stop1.setObjectName("btn_stop1")
        self.horizontalLayout_5.addWidget(self.btn_stop1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.ent_stock = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.ent_stock.setObjectName("ent_stock")
        self.verticalLayout.addWidget(self.ent_stock)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_period1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.btn_period1.setObjectName("btn_period1")
        self.horizontalLayout_2.addWidget(self.btn_period1)
        self.btn_period2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.btn_period2.setObjectName("btn_period2")
        self.horizontalLayout_2.addWidget(self.btn_period2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btn_update4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_update4.setObjectName("btn_update4")
        self.verticalLayout.addWidget(self.btn_update4)
        self.groupBox_hold = QtWidgets.QGroupBox(self.frame_control)
        self.groupBox_hold.setGeometry(QtCore.QRect(10, 440, 181, 221))
        self.groupBox_hold.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_hold.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_hold.setObjectName("groupBox_hold")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_hold)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 14, 229, 201))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lb_hold = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.lb_hold.setObjectName("lb_hold")
        self.verticalLayout_5.addWidget(self.lb_hold)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btn2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        self.btn2.setIconSize(QtCore.QSize(16, 16))
        self.btn2.setObjectName("btn2")
        self.horizontalLayout_10.addWidget(self.btn2)
        self.btn_del1 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn_del1.setObjectName("btn_del1")
        self.horizontalLayout_10.addWidget(self.btn_del1)
        self.btn_addint1 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn_addint1.setObjectName("btn_addint1")
        self.horizontalLayout_10.addWidget(self.btn_addint1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.groupBox_int = QtWidgets.QGroupBox(self.frame_control)
        self.groupBox_int.setGeometry(QtCore.QRect(10, 670, 181, 221))
        self.groupBox_int.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_int.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_int.setObjectName("groupBox_int")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_int)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 14, 229, 201))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lb_int = QtWidgets.QListWidget(self.verticalLayoutWidget_4)
        self.lb_int.setObjectName("lb_int")
        self.verticalLayout_6.addWidget(self.lb_int)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btn3 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.btn3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        self.btn3.setIconSize(QtCore.QSize(16, 16))
        self.btn3.setObjectName("btn3")
        self.horizontalLayout_11.addWidget(self.btn3)
        self.btn_del2 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.btn_del2.setObjectName("btn_del2")
        self.horizontalLayout_11.addWidget(self.btn_del2)
        self.btn_addhold1 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.btn_addhold1.setObjectName("btn_addhold1")
        self.horizontalLayout_11.addWidget(self.btn_addhold1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.groupBox_find = QtWidgets.QGroupBox(self.frame_control)
        self.groupBox_find.setGeometry(QtCore.QRect(10, 900, 181, 71))
        self.groupBox_find.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_find.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_find.setObjectName("groupBox_find")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_find)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 14, 229, 51))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.ent = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.ent.setObjectName("ent")
        self.verticalLayout_7.addWidget(self.ent)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_find = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.btn_find.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_find.sizePolicy().hasHeightForWidth())
        self.btn_find.setSizePolicy(sizePolicy)
        self.btn_find.setIconSize(QtCore.QSize(16, 16))
        self.btn_find.setObjectName("btn_find")
        self.horizontalLayout_4.addWidget(self.btn_find)
        self.btn_addhold2 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_addhold2.sizePolicy().hasHeightForWidth())
        self.btn_addhold2.setSizePolicy(sizePolicy)
        self.btn_addhold2.setObjectName("btn_addhold2")
        self.horizontalLayout_4.addWidget(self.btn_addhold2)
        self.btn_addint2 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_addint2.sizePolicy().hasHeightForWidth())
        self.btn_addint2.setSizePolicy(sizePolicy)
        self.btn_addint2.setObjectName("btn_addint2")
        self.horizontalLayout_4.addWidget(self.btn_addint2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.groupBox_search = QtWidgets.QGroupBox(self.frame_control)
        self.groupBox_search.setGeometry(QtCore.QRect(10, 130, 181, 301))
        self.groupBox_search.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox_search.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_search.setObjectName("groupBox_search")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_search)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 14, 307, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_search1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_search1.setObjectName("btn_search1")
        self.horizontalLayout_3.addWidget(self.btn_search1)
        self.btn_search2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_search2.setObjectName("btn_search2")
        self.horizontalLayout_3.addWidget(self.btn_search2)
        self.btn_search3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_search3.setObjectName("btn_search3")
        self.horizontalLayout_3.addWidget(self.btn_search3)
        self.btn_stop2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_stop2.setObjectName("btn_stop2")
        self.horizontalLayout_3.addWidget(self.btn_stop2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.lb_search = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.lb_search.setObjectName("lb_search")
        self.verticalLayout_4.addWidget(self.lb_search)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn.sizePolicy().hasHeightForWidth())
        self.btn.setSizePolicy(sizePolicy)
        self.btn.setIconSize(QtCore.QSize(16, 16))
        self.btn.setObjectName("btn")
        self.horizontalLayout_6.addWidget(self.btn)
        self.btn_addhold = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_addhold.sizePolicy().hasHeightForWidth())
        self.btn_addhold.setSizePolicy(sizePolicy)
        self.btn_addhold.setObjectName("btn_addhold")
        self.horizontalLayout_6.addWidget(self.btn_addhold)
        self.btn_addint = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_addint.sizePolicy().hasHeightForWidth())
        self.btn_addint.setSizePolicy(sizePolicy)
        self.btn_addint.setObjectName("btn_addint")
        self.horizontalLayout_6.addWidget(self.btn_addint)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.frame_plot = QtWidgets.QFrame(self.centralwidget)
        self.frame_plot.setGeometry(QtCore.QRect(200, 0, 1000, 900))
        self.frame_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plot.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame_plot.setObjectName("frame_plot")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.frame_plot)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 0, 991, 891))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")



        self.frame_info = QtWidgets.QFrame(self.centralwidget)
        self.frame_info.setGeometry(QtCore.QRect(1200, 0, 701, 901))
        self.frame_info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_info.setObjectName("frame_info")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.frame_info)
        self.webEngineView.setGeometry(QtCore.QRect(0, 0, 701, 891))
        self.webEngineView.setProperty("url", QtCore.QUrl("https://m.stock.naver.com/index.html#/"))
        self.webEngineView.setObjectName("webEngineView")
        self.frame_log = QtWidgets.QFrame(self.centralwidget)
        self.frame_log.setGeometry(QtCore.QRect(200, 900, 1701, 91))
        self.frame_log.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_log.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_log.setObjectName("frame_log")
        self.log_widget = QtWidgets.QTextBrowser(self.frame_log)
        self.log_widget.setGeometry(QtCore.QRect(0, 0, 1701, 90))
        self.log_widget.setObjectName("log_widget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_update1.clicked.connect(MainWindow.update_stocks)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_update.setTitle(_translate("MainWindow", "종목 업데이트"))
        self.btn_update1.setText(_translate("MainWindow", "한국"))
        self.btn_update2.setText(_translate("MainWindow", "미국"))
        self.btn_update3.setText(_translate("MainWindow", "전체"))
        self.btn_stop1.setText(_translate("MainWindow", "중단"))
        self.btn_period1.setText(_translate("MainWindow", "최근"))
        self.btn_period2.setText(_translate("MainWindow", "장기"))
        self.btn_update4.setText(_translate("MainWindow", "업데이트"))
        self.groupBox_hold.setTitle(_translate("MainWindow", "보유 종목"))
        self.btn2.setText(_translate("MainWindow", "선택"))
        self.btn_del1.setText(_translate("MainWindow", "삭제"))
        self.btn_addint1.setText(_translate("MainWindow", "관심추가"))
        self.groupBox_int.setTitle(_translate("MainWindow", "관심 종목"))
        self.btn3.setText(_translate("MainWindow", "선택"))
        self.btn_del2.setText(_translate("MainWindow", "삭제"))
        self.btn_addhold1.setText(_translate("MainWindow", "보유추가"))
        self.groupBox_find.setTitle(_translate("MainWindow", "종목 조회"))
        self.btn_find.setText(_translate("MainWindow", "선택"))
        self.btn_addhold2.setText(_translate("MainWindow", "보유추가"))
        self.btn_addint2.setText(_translate("MainWindow", "관심추가"))
        self.groupBox_search.setTitle(_translate("MainWindow", "종목 탐색"))
        self.btn_search1.setText(_translate("MainWindow", "한국"))
        self.btn_search2.setText(_translate("MainWindow", "미국"))
        self.btn_search3.setText(_translate("MainWindow", "전체"))
        self.btn_stop2.setText(_translate("MainWindow", "중단"))
        self.btn.setText(_translate("MainWindow", "선택"))
        self.btn_addhold.setText(_translate("MainWindow", "보유추가"))
        self.btn_addint.setText(_translate("MainWindow", "관심추가"))
from PyQt5 import QtWebEngineWidgets
