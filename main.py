#UI
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, uic

from unidecode import unidecode
import re
import math
#class for opening screen
qtCreatorFile = "kryptoUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

Abeceda=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5',
'6','7','8','9')
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # return string  
    return (str1.join(s))
class ZlaHodnota(Exception):
    pass

class MyApp(QMainWindow, Ui_MainWindow):


    
    def encrypt(self):
        
        SifrovanePole=[]
        a=int(self.plainTextEdit_A.toPlainText())
        b=int(self.plainTextEdit_B.toPlainText())

        vstup=str(self.plainTextEdit_Input.toPlainText())
        vstup=vstup.replace("§","")
        vstup=unidecode(vstup)
        for k in vstup.split("\n"):
            vstup=(re.sub(r"[^a-zA-Z0-9]+", ' ', k))
        if vstup==' ':
            vstup=vstup.replace(' ','')
        
        vstup=vstup.replace(' ',"XmezeraX")
                
        vstup=vstup.upper()
        try:
            if math.gcd(a,36)!=1 or a==None or b==None or vstup=="":
                raise ZlaHodnota
        except ZlaHodnota:
            self.labelVysledek.setText("Zadali ste neplatnú hodnotu")
            raise
        
        
        for i in range(0,len(vstup)):
            for j in range(0,len(Abeceda)):
                if vstup[i]==Abeceda[j]:
                    hodnota=(a*(j)+b)%36
                    SifrovanePole.append(Abeceda[hodnota])
        SifrovanePole=listToString(SifrovanePole)
        SifrovanePole=' '.join([SifrovanePole[i:i+5] for i in range(0, len(SifrovanePole), 5)])                    
        self.labelVysledek.setText(SifrovanePole)
        
    def decrypt(self):         
        DesifrovanePole=[]
        a=int(self.plainTextEdit_A.toPlainText())
        b=int(self.plainTextEdit_B.toPlainText())

        vstup=str(self.plainTextEdit_Input.toPlainText())
        vstup=vstup.upper()
        vstup=unidecode(vstup)

        try:
            if math.gcd(a,36)!=1:
                raise ZlaHodnota
        except ZlaHodnota:
            self.labelVysledek.setText("Zadali ste neplatnú hodnotu A!")
            raise

        vstup=vstup.replace(" ","")


        x=pow(a,-1, 36)
        for i in range(0,len(vstup)):
                for j in range(0,len(Abeceda)):
                    if vstup[i]==Abeceda[j]:
                        hodnota=(((j-b)*x)%36)
                        DesifrovanePole.append(Abeceda[hodnota])
        DesifrovanePole=listToString(DesifrovanePole)
        DesifrovanePole=DesifrovanePole.replace("XMEZERAX",' ')
        self.labelVysledek.setText(DesifrovanePole)
    
    def execute(self):
        if self.CheckBox_Desifrovat.isChecked():
            self.decrypt()
        elif self.CheckBox_Sifrovat.isChecked():
            self.encrypt()
        else:
            self.labelVysledek.setText("Vyberte možnosť sifrovat alebo desifrovat!")

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Button_Execute.clicked.connect(self.execute)



    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

















