#import details

import csv
from steganography.steganography import Steganography
from spy_details import spy,friends,Spy,Chat_message
from datetime import datetime

print'Welcome to spy chat\n'

print 'let\'s get started'

#status list

STATUS_MESSAGES = ['Hello', 'Hi', 'my name is bond', 'How you doing friends', 'High', 'Busy', 'Love you ol.']

#questioning if he want to continue as default user or create new spy

question = "continue as " + spy.salutation + ' ' + spy.name + "(Y/N)?"
print 'Welcome Onboard MrSpy'

exciting = input(question)

#add friend function

def add_friend():
    new_friend = Spy('','',0,0.0)

    new_friend.name = input("Please add your friend's name: ")
    new_friend.salutation = input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = input("Age?")

    new_friend.rating = input("Spy rating?")

    if len(new_friend.name) > 0 and new_friend.age > 12:

        friends.append(new_friend)
        with open("friends.csv",'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name, new_friend.salutation, new_friend.age, new_friend.rating, True])
        print '%s Added in friend list' % (new_friend.name)
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with these details'

    return len(friends)

#select a friend function


def select_friend():

    item_number = 0

    for friend in friends:
        print '%d. %s' % (item_number + 1,friend.name)

        item_number = item_number + 1

    friend_choice = input('choose from friends')

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


#add status function

def add_status(current_status_message):

    updated_status_message = None

    if current_status_message != None:

        print 'Your current status message is %s \n' % (current_status_message)
    else:

        print("you do not have any status messages currently \n")

    default = input(" Do you want to select from older status messages (y/n)?\n ")

    if default.upper() == "N":

        new_status_message = input("what status you want to set?")

        if len(new_status_message) > 0:

            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == "Y":

            item_position = 1

            for message in STATUS_MESSAGES:

                print '%d. %s' % (item_position, message)
                item_position = item_position + 1

            message_selection = int(input("\n Choose from above messages\n"))

            if len(STATUS_MESSAGES) >= message_selection:

                updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print('wrong input. Please choose either y or n ')

    if updated_status_message:
        print 'your updated status message is %s ' % (updated_status_message)
    else:
        print('you did not update your status')

    return updated_status_message

#send message

def send_message():

    friend_choice = select_friend()

    original_image = input("input the name of the image\n")
    output_path = 'output.jpg'
    text = input("enter the hidden message\n")
    if text.upper() == "HELP ME" or text.upper() == "I NEED YOU" or text.upper() == "SAVE ME":
        print"EMERGENCY, PLEASE REPLY"
    Steganography.encode(original_image, output_path, text)

    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    friends[friend_choice].chats.append(new_chat)

    print "secret message encrypted"

#read a message

def read_a_message():

    sender = select_friend()

    output_path = input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[sender].chats.append(new_chat)

    print "image decrypted, message saved"

#load friends fuction

def loadFriends():
    with open("friends.csv", "rb") as friends_list:
        reader = list(csv.reader(friends_list))

        for row in reader[1:]:

            print(row)
        friends.append(spy)

def loadMessage():

    with open("chats.csv", "rb") as chat_box:
        reader = list(csv.reader(chat_box))

        for row in reader:
            print row

            spy.chats.append(row)
            print('message loaded')


def read_chat_history():
    read_for = select_friend()
    if len(friends[read_for].chats):
        for chat in friends[read_for].chats:
            a = chat.time.strftime('%A, %d %B %Y %H:%M:%S')

            if chat.sent_by_me:
                print'[%s] %s: %s' % (a, 'you said:', 'Blue' + chat.message)
            else:
                print '[%s] %s read:%s' % (a, friends[read_for].name, 'Black' + chat.message)
    else:
        print " There is no chat history "

#defining chat function

def start_chat(spy):

    current_status_message = None
    loadFriends()
    loadMessage()
    show_menu = True

    while show_menu == 1:
        menu_choices = "What do you want to do? \n 1. Add a status update\n 2. Add a friend\n 3.Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6.close application\n"
        menu_choice = input(menu_choices)

        if menu_choice == 1:
            current_status_message = add_status(current_status_message)

        elif menu_choice == 2:
            number_of_friends = add_friend()
            print 'you have %d friends' % (number_of_friends)

        elif menu_choice == 3:
            send_message()

        elif menu_choice == 4:
            read_a_message()

        elif menu_choice == 5:
            read_chat_history()

        else:
            show_menu = False


if exciting == 'Y':

    start_chat(spy)
else:
    spy = ('','',0,0.0)

    spy.name = input('what is your name?')

    if len(spy.name) > 0:
        spy.salutation = input('what should we call you (Mr or Ms)?')
        spy.name = spy.salutation + '' + spy.name
        print 'welcome ' + spy.name + ' glad to have you back'
        print 'alright ' + spy.name + ' i would like to know more about you'

        #entering all other authentication criterias||deleted variables becoz imported them from spy_details

        spy.age = input('enter your age\n')

        #checking age

        if spy.age > 15 and spy.age < 50:

            print('valid spy')

            #entering spy rating if age is valid

            spy.rating = input('what is your spy rating\n')

            if spy.rating > 4.5:

                print('great ace')

            elif spy.rating >= 3.5 and spy.rating <= 4.5:

                print('you are a good spy')

            elif spy.rating >= 2.5 and spy.rating <= 3.5:

                print('you can be a better spy')

            else:
                print('you can contact our office anytime')

                #completing spy rating and welcoming him

            print("authentication complete. Welcome " + spy.name + " age:" + str(spy.age) + " rating:" + str(spy.rating))

            print('Proud to have you on board')

            start_chat(spy)

        else:
            print('sorry you are not of required spy age')

    else:
        print ("""Sorry a spy must have a name
        please enter your name""")