import sys
from PyQt5.QtWidgets import QApplication
from nuteCalc import nuteCalcWindow

app = QApplication(sys.argv)  # Create app obj

calculator = nuteCalcWindow()

sys.exit(app.exec_())

