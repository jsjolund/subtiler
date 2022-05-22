# Simple svg viewer which updates image after the file changes

import sys, os
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from PyQt5.QtCore import QRectF, QFileSystemWatcher
from PyQt5.QtGui import QPainter

svg_file = sys.argv[1]

class SvgWidget(QSvgWidget):

    def __init__(self, *args):
        QSvgWidget.__init__(self, *args)

    def paintEvent(self, event):
        renderer = self.renderer()
        if renderer != None:
            painter = QPainter(self)
            size = renderer.defaultSize()
            ratio = size.height()/size.width()
            length = min(self.width(), self.height())
            renderer.render(painter, QRectF(0, 0, length, ratio * length))
            painter.end()


@QtCore.pyqtSlot(str)
def file_changed(path):
    if os.path.getsize(svg_file) > 0:
        svg_widget.load(svg_file)


app = QApplication([])

svg_widget = SvgWidget()
svg_widget.load(svg_file)
svg_widget.setGeometry(50, 50, 800, 600)
svg_widget.show()

watcher = QFileSystemWatcher()
watcher.addPath(svg_file)
watcher.fileChanged.connect(file_changed)

sys.exit(app.exec_())
