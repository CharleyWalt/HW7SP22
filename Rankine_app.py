import sys
from PyQt5 import QtWidgets as qtw
from Rankine_GUI import Ui_Form
from Rankine_hw7 import rankine
from Steam import steam

class MainWindow(qtw.QWidget, Ui_Form, rankine):
    def __init__(self):
        """
        MainWindow constructor
        """
        super().__init__()  #if you inherit, you generally should run the parent constructor first.
        # Main UI code goes here
        self.setupUi(self)
        self.btn_Calculate.clicked.connect(self.calculate)
        # End main ui code
        self.show()

    def calculate(self):
        # step 1: read input values and assign to variables to send to rankine
        plow = float(self.le_PLow.text())  # bar
        phigh = float(self.le_PHigh.text())  # bar
        eff_turb = float(self.le_TurbineEff.text())
        if self.rdo_THigh.isChecked():
            thigh = float(self.le_TurbineInletCondition.text())
            R1 = rankine(p_high=100*phigh, p_low=100*plow, t_high=500, turb_eff=eff_turb)
        else:
            quality = float(self.le_TurbineInletCondition.text())
            R1 = rankine(p_high=phigh, p_low=plow, x=quality, turb_eff=eff_turb)

        # step 2: run rankine, sending it the newly named input values
        effcalc = R1.calc_efficiency()
        h1 = self.state1.h
        print(h1)

        # step 3: output values to text labels
            # example for how to print text to the labels
            # self.le_H1.setText(self.h1)  # must update to actual h1 value from Rankine

        pass


#if this module is being imported, this won't run. If it is the main module, it will run.
if __name__== '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.setWindowTitle('Hello QT')
    sys.exit(app.exec())