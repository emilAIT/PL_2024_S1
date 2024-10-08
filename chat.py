users = {}
events = {}
history = []
chat = {}
delimeter = '\n'

def addUser(nick, name, tel_number):
    if nick in users:
        return f'{nick} already exists in the database'
    else:
        users[nick] = {"name": name, "tel_number": tel_number}
        return f'{nick} was successfully added'
    
def addToChat(sender, receiver, event_id):
    if sender in chat:
        if receiver in chat[sender]:
            chat[sender][receiver].append(event_id)
        else:
            chat[sender][receiver] = [event_id]
    else:
        chat[sender] = {receiver:[event_id]}

def addEvent(sender, receiver, message):
    if sender not in users:
        return f'{sender} is not in user base'
    if receiver not in users:
        return f'{receiver} is not in user base'
    event_id = len(events)
    events[event_id] = {"sender":sender, "receiver":receiver, "message":message}
    history.append(event_id)
    addToChat(sender, receiver, event_id)
    addToChat(receiver, sender, event_id)
    print(chat)
    return f'ADDED : {sender}->{receiver} : {message}'


def getHistory():
    output = 'HISTORY' + delimeter + delimeter
    for event_id in history:
        sender_id = events[event_id]['sender']
        receiver_id = events[event_id]['receiver']
        message = events[event_id]['message']
        output += users[sender_id]['name'] + ' -> ' + users[receiver_id]['name']  + ' : ' + message + delimeter 
    return output

def getMessages(user):
    output = user + delimeter + 'MESSSAGES' + delimeter
    for _, msgs in chat[user].items():
        for event_id in msgs:
            sender_id = events[event_id]['sender']
            receiver_id = events[event_id]['receiver']
            message = events[event_id]['message']
            output += users[sender_id]['name'] + ' -> ' + users[receiver_id]['name']  + ' : ' + message + delimeter 
    return output


while True:
    command = input('command (new/event/history/get) ? >')

    if command == 'new':
        nick, name, tel = input('Nick, name, tel ? >').split(',')
        print(addUser(nick, name, tel))
    elif command == 'event':
        sender, receiver, message = input('Who, whom, message ? >').split(',')
        addEvent(sender, receiver, message)
    elif command == 'history':
        print(getHistory())
    elif command == 'get':
        user = input('what is username ? >')
        print(getMessages(user))
    else:
        print(f'Unknown command -> {command}')
