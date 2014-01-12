
import sys
from PyQt4 import QtGui
#from myuiwindow import myuiwindow

from UiGenerated import Ui_MainWindow
from drawGraph import DrawGraph
from AutomataProssesing import doAutomata

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.mySetupUI()
        
        
        
        
    
    def mySetupUI(self):
        self.genesGraphImageLabel.setScaledContents(True)
        self.statesGraphImageLabel.setScaledContents(True)
        self.simplifiedStatesGraphImageLabel.setScaledContents(True)
        
        
        maxNK=10
        minNK=1
        defaultNK=5
        self.nSlider.setMaximum(maxNK)
        self.kSlider.setMaximum(maxNK)
        self.nSlider.setMinimum(minNK)
        self.kSlider.setMinimum(minNK)
        self.nSlider.setValue(defaultNK)
        self.kSlider.setValue(defaultNK)
        
        self.nLabel.setText("N="+str(defaultNK))
        self.kLabel.setText("K="+str(defaultNK))
        
        
          
        
        self.goButton.clicked.connect(self.buttonSlotProceture)
        
        self.nSlider.valueChanged.connect(self.nSliderSlotProcedure)
        self.kSlider.valueChanged.connect(self.kSliderSlotProcedure)
        
        self.drawGraphObject=DrawGraph(self)
        self.drawGraphObject.valueUpdated.connect(self.handleValueUpdated)
        
        self.progressBar.setValue(0)
        self.progressBar.setMaximum(100)
        

    def nSliderSlotProcedure(self):
        self.nLabel.setText("N="+str(self.nSlider.value()))
        if self.nSlider.value() < self.kSlider.value():
            self.kSlider.setValue(self.nSlider.value())
            
            
        
    def kSliderSlotProcedure(self):
        self.kLabel.setText("K="+str(self.kSlider.value()))
        if self.kSlider.value() > self.nSlider.value():
            self.nSlider.setValue(self.kSlider.value())
        
    def buttonSlotProceture(self):
        
        N=self.nSlider.value()
        K=self.kSlider.value()
        doAutomata(N, K, self.drawGraphObject)
        self.genesGraphImageLabel.setPixmap(QtGui.QPixmap('/home/sashko/workspaceEclipse/NK_Network/src/mainGUI/tempPic3.png'))
        self.statesGraphImageLabel.setPixmap(QtGui.QPixmap('/home/sashko/workspaceEclipse/NK_Network/src/mainGUI/tempPic.png'))
        self.simplifiedStatesGraphImageLabel.setPixmap(QtGui.QPixmap('/home/sashko/workspaceEclipse/NK_Network/src/mainGUI/tempPic2.png'))

    def handleValueUpdated(self, value):
        self.progressBar.setValue(value)
        QtGui.qApp.processEvents()



def main():
    """
    app = QtGui.QApplication(sys.argv)
    qb = myuiwindow()
    qb.show()
    sys.exit(app.exec_())
    """
    
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
   

if __name__ == '__main__':
    main() 