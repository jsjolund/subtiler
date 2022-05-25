# Simple svg viewer which updates image after the file changes

import sys
import os
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from PyQt5.QtCore import QRectF, QFileSystemWatcher
from PyQt5.QtGui import QPainter, QColorConstants

svg_file = sys.argv[1]


class SvgWidget(QSvgWidget):

    def __init__(self, *args):
        QSvgWidget.__init__(self, *args)
        self.setStyleSheet("background-color: white;")

    def paintEvent(self, event):
        renderer = self.renderer()
        if renderer != None:
            painter = QPainter(self)
            # Preserve svg aspect ratio while maximizing size
            svg_size = renderer.defaultSize()
            ratio = svg_size.height()/svg_size.width()
            length = min(self.width(), self.height())
            length += max(0, self.width() - length)
            length += min(0, self.height()/ratio - length)
            svg_rect = QRectF(0, 0, length, ratio*length)
            renderer.render(painter, svg_rect)
            # Paint over geometry outsize svg boundary
            svg_below = QRectF(0, svg_rect.bottom(), self.width(), self.height() - svg_rect.bottom())
            svg_right = QRectF(svg_rect.right(), 0, self.width() - svg_rect.right(), svg_rect.bottom())
            painter.fillRect(svg_below, QColorConstants.Black)
            painter.fillRect(svg_right, QColorConstants.Black)
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
