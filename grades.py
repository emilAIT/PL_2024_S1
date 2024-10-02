import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtGui import QFont



##################################################
names = {}

def addGrade(name, grade, quiz):
    if name not in names:
        names[name] = {
            "quizes":[], 
            "grades":[]
        }
    names[name]['quizes'].append(quiz)
    names[name]['grades'].append(grade)


def getGrades(name):
    if name in names:
        return list(zip(names[name]['quizes'], names[name]['grades']))
    else:
        return name + " does not exist in the database"

def getAll():
    arr2 = []
    for i in names:
        arr = names[i]['grades']
        avg = sum(arr) / len(arr)
        arr2.append((i, avg))
    return arr2


#################################################


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Create UI elements
        self.name_label = QLabel('imya:')
        self.name_edit = QLineEdit()
        self.quiz_label = QLabel('quiz:')
        self.quiz = QLineEdit()
        self.grade_label = QLabel('grade:')
        self.grade = QLineEdit()


        self.addGradeButton = QPushButton('Add grade:')
        self.allButton = QPushButton('Get All Grades')

        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)  # Makes the text area read-only

        # Set the font size
        font = QFont()
        font.setPointSize(18)  # Adjust this value to make the text bigger


        self.name_label.setFont(font)
        self.name_edit.setFont(font)
        self.quiz_label.setFont(font)
        self.quiz.setFont(font)
        self.grade_label.setFont(font)
        self.grade.setFont(font)
        self.addGradeButton.setFont(font)
        self.text_output.setFont(font)
        self.allButton.setFont(font)


        # Connect the button click to the function
        self.addGradeButton.clicked.connect(self.addGrade)
        self.allButton.clicked.connect(self.getAllGrades)

        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.quiz_label)
        layout.addWidget(self.quiz)
        layout.addWidget(self.grade_label)
        layout.addWidget(self.grade)
        layout.addWidget(self.addGradeButton)
        layout.addWidget(self.allButton)
        layout.addWidget(self.text_output)

        self.setLayout(layout)
        self.setWindowTitle('GRADES')
        self.setGeometry(200, 200, 400, 300)

    def getAllGrades(self):
        text = 'AVERAGE GRADE OF ALL STUDENTS\n\n'
        arr = getAll()
        for name, avg in arr:
            text += f'{name} -> {avg}\n'
        self.text_output.setPlainText(text)


    def addGrade(self):
        name = self.name_edit.text()
        quiz = self.quiz.text()
        grade = int(self.grade.text())

        addGrade(name, grade, quiz)
        p = getGrades(name)
        text = 'GRADES FOR ' + name + '\n\n'
        sum, cnt = 0, 0
        for q, g in p:
            text += f'{q} -> {g}\n'
            sum += int(g)
            cnt += 1
        text += f'\n\n AVERAGE : {sum/cnt}'

        self.name_edit.setText('')
        self.quiz.setText('')
        self.grade.setText('')
        self.text_output.setPlainText(text)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
