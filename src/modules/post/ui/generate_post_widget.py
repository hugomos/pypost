import os, sys

from PyQt5.QtWidgets import QDialog
from .generate_post_form_two import Ui_GeneratePostDialog

CSS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'dark.qss'))

class GeneratePostWidget(QDialog, Ui_GeneratePostDialog):
    def __init__(self):
        QDialog.__init__(self)

        with open(CSS_PATH, 'r') as f:
            self.setStyleSheet(f.read())
            f.close()

        self.setupUi(self)
