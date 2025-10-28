from PyQt5.QtWidgets import QMessageBox


class UI_Controller:
    def __init__(self) :
        self._msg_box = QMessageBox()

    def show_box_error (self, msg: str):
        self._msg_box.setIcon(QMessageBox.Critical)
        self._msg_box.setText(msg)
        self._msg_box.setWindowTitle("Error")
        self._msg_box.setStandardButtons(QMessageBox.Ok)
        self._msg_box.exec_()

    def show_box_success(self, msg: str):
        self._msg_box.setIcon(QMessageBox.Information)
        self._msg_box.setText(msg)
        self._msg_box.setWindowTitle("Success")
        self._msg_box.setStandardButtons(QMessageBox.Ok)
        self._msg_box.exec_()

    def show_box_info(self, msg: str):
        self._msg_box.setIcon(QMessageBox.Warning)
        self._msg_box.setText(msg)
        self._msg_box.setWindowTitle("Warning")
        self._msg_box.setStandardButtons(QMessageBox.Ok)
        self._msg_box.exec_()
