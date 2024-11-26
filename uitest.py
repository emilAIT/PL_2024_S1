import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class Movie:
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule
        self.clients = []

    def book_ticket(self, client):
        self.clients.append(client)
    
    def remove_client(self, client):
        self.clients.remove(client)
    
    def getavailabe_seats(self):
        return len(self.clients)
    
    def get_details(self):
        return self.name + ' ' + self.schedule

class Client:
    def __init__(self, name):
        self.name = name
        self.movies = []
    
    def book_ticket(self, movie):
        self.movies.append(movie)
    
    def remove_movie(self, movie):
        self.movies.remove(movie)
    
    def get_booked_movies(self):
        return '\n'.join([i.name for i in self.movies])
        

class Cinema:
    def __init__(self):
        self.movies = []
        self.cost = 500
        self.percentage = 0.4
        self.booking_ids = {}

    
    def add_movie(self, movie):
        self.movies.append(movie)
    
    def remove_movie(self, movie):
        self.movies.remove(movie)
    
    def list_movies(self):
        return '\n'.join([i.get_details() for i in self.movies])

    def book_ticket(self, movie, client):
        id = movie.get_details() + client.name
        self.booking_ids[id] = (client, movie)
        movie.book_ticket(client)
        client.book_ticket(movie)
        return id

    def cancel_ticket(self, booking_id):
        client, movie = self.booking_ids[booking_id]
        movie.remove_client(client)
        client.remove_movie(movie)
    
    def get_seating_plan(self, movie):
        return movie.clients

    def get_total_cost(self, movie):
        return len(movie.clients) * self.cost

    def get_total_profit(self):
        return sum([len(movie.clients) for movie in self.movies]) * self.cost * self.percentage

    def get_customers_who_watched_multiple_films(self):
        from collections import defaultdict
        d = defaultdict(int)
        for movie in self.movies:
            for client in movie.clients:
                d[client] += 1
        
        arr = []
        for client, count in d.items():
            if count > 1:
                arr.append(client.name)
        return '\n'.join(arr)
    
cinema = Cinema()

class BookTicket(QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = QLineEdit("Movie name")
        self.label2 = QLineEdit("Schedule")
        self.label3 = QLineEdit("Client name")
        self.button = QPushButton("Add movie")
        self.label = QLabel("booking_id")
        self.button.clicked.connect(self.add_movie)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.label3)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.resize(300,300)
    
    def add_movie(self):
        pass


class AddMovie(QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = QLineEdit("Movie name")
        self.label2 = QLineEdit("Schedule")
        self.button = QPushButton("Add movie")
        self.label = QLabel("booking_id")
        self.button.clicked.connect(self.add_movie)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.button)
        layout.addChildWidget(self.label)
        self.setLayout(layout)
        self.resize(300,300)
    
    def add_movie(self):
        pass


class CancelMovie(QWidget):
    def __init__(self):
        super().__init__()
        self.label1 = QLineEdit("Movie name")
        self.label2 = QLineEdit("Schedule")
        self.button = QPushButton("Add movie")
        self.label = QLabel("booking_id")
        self.button.clicked.connect(self.remove_movie)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.resize(300,300)
    
    def remove_movie(self):
        #cinema.remove()
        pass

class SimpleUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.ui = []
        self.add_movie = []
        self.cancel_movie = []

    def init_ui(self):
        # Create widgets
        self.label = QLabel("Cinematica", self)
        self.add_movie_button = QPushButton("Add movie", self)
        self.book_button = QPushButton("Book Ticket", self)
        self.cancel_button = QPushButton("Cancel Ticket", self)

        # Connect button click to the update function
        self.book_button.clicked.connect(self.open_window)
        self.add_movie_button.clicked.connect(self.add_movie)
        self.cancel_button.clicked.connect(self.cancel_movie)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.add_movie_button)
        layout.addWidget(self.book_button)
        layout.addWidget(self.cancel_button)
        self.setLayout(layout)

        # Window settings
        self.setWindowTitle("Simple PyQt UI")
        self.resize(300, 200)

    def open_window(self):
        self.ui.append(BookTicket())
        self.ui[-1].show()
    
    def add_movie(self):
        self.add_movie.append(AddMovie())
        self.add_movie[-1].show()

    def cancel_movie(self):
        self.cancel_movie.append(CancelMovie())
        self.cancel_movie[-1].show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleUI()
    window.show()
    sys.exit(app.exec_())
