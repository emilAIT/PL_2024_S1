# Вам нужно управлять книжным фондом библиотеки с помощью списка словарей. Каждый словарь представляет собой книгу, содержащую следующую информацию.

# Пример записи о книге:
# {
#   "title": "Великий Гэтсби",
#   "author": "Фрэнсис Скотт Фицджеральд",
#   "year": 1925,
#   "available": True
# }

library = []

# 1.   Напишите функцию `add_book(library, title, author, year)`, которая добавляет новую книгу в библиотеку. Книга изначально должна быть помечена как доступная. (10)

def add_book(library, title, author, year):
    book = {
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }
    library.append(book)
    

# 2.  Напишите функцию `search_by_title(library, title)`, которая ищет книгу по названию в библиотеке. Если книга существует, верните информацию о книге. Если нет — верните сообщение, что книга не найдена. (10)

def search_by_title(library, title):
    for d in library:
        if d['title'] == title:
            return d
    return 'Book not found'

# 3. Напишите функцию `borrow_book(library, title)`, которая позволяет пользователю взять книгу на время. Функция должна пометить книгу как недоступную, если она доступна. Если книга уже взята, верните соответствующее сообщение. (10)
def borrow_book(library, title):
    for d in library:
        if d['title'] == title:
            d['available'] = False
            return
    return 'Book not found'

# 4. Напишите функцию `return_book(library, title)`, которая отмечает книгу как снова доступную. Если книга уже доступна, верните сообщение о том, что книга не была взята.(10)
def return_book(library, title):
    for d in library:
        if d['title'] == title:
            d['available'] = True
            return
    return 'Book not found'

# 5. Напишите функцию `list_available_books(library)`, которая возвращает список всех доступных книг в библиотеке(10)
def list_available_books(library):
    count = []
    for d in library:
        if d['available'] == True:
            count.append(d)
    return count

# 6. Напишите функцию `find_books_by_author(library, author)`, которая возвращает список всех книг, написанных определенным автором. Если книги не найдены. (10)

def find_books_by_author(library, author):
    result = []
    for d in library:
        if d['author'] == author:
            result.append(d)
    return result


# 7.  Напишите функцию `count_books(library)`, которая возвращает общее количество книг в библиотеке, независимо от их доступности (10)
def count_books(library):
    return len(library)

def count_books2(library):
    count = 0
    for i in library:
        count += 1
    return count

# 8. Напишите функцию `remove_book(library, title)`, которая удаляет книгу по названию из библиотеки. Если книга не найдена, верните соответствующее сообщение.(5)
def remove_book(library, title):
    for index, d in enumerate(library):
        if d['title'] == title:
            library.pop(index)
            return 'removed'
    return 'not found'

# 9.  Напишите функцию `find_oldest_book(library)`, которая находит и возвращает книгу с самым ранним годом издания (5)
def find_oldest_book(library):
    oldest = library[0]
    for d in library:
        if d['year'] < oldest['year']:
            oldest = d
    return oldest


# 10. Напишите функцию `book_availability_stats(library)`, которая возвращает количество книг которые уже взяты (10)
def book_availability_stats(library):
    count = []
    for i in library:
        if library[i]['available'] == False:
            count.append(library[i])
    return count


# 11. Напишите функцию `find_books_by_year_range(library, start_year, end_year)`, которая возвращает список всех книг, опубликованных в заданном диапазоне лет (10)

def find_books_by_year_range(library, start_year, end_year):
    count = []
    for d in library:
        if start_year <= d['year'] <= end_year:
            count.append(d)
    return count




# задачи для управления салоном красоты, где вам нужно работать со списком клиентов. Каждая запись о клиенте будет храниться в виде словаря, содержащего следующую информацию.

# Пример записи о клиенте:
# ```python
# {
#   "name": "Анна Иванова",
#   "service": "Стрижка",
#   "date": "2024-09-15",
#   "paid": True
# }
# ```

# 1. Напишите функцию `add_client(salon, name, service, date)`, которая добавляет нового клиента в список. Клиент изначально должен быть помечен как оплативший услугу. (10)

salon = []
def add_client(salon, name, service, date):
    client = {
        "name": name, 
        "service":service,
        "date": date,
        "paid": True
    }
    salon.append(client)

# 2. Напишите функцию `search_by_name(salon, name)`, которая ищет клиента по имени. Если клиент существует, верните информацию о нем. Если нет — верните сообщение, что клиент не найден. (10)
def search_by_name(salon, name):
    for d in salon:
        if d['name'] == name:
            return d
    return 'not found'

# 3. Напишите функцию `update_service(salon, name, new_service)`, которая позволяет обновить услугу для существующего клиента. Если клиент не найден, верните соответствующее сообщение. (10)

def update_service(salon, name, new_service):
    for d in salon:
        if d['name'] == name:
            d['service'] = new_service
            return 'updated'
    return 'client not found'

# 4. Напишите функцию `mark_as_paid(salon, name)`, которая отмечает услугу клиента как оплаченную. Если услуга уже оплачена, верните сообщение об этом. (10)

def mark_as_paid(salon, name):
    for d in salon:
        if d['name'] == name:
            d['paid'] = True
            return 'updated'
    return 'client not found'

# 5. Напишите функцию `list_unpaid_clients(salon)`, которая возвращает список всех клиентов, которые еще не оплатили услуги. (10)

def list_unpaid_clients(salon):
    count = 0
    for d in salon:
        if not d['paid']:
            count += 1
    return count

# 6. Напишите функцию `find_clients_by_service(salon, service)`, которая возвращает список всех клиентов, которые воспользовались определенной услугой. Если таких клиентов нет, верните сообщение об их отсутствии. (10)

def find_clients_by_service(salon, service):
    count = []
    for d in salon:
        if d['service'] == service:
            count.append(d['name'])
    return count
# 7. Напишите функцию `count_clients(salon)`, которая возвращает общее количество клиентов в списке салона. (10)

def count_clients(salon):
    return len(salon)

# 8. Напишите функцию `remove_client(salon, name)`, которая удаляет клиента по имени. Если клиент не найден, верните соответствующее сообщение. (5)
def remove_cliend(salon, name):
    for index, d in enumerate(salon):
        if d['name'] == name:
            library.pop(index)
            return
    return 'client not found'

# 9. Напишите функцию `find_last_client(salon)`, которая находит и возвращает последнего клиента по дате посещения. (5)
def find_last_client(salon):
    return salon[-1]

# 10. Напишите функцию `client_payment_stats(salon)`, которая возвращает количество клиентов, оплативших услуги и количество неоплаченных услуг. (10)
def client_payment_stats(salon):
    unpaid_count =  list_unpaid_clients(salon)
    return len(salon) - len(unpaid_count), len(unpaid_count)


# 11. Напишите функцию `find_clients_by_date_range(salon, start_date, end_date)`, которая возвращает список всех клиентов, посетивших салон в заданном диапазоне дат. (10)
def find_clients_by_date_range(salon, start_date, end_date):
    result = []
    for d in salon:
        if start_date <= d['date'] <= end_date:
            result.append(d)
    return result