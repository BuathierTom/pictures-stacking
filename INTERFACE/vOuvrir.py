from os import remove
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QFileDialog, QLineEdit, QLabel
from PyQt6.QtCore import pyqtSignal
from os.path import dirname

class vOuvrir(QWidget):
    
    def  __init__(self):
        super().__init__()
        
        self.setWindowTitle('SAE C2') 
        self.chemins = []
        #----------------- LAYOUTS -----------------
        self.topLayout : QVBoxLayout = QVBoxLayout() ; self.setLayout(self.topLayout)
        self.sousTopLayout : QHBoxLayout = QHBoxLayout()
        self.menuLayout : QHBoxLayout = QHBoxLayout()
        #----------------- CONTAINERS -----------------
        self.cMenuLayout : QWidget = QWidget() ; self.cMenuLayout.setLayout(self.menuLayout)
        self.cSousTopLayout : QWidget = QWidget() ; self.cSousTopLayout.setLayout(self.sousTopLayout)
        #----------------- PLACEMENT PHASE 0 -----------------
        self.topLayout.addWidget(self.cMenuLayout)
        self.topLayout.addWidget(self.cSousTopLayout)
        #----------------- LES BOUTONS -----------------
        self.labelOuvrir : QLabel = QLabel("Selectionner vos photos")
        self.ouvrirPhotos : QPushButton = QPushButton("Ouvrir les photos")
        
        #----------------- PLACEMENT PHASE 1 -----------------
        self.menuLayout.addWidget(self.labelOuvrir)
        self.sousTopLayout.addWidget(self.ouvrirPhotos)
        #----------------- VOILA -----------------
        self.show() #INDISPENSABLE
        #----------------- CALLBACK -----------------
        self.ouvrirPhotos.clicked.connect(self.cbOuvrir)
        
        
    def cbOuvrir(self):
        self.path = QFileDialog.getOpenFileNames( self, "Ouvrir", dirname( __file__ ), "Fichier FITS ( *.fits )" )
        self.chemins.append(self.path)
        print(self.path)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w0 : vOuvrir = vOuvrir()
    sys.exit(app.exec()) 