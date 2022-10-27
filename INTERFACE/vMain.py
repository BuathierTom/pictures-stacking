from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QFileDialog, QLineEdit, QLabel
from PyQt6.QtCore import pyqtSignal
import vOuvrir
import vGraph

class vMain(QWidget):
    
    def  __init__(self):
        super().__init__()
        self.setWindowTitle('SAE C2') 
        #----------------- LAYOUTS -----------------
        self.topLayout : QVBoxLayout = QVBoxLayout() ; self.setLayout(self.topLayout)
        self.sousTopLayout : QHBoxLayout = QHBoxLayout()
        self.selectionLayout : QHBoxLayout = QHBoxLayout()
        
        self.vuOuvrir : vOuvrir.vOuvrir = vOuvrir.vOuvrir() 
        self.vueGr : vGraph.vGraph = vGraph.vGraph() 
        
        #----------------- CONTAINERS -----------------
        self.cSelection : QWidget = QWidget() ; self.cSelection.setLayout(self.selectionLayout)
        self.cSousTopLayout : QWidget = QWidget() ; self.cSousTopLayout.setLayout(self.sousTopLayout)
        #----------------- PLACEMENT PHASE 0 -----------------
        self.selectionLayout.addWidget(self.vuOuvrir)
        self.sousTopLayout.addWidget(self.vueGr)
        self.topLayout.addWidget(self.cSelection)
        self.topLayout.addWidget(self.cSousTopLayout)
        
        self.show()
            
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w0: vMain = vMain()
    sys.exit(app.exec()) 