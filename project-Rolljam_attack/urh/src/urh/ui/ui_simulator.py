# -*- coding: utf-8 -*-

#
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SimulatorTab(object):
    def setupUi(self, SimulatorTab):
        SimulatorTab.setObjectName("SimulatorTab")
        SimulatorTab.resize(842, 689)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(SimulatorTab)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scrollArea = QtWidgets.QScrollArea(SimulatorTab)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 842, 689))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitterLeftRight = QtWidgets.QSplitter(self.scrollAreaWidgetContents)
        self.splitterLeftRight.setStyleSheet(
            "QSplitter::handle:horizontal {\n"
            "margin: 4px 0px;\n"
            "    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, \n"
            "stop:0 rgba(255, 255, 255, 0), \n"
            "stop:0.5 rgba(100, 100, 100, 100), \n"
            "stop:1 rgba(255, 255, 255, 0));\n"
            "image: url(:/icons/icons/splitter_handle_vertical.svg);\n"
            "}"
        )
        self.splitterLeftRight.setOrientation(QtCore.Qt.Horizontal)
        self.splitterLeftRight.setHandleWidth(6)
        self.splitterLeftRight.setObjectName("splitterLeftRight")
        self.layoutWidget = QtWidgets.QWidget(self.splitterLeftRight)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.treeProtocols = GeneratorTreeView(self.layoutWidget)
        self.treeProtocols.setObjectName("treeProtocols")
        self.verticalLayout_3.addWidget(self.treeProtocols)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.listViewSimulate = QtWidgets.QListView(self.layoutWidget)
        self.listViewSimulate.setAlternatingRowColors(True)
        self.listViewSimulate.setObjectName("listViewSimulate")
        self.verticalLayout_3.addWidget(self.listViewSimulate)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.spinBoxNRepeat = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.spinBoxNRepeat.sizePolicy().hasHeightForWidth()
        )
        self.spinBoxNRepeat.setSizePolicy(sizePolicy)
        self.spinBoxNRepeat.setMaximum(9999999)
        self.spinBoxNRepeat.setObjectName("spinBoxNRepeat")
        self.gridLayout.addWidget(self.spinBoxNRepeat, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.spinBoxTimeout = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.spinBoxTimeout.sizePolicy().hasHeightForWidth()
        )
        self.spinBoxTimeout.setSizePolicy(sizePolicy)
        self.spinBoxTimeout.setMinimum(1)
        self.spinBoxTimeout.setMaximum(9999999)
        self.spinBoxTimeout.setObjectName("spinBoxTimeout")
        self.gridLayout.addWidget(self.spinBoxTimeout, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.comboBoxError = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.comboBoxError.sizePolicy().hasHeightForWidth()
        )
        self.comboBoxError.setSizePolicy(sizePolicy)
        self.comboBoxError.setObjectName("comboBoxError")
        self.comboBoxError.addItem("")
        self.comboBoxError.addItem("")
        self.comboBoxError.addItem("")
        self.gridLayout.addWidget(self.comboBoxError, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.spinBoxRetries = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBoxRetries.setMinimum(1)
        self.spinBoxRetries.setMaximum(9999999)
        self.spinBoxRetries.setProperty("value", 10)
        self.spinBoxRetries.setObjectName("spinBoxRetries")
        self.gridLayout.addWidget(self.spinBoxRetries, 3, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.btnStartSim = QtWidgets.QPushButton(self.layoutWidget)
        icon = QtGui.QIcon.fromTheme("media-playback-start")
        self.btnStartSim.setIcon(icon)
        self.btnStartSim.setObjectName("btnStartSim")
        self.verticalLayout_3.addWidget(self.btnStartSim)
        self.splitter = QtWidgets.QSplitter(self.splitterLeftRight)
        self.splitter.setStyleSheet(
            "QSplitter::handle:vertical {\n"
            "margin: 4px 0px;\n"
            "    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, \n"
            "stop:0 rgba(255, 255, 255, 0), \n"
            "stop:0.5 rgba(100, 100, 100, 100), \n"
            "stop:1 rgba(255, 255, 255, 0));\n"
            "image: url(:/icons/icons/splitter_handle_horizontal.svg);\n"
            "}"
        )
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(6)
        self.splitter.setObjectName("splitter")
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("QTabWidget::pane { border: 0; }")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gvSimulator = SimulatorGraphicsView(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gvSimulator.sizePolicy().hasHeightForWidth())
        self.gvSimulator.setSizePolicy(sizePolicy)
        self.gvSimulator.setObjectName("gvSimulator")
        self.verticalLayout.addWidget(self.gvSimulator)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tblViewMessage = SimulatorMessageTableView(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tblViewMessage.sizePolicy().hasHeightForWidth()
        )
        self.tblViewMessage.setSizePolicy(sizePolicy)
        self.tblViewMessage.setAlternatingRowColors(True)
        self.tblViewMessage.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerPixel
        )
        self.tblViewMessage.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerPixel
        )
        self.tblViewMessage.setShowGrid(False)
        self.tblViewMessage.setObjectName("tblViewMessage")
        self.tblViewMessage.horizontalHeader().setHighlightSections(False)
        self.tblViewMessage.verticalHeader().setHighlightSections(False)
        self.verticalLayout_6.addWidget(self.tblViewMessage)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lNumSelectedColumns = QtWidgets.QLabel(self.tab_2)
        self.lNumSelectedColumns.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.lNumSelectedColumns.setObjectName("lNumSelectedColumns")
        self.horizontalLayout_3.addWidget(self.lNumSelectedColumns)
        self.lColumnsSelectedText = QtWidgets.QLabel(self.tab_2)
        self.lColumnsSelectedText.setObjectName("lColumnsSelectedText")
        self.horizontalLayout_3.addWidget(self.lColumnsSelectedText)
        spacerItem = QtWidgets.QSpacerItem(
            138, 33, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.cbViewType = QtWidgets.QComboBox(self.tab_2)
        self.cbViewType.setObjectName("cbViewType")
        self.cbViewType.addItem("")
        self.cbViewType.addItem("")
        self.cbViewType.addItem("")
        self.horizontalLayout_3.addWidget(self.cbViewType)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tabParticipants = QtWidgets.QWidget()
        self.tabParticipants.setObjectName("tabParticipants")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tabParticipants)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableViewParticipants = ParticipantTableView(self.tabParticipants)
        self.tableViewParticipants.setObjectName("tableViewParticipants")
        self.horizontalLayout.addWidget(self.tableViewParticipants)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.btnAddParticipant = QtWidgets.QToolButton(self.tabParticipants)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.btnAddParticipant.setIcon(icon)
        self.btnAddParticipant.setObjectName("btnAddParticipant")
        self.verticalLayout_9.addWidget(self.btnAddParticipant)
        self.btnRemoveParticipant = QtWidgets.QToolButton(self.tabParticipants)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.btnRemoveParticipant.setIcon(icon)
        self.btnRemoveParticipant.setObjectName("btnRemoveParticipant")
        self.verticalLayout_9.addWidget(self.btnRemoveParticipant)
        self.btnUp = QtWidgets.QToolButton(self.tabParticipants)
        icon = QtGui.QIcon.fromTheme("go-up")
        self.btnUp.setIcon(icon)
        self.btnUp.setObjectName("btnUp")
        self.verticalLayout_9.addWidget(self.btnUp)
        self.btnDown = QtWidgets.QToolButton(self.tabParticipants)
        icon = QtGui.QIcon.fromTheme("go-down")
        self.btnDown.setIcon(icon)
        self.btnDown.setObjectName("btnDown")
        self.verticalLayout_9.addWidget(self.btnDown)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_9.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.tabWidget.addTab(self.tabParticipants, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.layoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblMsgFieldsValues = QtWidgets.QLabel(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lblMsgFieldsValues.sizePolicy().hasHeightForWidth()
        )
        self.lblMsgFieldsValues.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblMsgFieldsValues.setFont(font)
        self.lblMsgFieldsValues.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMsgFieldsValues.setObjectName("lblMsgFieldsValues")
        self.verticalLayout_4.addWidget(self.lblMsgFieldsValues)
        self.detail_view_widget = QtWidgets.QStackedWidget(self.layoutWidget_3)
        self.detail_view_widget.setObjectName("detail_view_widget")
        self.page_empty = QtWidgets.QWidget()
        self.page_empty.setObjectName("page_empty")
        self.detail_view_widget.addWidget(self.page_empty)
        self.page_goto_action = QtWidgets.QWidget()
        self.page_goto_action.setObjectName("page_goto_action")
        self.verticalLayout_7 = QtWidgets.QGridLayout(self.page_goto_action)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.page_goto_action)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.goto_combobox = QtWidgets.QComboBox(self.page_goto_action)
        self.goto_combobox.setObjectName("goto_combobox")
        self.verticalLayout_7.addWidget(self.goto_combobox, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.verticalLayout_7.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_7.addItem(spacerItem3, 1, 0, 1, 3)
        self.detail_view_widget.addWidget(self.page_goto_action)
        self.page_message = QtWidgets.QWidget()
        self.page_message.setObjectName("page_message")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_message)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_10 = QtWidgets.QLabel(self.page_message)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 1, 0, 1, 1)
        self.tblViewFieldValues = SimulatorLabelTableView(self.page_message)
        self.tblViewFieldValues.setAlternatingRowColors(True)
        self.tblViewFieldValues.setShowGrid(False)
        self.tblViewFieldValues.setObjectName("tblViewFieldValues")
        self.tblViewFieldValues.horizontalHeader().setDefaultSectionSize(150)
        self.tblViewFieldValues.horizontalHeader().setStretchLastSection(True)
        self.tblViewFieldValues.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.tblViewFieldValues, 2, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.page_message)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 2, 0, 1, 1)
        self.spinBoxRepeat = QtWidgets.QSpinBox(self.page_message)
        self.spinBoxRepeat.setMinimum(1)
        self.spinBoxRepeat.setObjectName("spinBoxRepeat")
        self.gridLayout_6.addWidget(self.spinBoxRepeat, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_message)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)
        self.lblEncodingDecoding = QtWidgets.QLabel(self.page_message)
        self.lblEncodingDecoding.setObjectName("lblEncodingDecoding")
        self.gridLayout_6.addWidget(self.lblEncodingDecoding, 0, 2, 1, 1)
        self.detail_view_widget.addWidget(self.page_message)
        self.page_rule = QtWidgets.QWidget()
        self.page_rule.setObjectName("page_rule")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_rule)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_12 = QtWidgets.QLabel(self.page_rule)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout_3.addItem(spacerItem4, 1, 0, 1, 2)
        self.ruleCondLineEdit = ExpressionLineEdit(self.page_rule)
        self.ruleCondLineEdit.setObjectName("ruleCondLineEdit")
        self.gridLayout_3.addWidget(self.ruleCondLineEdit, 0, 1, 1, 1)
        self.detail_view_widget.addWidget(self.page_rule)
        self.page_ext_prog_action = QtWidgets.QWidget()
        self.page_ext_prog_action.setObjectName("page_ext_prog_action")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_ext_prog_action)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.checkBoxPassTranscriptSTDIN = QtWidgets.QCheckBox(
            self.page_ext_prog_action
        )
        self.checkBoxPassTranscriptSTDIN.setObjectName("checkBoxPassTranscriptSTDIN")
        self.gridLayout_9.addWidget(self.checkBoxPassTranscriptSTDIN, 2, 0, 1, 4)
        self.label_14 = QtWidgets.QLabel(self.page_ext_prog_action)
        self.label_14.setObjectName("label_14")
        self.gridLayout_9.addWidget(self.label_14, 1, 0, 1, 1)
        self.lineEditTriggerCommand = QtWidgets.QLineEdit(self.page_ext_prog_action)
        self.lineEditTriggerCommand.setReadOnly(False)
        self.lineEditTriggerCommand.setObjectName("lineEditTriggerCommand")
        self.gridLayout_9.addWidget(self.lineEditTriggerCommand, 1, 1, 1, 1)
        self.btnChooseCommand = QtWidgets.QToolButton(self.page_ext_prog_action)
        self.btnChooseCommand.setObjectName("btnChooseCommand")
        self.gridLayout_9.addWidget(self.btnChooseCommand, 1, 2, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout_9.addItem(spacerItem5, 4, 0, 1, 4)
        self.label_18 = QtWidgets.QLabel(self.page_ext_prog_action)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.gridLayout_9.addWidget(self.label_18, 3, 0, 1, 4)
        self.detail_view_widget.addWidget(self.page_ext_prog_action)
        self.page_sleep = QtWidgets.QWidget()
        self.page_sleep.setObjectName("page_sleep")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_sleep)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.page_sleep)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_2.addWidget(self.label_13)
        self.doubleSpinBoxSleep = QtWidgets.QDoubleSpinBox(self.page_sleep)
        self.doubleSpinBoxSleep.setDecimals(6)
        self.doubleSpinBoxSleep.setMaximum(10000.0)
        self.doubleSpinBoxSleep.setProperty("value", 1.0)
        self.doubleSpinBoxSleep.setObjectName("doubleSpinBoxSleep")
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxSleep)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 231, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_10.addItem(spacerItem6)
        self.detail_view_widget.addWidget(self.page_sleep)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinBoxCounterStep = QtWidgets.QSpinBox(self.page)
        self.spinBoxCounterStep.setMinimum(1)
        self.spinBoxCounterStep.setMaximum(999999)
        self.spinBoxCounterStep.setObjectName("spinBoxCounterStep")
        self.gridLayout_2.addWidget(self.spinBoxCounterStep, 2, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.page)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.page)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)
        self.spinBoxCounterStart = QtWidgets.QSpinBox(self.page)
        self.spinBoxCounterStart.setMaximum(999999)
        self.spinBoxCounterStart.setObjectName("spinBoxCounterStart")
        self.gridLayout_2.addWidget(self.spinBoxCounterStart, 1, 1, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout_2)
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_11.addWidget(self.label_17)
        spacerItem7 = QtWidgets.QSpacerItem(
            20, 36, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_11.addItem(spacerItem7)
        self.detail_view_widget.addWidget(self.page)
        self.verticalLayout_4.addWidget(self.detail_view_widget)
        self.verticalLayout_5.addWidget(self.splitterLeftRight)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_8.addWidget(self.scrollArea)

        self.retranslateUi(SimulatorTab)
        self.tabWidget.setCurrentIndex(0)
        self.detail_view_widget.setCurrentIndex(2)

    def retranslateUi(self, SimulatorTab):
        _translate = QtCore.QCoreApplication.translate
        SimulatorTab.setWindowTitle(_translate("SimulatorTab", "Form"))
        self.label.setText(
            _translate("SimulatorTab", "Protocols (Drag&Drop to Flow Graph):")
        )
        self.label_6.setText(_translate("SimulatorTab", "Simulate these participants:"))
        self.label_4.setText(
            _translate("SimulatorTab", "Repeat simulation this often:")
        )
        self.spinBoxNRepeat.setSpecialValueText(_translate("SimulatorTab", "Infinite"))
        self.label_3.setText(_translate("SimulatorTab", "Timeout:"))
        self.spinBoxTimeout.setSuffix(_translate("SimulatorTab", "ms"))
        self.label_7.setText(
            _translate("SimulatorTab", "In case of an overdue response:")
        )
        self.comboBoxError.setItemText(
            0, _translate("SimulatorTab", "Resend last message")
        )
        self.comboBoxError.setItemText(1, _translate("SimulatorTab", "Stop simulation"))
        self.comboBoxError.setItemText(
            2, _translate("SimulatorTab", "Restart simulation")
        )
        self.label_8.setText(_translate("SimulatorTab", "Maximum retries:"))
        self.btnStartSim.setText(_translate("SimulatorTab", "Simulate..."))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab), _translate("SimulatorTab", "Flow Graph")
        )
        self.lNumSelectedColumns.setText(_translate("SimulatorTab", "0"))
        self.lColumnsSelectedText.setText(
            _translate("SimulatorTab", "column(s) selected")
        )
        self.label_5.setText(_translate("SimulatorTab", "Viewtype:"))
        self.cbViewType.setItemText(0, _translate("SimulatorTab", "Bit"))
        self.cbViewType.setItemText(1, _translate("SimulatorTab", "Hex"))
        self.cbViewType.setItemText(2, _translate("SimulatorTab", "ASCII"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2), _translate("SimulatorTab", "Messages")
        )
        self.btnAddParticipant.setToolTip(_translate("SimulatorTab", "Add participant"))
        self.btnAddParticipant.setText(_translate("SimulatorTab", "Add"))
        self.btnRemoveParticipant.setToolTip(
            _translate("SimulatorTab", "Remove participant")
        )
        self.btnRemoveParticipant.setText(_translate("SimulatorTab", "Remove"))
        self.btnUp.setToolTip(
            _translate("SimulatorTab", "Move selected participants up")
        )
        self.btnUp.setText(_translate("SimulatorTab", "..."))
        self.btnDown.setToolTip(
            _translate("SimulatorTab", "Move selected participants down")
        )
        self.btnDown.setText(_translate("SimulatorTab", "..."))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabParticipants),
            _translate("SimulatorTab", "Participants"),
        )
        self.lblMsgFieldsValues.setText(
            _translate("SimulatorTab", "Detail view for item")
        )
        self.label_9.setText(_translate("SimulatorTab", "Goto:"))
        self.label_10.setText(_translate("SimulatorTab", "Copies:"))
        self.label_11.setText(_translate("SimulatorTab", "Labels:"))
        self.label_2.setText(_translate("SimulatorTab", "Coding:"))
        self.lblEncodingDecoding.setText(_translate("SimulatorTab", "-"))
        self.label_12.setText(_translate("SimulatorTab", "Condition:"))
        self.ruleCondLineEdit.setPlaceholderText(
            _translate("SimulatorTab", "not (item1.crc == 0b1010 and item2.length >=3)")
        )
        self.checkBoxPassTranscriptSTDIN.setText(
            _translate("SimulatorTab", "Pass transcript to STDIN")
        )
        self.label_14.setText(_translate("SimulatorTab", "Command:"))
        self.lineEditTriggerCommand.setPlaceholderText(
            _translate(
                "SimulatorTab",
                "Path [+arguments] to external command e.g. mail or sendsms",
            )
        )
        self.btnChooseCommand.setText(_translate("SimulatorTab", "..."))
        self.label_18.setText(
            _translate(
                "SimulatorTab",
                '<html><head/><body><p>You can access the return code of this item in formulas and rules using the item identifier followed by <span style=" font-style:italic;">.rc</span> e.g.<span style=" font-style:italic;"> item5.rc</span>.</p></body></html>',
            )
        )
        self.label_13.setText(_translate("SimulatorTab", "Sleep for:"))
        self.doubleSpinBoxSleep.setSuffix(_translate("SimulatorTab", "s"))
        self.label_15.setText(_translate("SimulatorTab", "Start:"))
        self.label_16.setText(_translate("SimulatorTab", "Step:"))
        self.label_17.setText(
            _translate(
                "SimulatorTab",
                '<html><head/><body><p>This counter will increase by <span style=" font-weight:600;">step</span> each time it gets hit during simulation. It will preserve it\'s value during simulation repeats and retries. To reset all counters stop the simulation and start it again.</p><p>Access the value of this counter using item&lt;Number&gt;.counter_value in <span style=" font-weight:600;">Formulas</span> or as parameter in <span style=" font-weight:600;">external programs</span> e.g. <span style=" font-style:italic;">external_py -c item5.counter_value</span>. The value of this counter will be inserted during simulation time.</p></body></html>',
            )
        )


from urh.ui.ExpressionLineEdit import ExpressionLineEdit
from urh.ui.views.GeneratorTreeView import GeneratorTreeView
from urh.ui.views.ParticipantTableView import ParticipantTableView
from urh.ui.views.SimulatorGraphicsView import SimulatorGraphicsView
from urh.ui.views.SimulatorLabelTableView import SimulatorLabelTableView
from urh.ui.views.SimulatorMessageTableView import SimulatorMessageTableView
from . import urh_rc
