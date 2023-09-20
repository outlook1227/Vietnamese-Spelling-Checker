import sys
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

"Input the latin alphabet for the Vietnamese Word"

# Vietnamese alphabet
alphabet = {"^[ _abcdefghijklmnopqrstuvwxyz0123456789áàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗộơớờởỡợéèẻẽẹêếềểễệúùủũụưứừửữựíìỉĩịýỳỷỹỵđ!\"\',\-\.:;?_\(\)]+$"}

# Mistake in Vietnamese spelling
letter_1 = list("abcdefghijklmnopqrstuvwxyzáàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗộơớờởỡợéèẻẽẹêếềểễệúùủũụưứừửữựíìỉĩịýỳỷỹỵđABCDEFGHIJKLMNOPQRSTUVWXYZÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÉÈẺẼẸÊẾỀỂỄỆÚÙỦŨỤƯỨỪỬỮỰÍÌỈĨỊÝỲỶỸỴĐ")
letter_2 = list("abcdefghijklmnopqrstuvwxyz")

# Vietnamese Type keyboard
type_keyboard = {"ă":"aw","â":"aa","á":"as","à":"af","ả":"ar","ã":"ax","ạ":"aj","ắ":"aws","ổ":"oor","ỗ":"oox","ộ":"ooj","ơ":"ow",
        "ằ":"awf","ẳ":"awr","ẵ":"awx","ặ":"awj","ó":"os","ò":"of","ỏ":"or","õ":"ox","ọ":"oj","ô":"oo","ố":"oos","ồ":"oof",
        "ớ":"ows","ờ":"owf","ở":"owr","ỡ":"owx","ợ":"owj","é":"es","è":"ef","ẻ":"er","ẽ":"ex","ẹ":"ej","ê":"ee","ế":"ees","ề":"eef",
        "ể":"eer","ễ":"eex","ệ":"eej","ú":"us","ù":"uf","ủ":"ur","ũ":"ux","ụ":"uj","ư":"uw","ứ":"uws","ừ":"uwf","ử":"uwr","ữ":"uwx",
        "ự":"uwj","í":"is","ì":"if","ỉ":"ir","ị":"ij","ĩ":"ix","ý":"ys","ỳ":"yf","ỷ":"yr","ỵ":"yj","đ":"dd",
        "Ă":"Aw","Â":"Aa","Á":"As","À":"Af","Ả":"Ar","Ã":"Ax","Ạ":"Aj","Ắ":"Aws","Ổ":"Oor","Ỗ":"Oox","Ộ":"Ooj","Ơ":"Ow",
        "Ằ":"AWF","Ẳ":"Awr","Ẵ":"Awx","Ặ":"Awj","Ó":"Os","Ò":"Of","Ỏ":"Or","Õ":"Ox","Ọ":"Oj","Ô":"Oo","Ố":"Oos","Ồ":"Oof",
        "Ớ":"Ows","Ờ":"Owf","Ở":"Owr","Ỡ":"Owx","Ợ":"Owj","É":"Es","È":"Ef","Ẻ":"Er","Ẽ":"Ex","Ẹ":"Ej","Ê":"Ee","Ế":"Ees","Ề":"Eef",
        "Ể":"Eer","Ễ":"Eex","Ệ":"Eej","Ú":"Us","Ù":"Uf","Ủ":"Ur","Ũ":"Ux","Ụ":"Uj","Ư":"Uw","Ứ":"Uws","Ừ":"Uwf","Ử":"Uwr","Ữ":"Uwx",
        "Ự":"Uwj","Í":"Is","Ì":"If","Ỉ":"Ir","Ị":"Ij","Ĩ":"Ix","Ý":"Ys","Ỳ":"Yf","Ỷ":"Yr","Ỵ":"Yj","Đ":"Dd"}

reverse_type = {w: k for k, w in type_keyboard.items()}


# Import class
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createMainWindow()

    def createMainWindow(self):
        # Create the main window
        self.input_text = QTextEdit(self)
        self.input_text.setGeometry(50, 70, 400, 200)

        self.output_text = QTextEdit(self)
        self.output_text.setGeometry(500, 70, 400, 200)

        self.label_input = QLabel(self)
        self.label_input.setText("Input text:")
        self.label_input.setGeometry(50, 10, 60, 80)

        self.label_output = QLabel(self)
        self.label_output.setText("Output text:")
        self.label_output.setGeometry(500, 10, 80, 80)

        self.correct_label = QLabel(self)
        self.correct_label.setGeometry(50, 320, 400, 50)

        # Create the check and correct with QPushButton
        self.button_check = QPushButton("Check Spelling", self)
        self.button_check.setGeometry(190, 280, 120, 30)
        self.button_check.clicked.connect(self.spell_checking)

        self.button_correct = QPushButton("Correct Spelling", self)
        self.button_correct.setGeometry(650, 280, 120, 30)
        self.button_correct.clicked.connect(self.correct_spelling)

        # Set main window title
        self.setWindowTitle("Vietnamese Spell Checker")
        self.setGeometry(300, 300, 1000, 400)
        self.show()


    def spell_checking(self):
        text = self.input_text.toPlainText()
        missSpelled_Words = []
        for words in text.split():
            if not self.is_Vietnamese(words):
                missSpelled_Words.append(words)

        self.correct_label.setText("Misspelled words: " + ",".join(missSpelled_Words))

    def is_Vietnamese(self, words):
        for char in words:
            if char not in alphabet:
                return False
        return True

    def correct_spelling(self):
        words = self.input_text.toPlainText()
        corrected_text = self.correct_vietnamese_text(words)
        self.output_text.setText(("Corrected words: " + corrected_text))
    
    def correct_vietnamese_text(self, text):
        corrected_text = ""
        for char in text:
            if char in reverse_type:
                corrected_text += reverse_type[char]
            else:
                corrected_text += char
        return corrected_text

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
