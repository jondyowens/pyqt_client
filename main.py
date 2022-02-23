from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QFormLayout
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import Qt
import sys, platform
import ctypes, ctypes.util





class lineEditDemo(QWidget):
        

        def __init__(self,parent=None):
                super().__init__(parent)
                self.e1 = QLabel()
                


        def setText(self, text):
                self.e1.setText(text)
        def textchanged(self,text):
                print("Changed: " + text)

        def enterPress(self):
                print("Enter pressed")

if __name__ == "__main__":

        if platform.system() == "Windows":
                path_lib = ctypes.util.find_library("./licensing_api")

        print (path_lib)

        if not path_lib:
                print("Unable to find library")
                sys.exit()

        try:
                licensing_lib = ctypes.cdll.LoadLibrary(path_lib)
                licensing_lib.generate_hardware_hash.restype = ctypes.c_wchar_p
                text = licensing_lib.generate_hardware_hash()
                licensing_lib.checkout_key.restype = ctypes.c_char_p
                licensing_lib.checkout_key.argtypes = [ctypes.c_wchar_p]
                checkout_return = licensing_lib.checkout_key(text)
                print(checkout_return)
                app = QApplication(sys.argv)
                win = lineEditDemo()
                win.setWindowTitle(text)
                win.show()
                sys.exit(app.exec_())

        except OSError as error:
                print(error)
                sys.exit()

