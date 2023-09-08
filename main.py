import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QTextEdit, QLineEdit, QApplication
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.bot = Chatbot()

        self.setWindowTitle("Chatbot window")
        self.setMinimumSize(700, 500)

        # add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # add input entry widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 50)

        # add send button widget
        button = QPushButton("Send", self)
        button.setGeometry(490, 350, 70, 40)
        button.clicked.connect(self.send_input)

        self.show()

    def send_input(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'> Me: {user_input} </p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.bot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'> Bot: {response} </p>")


app = QApplication(sys.argv)

bot_window = ChatbotWindow()

sys.exit(app.exec())
