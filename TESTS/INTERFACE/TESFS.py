from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QApplication, QFileDialog, QLineEdit, QLabel

class TESFS(QWidget):
    
    def  __init__(self):
        super().__init__()
        
        self.topLayout : QHBoxLayout = QHBoxLayout() ; self.setLayout(self.topLayout)
        
        self.boutonMoyLayout : QVBoxLayout = QVBoxLayout()
        self.boutonMedLayout : QVBoxLayout = QVBoxLayout()
        self.boutonOutLayout : QVBoxLayout = QVBoxLayout()
        
        
        self.cboutonMoyLayout : QWidget = QWidget() ; self.cboutonMoyLayout.setLayout(self.boutonMoyLayout)
        self.cboutonMedLayout : QWidget = QWidget() ; self.cboutonMedLayout.setLayout(self.boutonMedLayout)
        self.cboutonOutLayout : QWidget = QWidget() ; self.cboutonOutLayout.setLayout(self.boutonOutLayout)
        
        
        self.topLayout.addWidget(self.cboutonMoyLayout)
        self.topLayout.addWidget(self.cboutonMedLayout)
        self.topLayout.addWidget(self.cboutonOutLayout)
        
        
        
        self.boutonMoy : QPushButton = QPushButton("Empilement par moyenne")
        self.boutonSaveMoy : QPushButton = QPushButton("Sauvegarder l'image")         
        self.boutonMed : QPushButton = QPushButton("Empilement par médiane")
        self.boutonSaveMed : QPushButton = QPushButton("✨Sauvegarder l'image✨")         
        self.boutonOutliers : QPushButton = QPushButton("Empilement par rejet des outliers")  
        self.boutonSaveOut : QPushButton = QPushButton("✨Sauvegarder l'image✨")      
        
        self.boutonMoyLayout.addWidget(self.boutonMoy)
        self.boutonMoyLayout.addWidget(self.boutonSaveMoy)
        
        self.boutonMedLayout.addWidget(self.boutonMed)
        self.boutonMedLayout.addWidget(self.boutonSaveMed)
        
        self.boutonOutLayout.addWidget(self.boutonOutliers)
        self.boutonOutLayout.addWidget(self.boutonSaveOut)        
        

        self.show()
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w0 : TESFS = TESFS()
    sys.exit(app.exec()) 