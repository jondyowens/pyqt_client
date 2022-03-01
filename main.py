from PyQt5.QtWidgets import QApplication,QTextEdit,QWidget,QVBoxLayout
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import Qt
import sys, platform
import ctypes, ctypes.util





class lineEditDemo(QWidget):
        

        def __init__(self,parent=None):
                super().__init__(parent)
                self.e1 = QTextEdit(parent)
                self.setLayout(QVBoxLayout(parent))
                self.layout().addWidget(self.e1)
                


        def appendText(self, text):
                self.e1.append(text)
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

                app = QApplication(sys.argv)
                win = lineEditDemo()
                win.setWindowTitle("Python Client")
                win.show()
                win.appendText("Loading C DLL...\n")
                licensing_lib = ctypes.cdll.LoadLibrary(path_lib)
                win.appendText("C DLL loaded successfully.\n")
                licensing_lib.generate_hardware_hash.restype = ctypes.c_wchar_p
                win.appendText("Generating hardware hash using C DLL...\n")
                text = licensing_lib.generate_hardware_hash()
                win.appendText("Hardware hash generated from C DLL: " + text + "\n")
                
                licensing_lib.checkout_key.restype = ctypes.c_char_p
                licensing_lib.checkout_key.argtypes = [ctypes.c_wchar_p]
                win.appendText("Calling checkout_key() from C DLL...\n")
                checkout_return = licensing_lib.checkout_key(text)
                win.appendText("checkout_key() returned: " + str(checkout_return) + "\n")
                sys.exit(app.exec_())

        except OSError as error:
                print(error)
                sys.exit()

