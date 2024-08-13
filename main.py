import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox
from PyQt5.QtGui import QFont

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Tic Tac Toe")
        self.setStyleSheet("background-color: #2e2e2e;")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        for i in range(3):
            for j in range(3):
                button = QPushButton(" ")
                button.setFixedSize(100, 100)
                font = QFont()
                font.setPointSize(20)
                button.setFont(font)
                button.setStyleSheet("background-color: #4c4c4c; color: #ffffff; border: 2px solid #333;")
                button.clicked.connect(lambda checked, row=i, col=j: self.on_click(row, col))
                self.buttons[i][j] = button
                grid_layout.addWidget(button, i, j)

        self.show()

    def on_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].setText(self.current_player)
            if self.current_player == "X":
                self.buttons[row][col].setStyleSheet("background-color: #ff6666; color: #ffffff; border: 2px solid #333;")
            else:
                self.buttons[row][col].setStyleSheet("background-color: #66ff66; color: #ffffff; border: 2px solid #333;")
            if self.check_winner():
                QMessageBox.information(self, "Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_tie():
                QMessageBox.information(self, "Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.computer_move()

    def check_winner(self):

        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return True


        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True


        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

        return False

    def check_tie(self):
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def computer_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == " "]
        row, col = random.choice(empty_cells)
        self.board[row][col] = self.current_player
        self.buttons[row][col].setText(self.current_player)
        if self.current_player == "O":
            self.buttons[row][col].setStyleSheet("background-color: #66ff66; color: #ffffff; border: 2px solid #333;")
        if self.check_winner():
            QMessageBox.information(self, "Tic Tac Toe", f"Player {self.current_player} wins!")
            self.reset_game()
        elif self.check_tie():
            QMessageBox.information(self, "Tic Tac Toe", "It's a tie!")
            self.reset_game()
        else:
            self.current_player = "X"

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText(" ")
                self.buttons[i][j].setStyleSheet("background-color: #4c4c4c; color: #ffffff; border: 2px solid #333;")
                self.board[i][j] = " "
        self.current_player = "X"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TicTacToe()
    sys.exit(app.exec_())
