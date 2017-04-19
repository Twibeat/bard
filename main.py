
import sys
from PyQt5.QtWidgets import QApplication
from multiBardGUI5 import MainDialog

app = QApplication(sys.argv)
dialog = MainDialog()
dialog.show()
app.exec_()