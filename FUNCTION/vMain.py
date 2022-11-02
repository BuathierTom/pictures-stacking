from os import remove
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QFileDialog, QLineEdit, QLabel
from PyQt6.QtCore import pyqtSignal
from os.path import dirname
import main as m

class vMain(QWidget):
    
    def  __init__(self):
        super().__init__()
        
        self.setWindowTitle('SAE C2') 
        self.chemins = []
        #----------------- LAYOUTS -----------------
        self.topLayout : QVBoxLayout = QVBoxLayout() ; self.setLayout(self.topLayout)
        self.sousTopLayout : QHBoxLayout = QHBoxLayout()
        self.menuLayout : QHBoxLayout = QHBoxLayout()
        #---
        self.graphLayout : QHBoxLayout = QHBoxLayout()
        self.boutonlayout : QHBoxLayout = QHBoxLayout()
        #----------------- CONTAINERS -----------------
        self.cMenuLayout : QWidget = QWidget() ; self.cMenuLayout.setLayout(self.menuLayout)
        self.cSousTopLayout : QWidget = QWidget() ; self.cSousTopLayout.setLayout(self.sousTopLayout)
        #---
        self.cGraphLayout : QWidget = QWidget() ; self.cGraphLayout.setLayout(self.graphLayout)
        self.cBoutonlayout : QWidget = QWidget() ; self.cBoutonlayout.setLayout(self.boutonlayout)
        #----------------- PLACEMENT PHASE LAYOUTS -----------------
        self.topLayout.addWidget(self.cMenuLayout)
        self.topLayout.addWidget(self.cSousTopLayout)
        #---
        self.topLayout.addWidget(self.cGraphLayout)
        self.topLayout.addWidget(self.cBoutonlayout)
        #----------------- LES BOUTONS -----------------
        self.labelOuvrir : QLabel = QLabel("Selectionner vos photos (Fermer et reouvrir pour changer de selections de photos)")
        self.ouvrirPhotos : QPushButton = QPushButton("Ouvrir les photos")
        #---
        self.boutonMoy : QPushButton = QPushButton("Empilement par moyenne")
        self.boutonMed : QPushButton = QPushButton("Empilement par médiane")
        self.boutonOutliers : QPushButton = QPushButton("Empilement par rejet des outliers")            
        #----------------- PLACEMENT PHASE BOUTONS -----------------
        self.menuLayout.addWidget(self.labelOuvrir)
        self.sousTopLayout.addWidget(self.ouvrirPhotos)
        #---
        self.boutonlayout.addWidget(self.boutonMoy)
        self.boutonlayout.addWidget(self.boutonMed)
        self.boutonlayout.addWidget(self.boutonOutliers)
        #----------------- VOILA -----------------
        self.show() #INDISPENSABLE
        #----------------- CALLBACK -----------------
        self.ouvrirPhotos.clicked.connect(self.cbOuvrir)
        #---
        self.boutonMoy.clicked.connect(self.cbMoyenne)
        self.boutonMed.clicked.connect(self.cbMediane)
        self.boutonOutliers.clicked.connect(self.cbOutliers)
        
    def cbMoyenne(self):
        for i in range(len(self.chemins)):
            m.moyenne(self.chemins[i][0])
            
    def cbMediane(self):
        for i in range(len(self.chemins)):
            m.median(self.chemins[i][0])
    
    def cbOutliers(self, images: list):
        print("-- TQT FRR CA MARCHE --")
        
        
    def cbOuvrir(self):
        self.path = QFileDialog.getOpenFileNames( self, "Ouvrir", dirname( __file__ ), "Fichier FITS ( *.fits )" )
        self.chemins.append(self.path)
        
        print(self.chemins)
        print(self.path)
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w0 : vMain = vMain()
    sys.exit(app.exec()) 