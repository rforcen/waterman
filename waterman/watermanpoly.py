'''
developed w/python 3.6
ui/openGL widget based on PyQt5
precalc coords

coded by: robertoforcen@gmail.com
'''
import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.uic import loadUi

from watermanCoords import watermanCoords


class WatermanPoly:
    n = None
    coords = faces = None

    def __init__(self, n):
        self.n = n
        if n in watermanCoords:
            self.coords, self.faces = watermanCoords[n]


class Main(QMainWindow):
    def __init__(self, *args):
        super(Main, self).__init__(*args)
        loadUi('waterman.ui', self)
        self.nSlider.setValue(14)

    # slots
    def onSliderChanged(self, n):  # root #
        self.waterman.setWP(WatermanPoly(n))
        self.setWindowTitle('Waterman polyhedra %d' % n)
        self.statusBar().showMessage(
            '[coords:%d, faces:%d, max points in face:%d]' % (
                len(self.waterman.wp.coords), len(self.waterman.wp.faces),
                max([len(l) for l in self.waterman.wp.faces])))

    def onShuffle(self):
        self.waterman.randColors()

    def onColorMode(self, cm):
        self.waterman.setColorMode(cm)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = Main()
    mw.show()

    sys.exit(app.exec_())
