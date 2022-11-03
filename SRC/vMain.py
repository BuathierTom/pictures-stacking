from os import remove
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QFileDialog, QLineEdit, QLabel
from PyQt6 import QtGui
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
        self.ouvrirPhotoLayout : QHBoxLayout = QHBoxLayout()
        self.afficherPhotoLayout : QHBoxLayout = QHBoxLayout()
        #---
        self.graphLayout : QHBoxLayout = QHBoxLayout()
        self.boutonslayout : QHBoxLayout = QHBoxLayout()
        #----------------- CONTAINERS -----------------
        self.cOuvrirPhotoLayout : QWidget = QWidget() ; self.cOuvrirPhotoLayout.setLayout(self.ouvrirPhotoLayout)
        #---
        self.cAfficherPhotoLayout : QWidget = QWidget() ; self.cAfficherPhotoLayout.setLayout(self.afficherPhotoLayout)
        #---
        self.cGraphLayout : QWidget = QWidget() ; self.cGraphLayout.setLayout(self.graphLayout)
        self.cBoutonslayout : QWidget = QWidget() ; self.cBoutonslayout.setLayout(self.boutonslayout)
        #----------------- PLACEMENT PHASE LAYOUTS -----------------
        self.topLayout.addWidget(self.cOuvrirPhotoLayout)
        #---
        self.topLayout.addWidget(self.cAfficherPhotoLayout)
        #---
        self.topLayout.addWidget(self.cGraphLayout)
        self.topLayout.addWidget(self.cBoutonslayout)
        #----------------- LES BOUTONS -----------------
        self.ouvrirPhotos : QPushButton = QPushButton("Ouvrir les photos 🗂️")
        #---
        self.afficherPhotos : QPushButton = QPushButton("Afficher les images")
        #---
        self.boutonMoy : QPushButton = QPushButton("Empilement par moyenne")
        self.boutonMed : QPushButton = QPushButton("Empilement par médiane")
        self.boutonOutliers : QPushButton = QPushButton("Empilement par rejet des outliers")            
        #----------------- PLACEMENT PHASE BOUTONS -----------------
        self.ouvrirPhotoLayout.addWidget(self.ouvrirPhotos)
        #---
        self.afficherPhotoLayout.addWidget(self.afficherPhotos)
        #---
        self.boutonslayout.addWidget(self.boutonMoy)
        self.boutonslayout.addWidget(self.boutonMed)
        self.boutonslayout.addWidget(self.boutonOutliers)
        #----------------- VOILA -----------------
        self.show() #INDISPENSABLE
        #----------------- CALLBACK -----------------
        self.ouvrirPhotos.clicked.connect(self.cbOuvrir)
        #---
        self.afficherPhotos.clicked.connect(self.cbAfficher)
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
    
    def cbOutliers(self):
        print("-- TQT FRR CA MARCHE --")
        
        
    def cbOuvrir(self):
        self.path = QFileDialog.getOpenFileNames( self, "Ouvrir", dirname( __file__ ), "Fichier FITS ( *.fits )" )
        self.chemins.append(self.path)
        
        print(self.chemins)
        print(self.path)
        
    def cbAfficher(self):
        print("FERME TA GUEULE")
        
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w0 : vMain = vMain()
    sys.exit(app.exec()) 