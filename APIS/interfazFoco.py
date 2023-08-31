import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QDialog, QMessageBox, QSystemTrayIcon, QAction
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve 
from PyQt5 import QtCore, QtWidgets, uic 
from PyQt5.uic import loadUi
from PyQt5.QtGui import QDoubleValidator, QIcon

from foco import Foco
from InteligenciaArtificial import IA2

import ctypes
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class Ventana(QMainWindow):
    def __init__(self):
        super(Ventana, self).__init__()
        self.Inter = uic.loadUi('MainInt.ui', self)
        self.Inter.setWindowTitle('Foco')
        self.Inter.setWindowIcon(QIcon('IconoEsfera.png'))

        self.Valor = False
        '''foco = Foco()
        foco.LuzBlanca(0)
        foco.OnOff(False)'''
        self.Valores()

        #===========================Botones=============================#
        self.Inter.ACControl.triggered.connect(self.FMNControl)
        self.Inter.ACAjustes.triggered.connect(self.FMNAjustes)
            #Conexion#
        self.Inter.BTOnOff.clicked.connect(self.FBTOnOff)
        self.Inter.BTGuardar.clicked.connect(self.FBTGuardar)

        self.Inter.RBBlanco.toggled.connect(self.FRBBlanco)
        self.Inter.RBColores.toggled.connect(self.FRBColor)

        self.Inter.HSColor.valueChanged.connect(self.FHSColor)
        self.Inter.HSSaturacion.valueChanged.connect(self.FHSSSaturacion)
        self.Inter.HSBrillo.valueChanged.connect(self.FHSBrillo)

        self.Inter.TXRojo.cursorPositionChanged.connect(self.FTXRojo)
        self.Inter.TXVerde.cursorPositionChanged.connect(self.FTVerde)
        self.Inter.TXAzul.cursorPositionChanged.connect(self.FTXAzyl)
            #Conexion#
        #===========================Botones=============================#
    
    #=========================================FUNCIONES ==========================================#
    def FMNControl(self):
        print('FMNControl')
        self.Inter.PAGINAS.setCurrentWidget(self.Inter.PGControl)
        self.Actualizar()
    def FMNAjustes(self):
        print('FMNAjustes')
        self.Inter.PAGINAS.setCurrentWidget(self.Inter.PGAjustes)

    def FBTOnOff(self):
        if self.Valor == False:
            foco = Foco()
            foco.OnOff(True)
            self.Valor = True

            self.Inter.RBBlanco.setEnabled(True)
            self.Inter.RBColores.setEnabled(True)

            self.Inter.HSColor.setEnabled(True)
            self.Inter.HSSaturacion.setEnabled(True)
            self.Inter.HSBrillo.setEnabled(True)

            self.Inter.TXRojo.setEnabled(True)
            self.Inter.TXVerde.setEnabled(True)
            self.Inter.TXAzul.setEnabled(True)

            self.Inter.BTOnOff.setStyleSheet("QPushButton{\n"
                                                "background-color: Yellow;\n"
                                                "border-radius:60px;\n"
                                                "color: Black;\n"
                                                "}\n"

                                                "QPushButton:hover{\n"
                                                "background-color: rgb(61,61,61);\n"
                                                "border-radius:60px;\n"
                                                "color: White;\n"
                                                "}\n"

                                                "QPushButton:pressed{\n"
                                                "background-color: rgb(0,0,0);\n"
                                                "border-radius:60px;\n"
                                                "color: White;\n"
                                                "}\n")
        else:
            foco = Foco()
            foco.OnOff(False)
            self.Valor = False

            self.Inter.RBBlanco.setEnabled(False)
            self.Inter.RBColores.setEnabled(False)

            self.Inter.HSColor.setEnabled(False)
            self.Inter.HSSaturacion.setEnabled(False)
            self.Inter.HSBrillo.setEnabled(False)

            self.Inter.TXRojo.setEnabled(False)
            self.Inter.TXVerde.setEnabled(False)
            self.Inter.TXAzul.setEnabled(False)

            self.Inter.BTOnOff.setStyleSheet("QPushButton{\n"
                                                "background-color: Black;\n"
                                                "border-radius:60px;\n"
                                                "color: White;\n"
                                                "}\n"

                                                "QPushButton:hover{\n"
                                                "background-color: rgb(61,61,61);\n"
                                                "border-radius:60px;\n"
                                                "color: White;\n"
                                                "}\n"

                                                "QPushButton:pressed{\n"
                                                "background-color: rgb(0,0,0);\n"
                                                "border-radius:60px;\n"
                                                "color: White;\n"
                                                "}\n")
    def FBTGuardar(self):
        pass

    def FRBBlanco(self):
        foco = Foco()
        foco.LuzBlanca(0)
        self.Inter.BTOnOff.setEnabled(True)

        self.Inter.HSColor.setEnabled(False)
        self.Inter.HSSaturacion.setEnabled(False)
        self.Inter.HSBrillo.setEnabled(True)

        self.Inter.TXRojo.setEnabled(False)
        self.Inter.TXVerde.setEnabled(False)
        self.Inter.TXAzul.setEnabled(False)

        self.Valores2()
    def FRBColor(self):
        foco = Foco()
        foco.LuzBlanca(1)
        self.Inter.BTOnOff.setEnabled(True)

        self.Inter.HSColor.setEnabled(True)
        self.Inter.HSSaturacion.setEnabled(True)
        self.Inter.HSBrillo.setEnabled(True)
        
        self.Inter.TXRojo.setEnabled(True)
        self.Inter.TXVerde.setEnabled(True)
        self.Inter.TXAzul.setEnabled(True)

        self.Valores2()

    def FHSColor(self):
        valor = int(self.Inter.HSColor.value())
        self.Inter.TXColor.setText(str(valor+1))

        H = int((valor) * 360 / 100)
        S = int(int(self.Inter.TXSaturacion.text()) * 255 / 100)
        V = int(int(self.Inter.TXBrillo.text()) * 255 / 100)
        #print(H)

        foco = Foco()
        foco.Color3(H,S,V)
    def FHSSSaturacion(self):
        valor = int(self.Inter.HSSaturacion.value())
        self.Inter.TXSaturacion.setText(str(valor+1))

        H = int(int(self.Inter.TXColor.text()) * 360 / 100)
        S = int((valor) * 255 / 100)
        V = int(int(self.Inter.TXBrillo.text()) * 255 / 100)
        #print(H)

        foco = Foco()
        foco.Color3(H,S,V)
    def FHSBrillo(self):
        valor = int(self.Inter.HSBrillo.value())
        self.Inter.TXBrillo.setText(str(valor+1))

        if self.Inter.RBBlanco.isChecked():
            if valor <= 25:
                valor = 25
                foco = Foco()
                foco.Brillo(valor)
            else:
                valor = valor
                foco = Foco()
                foco.Brillo(valor)
        else:
            H = int(int(self.Inter.TXColor.text()) * 360 / 100)
            S = int(int(self.Inter.TXSaturacion.text()) * 255 / 100)
            V = int((valor) * 255 / 100)
            #print(H)

            foco = Foco()
            foco.Color3(H,S,V)
    def FTXRojo(self):
        if self.Inter.TXRojo.text() == "":
            pass
        else:
            R = int(self.Inter.TXRojo.text())
            G = int(self.Inter.TXVerde.text())
            B = int(self.Inter.TXAzul.text())
            S = int(int(self.Inter.TXSaturacion.text()) * 255 / 100)
            L = int(int(self.Inter.TXBrillo.text()) * 255 / 100)
            IA = Foco()
            IA.Color2(R,G,B,S,L)
    def FTVerde(self):
        if self.Inter.TXVerde.text() == "":
            pass
        else:
            R = int(self.Inter.TXRojo.text())
            G = int(self.Inter.TXVerde.text())
            B = int(self.Inter.TXAzul.text())
            S = int(int(self.Inter.TXSaturacion.text()) * 255 / 100)
            L = int(int(self.Inter.TXBrillo.text()) * 255 / 100)
            IA = Foco()
            IA.Color2(R,G,B,S,L)
    def FTXAzyl(self):
        if self.Inter.TXAzul.text() == "":
            pass
        else:
            R = int(self.Inter.TXRojo.text())
            G = int(self.Inter.TXVerde.text())
            B = int(self.Inter.TXAzul.text())
            S = int(int(self.Inter.TXSaturacion.text()) * 255 / 100)
            L = int(int(self.Inter.TXBrillo.text()) * 255 / 100)
            IA = Foco()
            IA.Color2(R,G,B,S,L)
    #=========================================FUNCIONES ==========================================#

    #=========================================BUSCAR API==========================================#
    def Valores(self):
        Memoria = Foco()
        Lista = Memoria.valores()

        #print(Lista)
        On_Off = Lista[0][1] 
        Modo_Trabajo = Lista[1][1]
        brllo = Lista[2][1]
        Col_Val = Lista[3][1]

        #print(type(Col_Val))

        import ast
        vall = ast.literal_eval(Col_Val)

        color = [vall["h"], vall["s"], vall["v"]]

        #print(On_Off,Modo_Trabajo,brllo,color)

        self.Valor = On_Off
        self.FVisual()

        if Modo_Trabajo == 'colour':
            print(color)
            self.Inter.RBColores.setChecked(True)
            self.Inter.HSBrillo.setValue(int((int(color[2])) * 100 / 255))
            self.Inter.TXBrillo.setText(str((int(self.Inter.HSBrillo.value()))+1))

            self.Inter.HSColor.setValue(int((int(color[0])) * 100 / 360))
            self.Inter.TXColor.setText(str((int(self.Inter.HSColor.value()))+1))
            #self.Inter.HSSaturacion.setEnabled(False)
            self.Inter.HSSaturacion.setValue(int((int(color[1])) * 100 / 255))
            self.Inter.TXSaturacion.setText(str((int(self.Inter.HSSaturacion.value()))+1))
            
        else:
            self.Inter.RBBlanco.setChecked(True)
            self.Inter.HSBrillo.setValue(int(brllo))
            self.Inter.TXBrillo.setText(str((int(self.Inter.HSBrillo.value()))+1))

    def Valores2(self):
        Memoria = Foco()
        Lista = Memoria.valores()

        #print(Lista)
        On_Off = Lista[0][1] 
        Modo_Trabajo = Lista[1][1]
        brllo = Lista[2][1]
        Col_Val = Lista[3][1]

        #print(type(Col_Val))

        import ast
        vall = ast.literal_eval(Col_Val)

        color = [vall["h"], vall["s"], vall["v"]]

        #print(On_Off,Modo_Trabajo,brllo,color)

        if Modo_Trabajo == 'colour':
            print(color)
            self.Inter.HSBrillo.setValue(int((int(color[2])) * 100 / 255))
            self.Inter.TXBrillo.setText(str((int(self.Inter.HSBrillo.value()))+1))

            self.Inter.HSColor.setValue(int((int(color[0])) * 100 / 360))
            self.Inter.TXColor.setText(str((int(self.Inter.HSColor.value()))+1))
            #self.Inter.HSSaturacion.setEnabled(False)
            self.Inter.HSSaturacion.setValue(int((int(color[1])) * 100 / 255))
            self.Inter.TXSaturacion.setText(str((int(self.Inter.HSSaturacion.value()))+1))
            
        else:
            self.Inter.HSBrillo.setValue(int(brllo))
            self.Inter.TXBrillo.setText(str((int(self.Inter.HSBrillo.value()))+1))

    
    def Actualizar(self):
        '''import time
        while True:
            time.sleep(0.5)
            print("Actualizando")
            self.Valores2()'''
        self.Valores()

    #=========================================BUSCAR API==========================================#

    #=========================================BOTONES DE LA BARRA PRINCIPAL==========================================#
    def FVisual(self):
        if self.Valor == True:
            self.Inter.RBBlanco.setEnabled(True)
            self.Inter.RBColores.setEnabled(True)

            self.Inter.HSColor.setEnabled(True)
            self.Inter.HSSaturacion.setEnabled(True)
            self.Inter.HSBrillo.setEnabled(True)

            self.Inter.TXRojo.setEnabled(True)
            self.Inter.TXVerde.setEnabled(True)
            self.Inter.TXAzul.setEnabled(True)

            self.Inter.BTOnOff.setStyleSheet("QPushButton{\n"
                                                "background-color: Yellow;\n"
                                                "border-radius:60px;\n"
                                                "color: Black;\n"
                                                "}\n"

                                                "QPushButton:hover{\n"
                                                "background-color: rgb(61,61,61);\n"
                                                "border-radius:60px;\n"
                                                "color: White;\n"
                                                "}\n"

                                                "QPushButton:pressed{\n"
                                                "background-color: rgb(0,0,0);\n"
                                                "border-radius:60px;\n"
                                                "color: White;\n"
                                                "}\n")
        else:
            self.Inter.RBBlanco.setEnabled(False)
            self.Inter.RBColores.setEnabled(False)

            self.Inter.HSColor.setEnabled(False)
            self.Inter.HSSaturacion.setEnabled(False)
            self.Inter.HSBrillo.setEnabled(False)

            self.Inter.TXRojo.setEnabled(False)
            self.Inter.TXVerde.setEnabled(False)
            self.Inter.TXAzul.setEnabled(False)

            self.Inter.BTOnOff.setStyleSheet("QPushButton{\n"
                                                "background-color: Black;\n"
                                                "border-radius:60px;\n"
                                                "color: White;\n"
                                                "}\n"

                                                "QPushButton:hover{\n"
                                                "background-color: rgb(61,61,61);\n"
                                                "border-radius:60px;\n"
                                                "color: White;\n"
                                                "}\n"

                                                "QPushButton:pressed{\n"
                                                "background-color: rgb(0,0,0);\n"
                                                "border-radius:60px;\n"
                                                "color: White;\n"
                                                "}\n")
    #=========================================BOTONES DE LA BARRA PRINCIPAL==========================================#


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = Ventana()
    myApp.show()
    sys.exit(app.exec_())




