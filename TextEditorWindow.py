from PyQt5.QtCore import Qt

from TextEditor import Ui_TextEditor
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox, QFontDialog, QColorDialog
from PyQt5.QtPrintSupport import QPrinter


class EditorWindow(QMainWindow, Ui_TextEditor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Text Editor")
        self.setGeometry(100, 100, 800, 600)
        self.actionYeni.triggered.connect(self.new_file)
        self.actionA.triggered.connect(self.open_file)
        self.actionKaydet.triggered.connect(self.save_file)
        self.actionFarkl_Kaydet.triggered.connect(self.save_as_file)
        self.actionPDF_D_a_AKtar.triggered.connect(self.export_to_pdf)
        self.action_k.triggered.connect(self.close)
        self.actionKopyala.triggered.connect(self.copy)
        self.actionKes.triggered.connect(self.cut)
        self.actionYap_t_r.triggered.connect(self.paste)
        self.actionGeri_AL.triggered.connect(self.undo)
        self.action_leri_Sar.triggered.connect(self.redo)
        self.actionFont.triggered.connect(self.change_font)
        self.actionColor.triggered.connect(self.change_color)
        self.actionKal_n.triggered.connect(self.bold)
        self.action_talik.triggered.connect(self.italic)
        self.actionAlt_izili.triggered.connect(self.underline)
        self.actionSola_Yasla.triggered.connect(self.align_left)
        self.actionOrtala.triggered.connect(self.align_center)
        self.actionSa_a_Yasla.triggered.connect(self.align_right)
        self.action_ki_Yana_Yasl.triggered.connect(self.align_left)

    def new_file(self):
        self.textEdit.clear()

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Aç", "C:/Users/bugra/OneDrive/Masaüstü", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, 'r') as file:
                self.textEdit.setPlainText(file.read())

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Kaydet", "C:/Users/bugra/OneDrive/Masaüstü", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.textEdit.toPlainText())

    def save_as_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Farklı Kaydet", "C:/Users/bugra/OneDrive/Masaüstü", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.textEdit.toPlainText())

    def export_to_pdf(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "PFD olarak dışa aktar", "", "PDF Files (*.pdf);;All Files (*)")
        if file_name:
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(file_name)
            self.textEdit.document().print_(printer)
            QMessageBox.information(self, "Başarılı", "PDF başarıyla dışa aktarıldı.")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Uyarı', 'Dosyayı kaydetmek ister misiniz?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.save_file()
            event.accept()
        elif reply == QMessageBox.No:
            event.accept()
        else:
            event.ignore()

    def copy(self):
        self.textEdit.copy()

    def cut(self):
        self.textEdit.cut()

    def paste(self):
        self.textEdit.paste()

    def undo(self):
        self.textEdit.undo()

    def redo(self):
        self.textEdit.redo()

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def change_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.textEdit.setTextColor(color)

    def bold(self):
        font = self.textEdit.font()
        font.setBold(not font.bold())
        self.textEdit.setFont(font)

    def italic(self):
        font = self.textEdit.font()
        font.setItalic(not font.italic())
        self.textEdit.setFont(font)

    def underline(self):
        font = self.textEdit.font()
        font.setUnderline(not font.underline())
        self.textEdit.setFont(font)

    def align_left(self):
        self.textEdit.setAlignment(Qt.AlignLeft)

    def align_center(self):
        self.textEdit.setAlignment(Qt.AlignCenter)

    def align_right(self):
        self.textEdit.setAlignment(Qt.AlignRight)

    def align_justify(self):
        self.textEdit.setAlignment(Qt.AlignJustify)
