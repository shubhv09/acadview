from datetime import datetime


class Spy:

  def __init__(self, name, salutation, age, rating):
    self.name = name
    self.salutation = salutation
    self.age = age
    self.rating = rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None


spy = Spy('Shubham','Mr.',26,4.8)

friend_one = Spy('Sarthak', 'Mr.', 28, 3.9)
friend_two = Spy('Siddhant', 'Mr.', 31, 2.3)
friend_three = Spy('Kawal', 'Dr.', 42, 4.0)

friends = [friend_one, friend_two, friend_three]


class Chat_message:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me