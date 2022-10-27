from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QFileDialog, QLineEdit
from PyQt6.QtCore import pyqtSignal

class VuePersonne(QWidget):
    
    def  __init__(self):
        
        super().__init__()
        self.setWindowTitle('SAE C2') 
        #----------------- LAYOUT -----------------
        self.topLayout : QVBoxLayout = QVBoxLayout() ; self.setLayout(self.topLayout)
        
        self.sousTopLayout : QHBoxLayout = QHBoxLayout()
        self.menuLayout : QHBoxLayout = QHBoxLayout()
        # -------------- Container ---------------------------
        self.cMenuLayout : QWidget = QWidget() ; self.cMenuLayout.setLayout(self.menuLayout)
        self.cSousTopLayout : QWidget = QWidget() ; self.cSousTopLayout.setLayout(self.sousTopLayout)
        # ------------- Placement phase 0 -----------------------
        self.topLayout.addWidget(self.cMenuLayout)
        self.topLayout.addWidget(self.cSousTopLayout)
        #----------------- LES BOUTONS -----------------
        self.prenom : QLineEdit = QLineEdit("Ouvrir les photos")
        self.nom : QLineEdit = QLineEdit("")
        
        
        
        
        
        
        #----------------- Voila -----------------
        self.show() #INDISPENSABLE

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w0 : VuePersonne = VuePersonne()
    sys.exit(app.exec()) 