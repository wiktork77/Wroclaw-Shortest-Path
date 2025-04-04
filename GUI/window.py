# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QCompleter

from algorithms import dijkstra, astar
from cost_computations import heuristics
from data_processing import data_presentation
from data_processing import data_utilities
import datetime



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 735)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setCentralWidget(self.centralwidget)

        self.setupDepartureUi()
        self.setupArrivalUi()
        self.setupDepartureTimeUi()
        self.setupAlgorithmChooseUi()
        self.setupPathBuildingCriteriaUi()
        self.setupSearchButton()
        self.setupResultUi()

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.departureLabel.setText(_translate("MainWindow", "Departure stop"))
        self.departureErrorLabel.setText(_translate("MainWindow", "Please fill with existing stop"))
        self.arrivalLabel.setText(_translate("MainWindow", "Arrival stop"))
        self.arrivalErrorLabel.setText(_translate("MainWindow", "Please fill with existing stop"))
        self.timeSeparatorLabel.setText(_translate("MainWindow", ":"))
        self.departureTimeLabel.setText(_translate("MainWindow", "Departure time"))
        self.algorithmLabel.setText(_translate("MainWindow", "Algorithm"))
        self.dijkstraRadioButton.setText(_translate("MainWindow", "Dijkstra"))
        self.aStarRadioButton.setText(_translate("MainWindow", "A*"))
        self.pathBuildCriteriaLabel.setText(_translate("MainWindow", "Path building criteria"))
        self.transferCountMinimizationRadioButton.setText(_translate("MainWindow", "Transfer count minimization"))
        self.timeMinimizationRadioButton.setText(_translate("MainWindow", "Time minimization"))
        self.searchButton.setText(_translate("MainWindow", "Search"))


    def setupDepartureUi(self):
        self.departureLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.departureLabel.setGeometry(QtCore.QRect(20, 20, 201, 21))
        self.departureLabel.setFont(self.majorLabelFont)
        self.departureLabel.setObjectName("departureLabel")

        self.departureLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.departureLineEdit.setGeometry(QtCore.QRect(20, 50, 211, 31))
        self.departureLineEdit.setObjectName("departureLineEdit")

        self.departureLineEdit.setStyleSheet("border: 0.035em solid black")

        self.departureErrorLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.departureErrorLabel.setGeometry(QtCore.QRect(20, 80, 211, 21))
        self.departureErrorLabel.setFont(self.majorLabelFont)
        self.departureErrorLabel.setObjectName("departureErrorLabel")
        self.departureErrorLabel.setStyleSheet("color: red")
        self.departureErrorLabel.setVisible(False)

        self.departureLineEdit.setCompleter(self.completer)




    def setupArrivalUi(self):
        self.arrivalLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.arrivalLabel.setGeometry(QtCore.QRect(410, 20, 201, 21))

        self.arrivalLabel.setFont(self.majorLabelFont)
        self.arrivalLabel.setObjectName("arrivalLabel")

        self.arrivalLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.arrivalLineEdit.setGeometry(QtCore.QRect(410, 50, 211, 31))
        self.arrivalLineEdit.setObjectName("arrivalLineEdit")

        self.arrivalLineEdit.setStyleSheet("border: 0.035em solid black")

        self.arrivalErrorLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.arrivalErrorLabel.setGeometry(QtCore.QRect(410, 80, 211, 21))
        self.arrivalErrorLabel.setFont(self.majorLabelFont)
        self.arrivalErrorLabel.setObjectName("arrivalErrorLabel")
        self.arrivalErrorLabel.setStyleSheet("color: red")
        self.arrivalErrorLabel.setVisible(False)

        self.arrivalLineEdit.setCompleter(self.completer)

    def setupDepartureTimeUi(self):
        self.departureTimeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.departureTimeLabel.setGeometry(QtCore.QRect(20, 110, 201, 21))
        self.departureTimeLabel.setFont(self.minorLabelFont)
        self.departureTimeLabel.setObjectName("departureTimeLabel")

        self.timeSeparatorLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.timeSeparatorLabel.setGeometry(QtCore.QRect(115, 145, 20, 21))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)

        self.timeSeparatorLabel.setFont(font)
        self.timeSeparatorLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.timeSeparatorLabel.setObjectName("timeSeparatorLabel")

        self.hourSpinBox = TimeSpinbox(minVal=0, maxVal=23, parent=self.centralwidget)
        self.hourSpinBox.setGeometry(QtCore.QRect(20, 140, 81, 31))
        self.hourSpinBox.setFont(self.majorLabelFont)
        self.hourSpinBox.setObjectName("hourSpinBox")
        self.hourSpinBox.setMinimum(0)
        self.hourSpinBox.setMaximum(23)

        self.minuteSpinBox = TimeSpinbox(minVal=0, maxVal=59, parent=self.centralwidget)
        self.minuteSpinBox.setGeometry(QtCore.QRect(150, 140, 81, 31))
        self.minuteSpinBox.setFont(self.majorLabelFont)
        self.minuteSpinBox.setObjectName("minuteSpinBox")
        self.minuteSpinBox.setMinimum(0)
        self.minuteSpinBox.setMaximum(59)

        time = datetime.datetime.now()

        self.hourSpinBox.setValue(time.hour)
        self.minuteSpinBox.setValue(time.minute)


    def setupAlgorithmChooseUi(self):
        self.algorithmLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.algorithmLabel.setGeometry(QtCore.QRect(410, 110, 201, 21))
        self.algorithmLabel.setFont(self.minorLabelFont)
        self.algorithmLabel.setObjectName("algorithmLabel")

        self.algorithmGroup = QtWidgets.QButtonGroup()

        self.dijkstraRadioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.dijkstraRadioButton.setGeometry(QtCore.QRect(410, 150, 95, 20))
        self.dijkstraRadioButton.setObjectName("dijkstraRadioButton")

        self.aStarRadioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.aStarRadioButton.setGeometry(QtCore.QRect(520, 150, 95, 20))
        self.aStarRadioButton.setObjectName("aStarRadioButton")

        self.algorithmGroup.addButton(self.dijkstraRadioButton)
        self.algorithmGroup.addButton(self.aStarRadioButton)

        self.dijkstraRadioButton.click()

        self.algorithmGroup.buttonClicked.connect(self.onAlgorithmChange)




    def setupPathBuildingCriteriaUi(self):
        self.pathBuildCriteriaLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.pathBuildCriteriaLabel.setGeometry(QtCore.QRect(410, 210, 201, 16))
        self.pathBuildCriteriaLabel.setObjectName("pathBuildCriteriaLabel")

        self.pathBuildCriteriaGroup = QtWidgets.QButtonGroup()

        self.transferCountMinimizationRadioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.transferCountMinimizationRadioButton.setGeometry(QtCore.QRect(410, 290, 211, 20))
        self.transferCountMinimizationRadioButton.setObjectName("transferCountMinimizationRadioButton")

        self.timeMinimizationRadioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.timeMinimizationRadioButton.setGeometry(QtCore.QRect(410, 250, 201, 20))
        self.timeMinimizationRadioButton.setObjectName("timeMinimizationRadioButton")

        self.pathBuildCriteriaGroup.addButton(self.transferCountMinimizationRadioButton)
        self.pathBuildCriteriaGroup.addButton(self.timeMinimizationRadioButton)

        self.timeMinimizationRadioButton.click()

        self.pathBuildCriteriaGroup.buttonClicked.connect(self.onCriteriaChange)


        self.changeVisibilityOfCriteria()


    def setupSearchButton(self):
        self.searchButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(20, 270, 121, 41))
        self.searchButton.setFont(self.majorLabelFont)
        self.searchButton.setObjectName("searchButton")

        self.searchButton.clicked.connect(self.onSearchPressed)

    def setupResultUi(self):
        self.treeView = QtWidgets.QTreeView(parent=self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(20, 340, 601, 341))

        self.treeModel = QtGui.QStandardItemModel()
        self.treeModel.setColumnCount(5)
        self.treeModel.setHorizontalHeaderLabels(["Departure stop", "Departure time", "Arrival stop", "Arrival time", "Line"])

        self.rootNode = self.treeModel.invisibleRootItem()

        self.treeView.setModel(self.treeModel)
        self.treeView.header().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        self.computationTimeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.computationTimeLabel.setGeometry(QtCore.QRect(20, 682, 201, 21))
        self.computationTimeLabel.setFont(self.minorLabelFont)
        self.computationTimeLabel.setObjectName("computationTimeLabel")




    def changeVisibilityOfCriteria(self):
        if self.algorithm == 'Dijkstra' or self.algorithm is None:
            self.pathBuildCriteriaLabel.setEnabled(False)
            self.transferCountMinimizationRadioButton.setEnabled(False)
            self.timeMinimizationRadioButton.setEnabled(False)
        else:
            self.pathBuildCriteriaLabel.setEnabled(True)
            self.transferCountMinimizationRadioButton.setEnabled(True)
            self.timeMinimizationRadioButton.setEnabled(True)

    def onAlgorithmChange(self, radioButton):
        self.algorithm = radioButton.text()
        self.changeVisibilityOfCriteria()

    def onCriteriaChange(self, radioButton):
        criteriaText = radioButton.text()
        if criteriaText == "Time minimization":
            self.criteria = 't'
        else:
            self.criteria = 'p'

    def onSearchPressed(self):
        if self.validateForm():
            print("Invoking the search")
            departure, arrival = self.departureLineEdit.text(), self.arrivalLineEdit.text()
            time = f"{self.hourSpinBox.text()}:{self.minuteSpinBox.text()}"
            if self.algorithm == "Dijkstra":
                result = dijkstra.dsp(self.graph, departure, arrival, time)
            elif self.algorithm == "A*":
                result = astar.astar(self.graph, departure, arrival, time, heuristics.euclidean_distance, self.criteria)
            else:
                result = None
            path, travel_time, computation_time = result

            segmented = data_presentation.segment_path(path)

            # data_presentation.print_path_concise(segmented)
            print(travel_time)
            self.treeModel.removeRows(0, self.treeModel.rowCount())

            for seg in segmented:
                stopNameItem = StandardItem(f'{seg[1].start_stop.name}')
                self.rootNode.appendRow(
                    [
                        stopNameItem,
                        StandardItem(f'{data_presentation.datetime_to_day_time(seg[2].departure_time)}'),
                        StandardItem(f'{seg[1].end_stop.name}'),
                        StandardItem(f'{data_presentation.datetime_to_day_time(seg[2].arrival_time)}'),
                        StandardItem(f'{seg[2].line}')
                    ]
                )

                for stop in seg[3]:
                    stopNameItem.appendRow(
                        [
                            StandardItem(stop[0]),
                            StandardItem(data_presentation.datetime_to_day_time(stop[1])),
                        ]
                    )

            self.rootNode.appendRow(
                [
                    StandardItem(f''),
                    StandardItem(f''),
                    StandardItem(f''),
                    StandardItem(f''),
                    StandardItem(f''),
                ]
            )

            self.rootNode.appendRow(
                [
                    StandardItem(f'Departure:'),
                    StandardItem(f'{data_presentation.datetime_to_day_time(segmented[0][2].departure_time)}', isBold=True),
                    StandardItem(f'Arrival:'),
                    StandardItem(f'{data_presentation.datetime_to_day_time(segmented[-1][2].arrival_time)}', isBold=True),
                    StandardItem(f'{data_utilities.convert_minutes_to_hourminute(int(travel_time))}', isBold=True),
                ]
            )
            computation_time = computation_time*1000
            computation_time = float(str(computation_time)[:4])
            self.computationTimeLabel.setText(f"Computation time: {computation_time}ms")

    def validateDeparture(self):
        isValid = True
        if self.departureLineEdit.text() not in self.stops:
            isValid = False
        self.setValidityStyle(self.departureLineEdit, self.departureErrorLabel, isValid)
        return isValid

    def validateArrival(self):
        isValid = True
        if self.arrivalLineEdit.text() not in self.stops:
            isValid = False
        self.setValidityStyle(self.arrivalLineEdit, self.arrivalErrorLabel, isValid)
        return isValid

    def setValidityStyle(self, input, errorLabel, isValid):
        if isValid:
            input.setStyleSheet("border: 0.035em solid black")
            errorLabel.setVisible(False)
        else:
            input.setStyleSheet("border: 0.035em solid red")
            errorLabel.setVisible(True)

    def validateForm(self):
        isValid = True

        validators = [
            self.validateDeparture,
            self.validateArrival,
        ]

        for validator in validators:
            if not validator():
                isValid = False
        return isValid

    def __init__(self, graph):
        self.graph = graph
        self.stops = graph.get_vertices_names()

        self.completer = QCompleter(sorted(self.stops, key=str.casefold))
        self.completer.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)

        self.majorLabelFont = QtGui.QFont()
        self.majorLabelFont.setPointSize(10)

        self.minorLabelFont = QtGui.QFont()
        self.minorLabelFont.setPointSize(9)

        self.algorithm = "Dijkstra"
        self.criteria = "t"


class TimeSpinbox(QtWidgets.QSpinBox):
    def __init__(self, minVal, maxVal, parent):
        QtWidgets.QSpinBox.__init__(self, parent=parent)

        self.setRange(minVal, maxVal)

    def textFromValue(self, v: int) -> str:
        return "%02d" % v


class StandardItem(QtGui.QStandardItem):
    def __init__(self, txt='', isBold=False):
        super().__init__()
        self.setText(txt)
        font = QtGui.QFont()
        font.setBold(isBold)
        self.setFont(font)