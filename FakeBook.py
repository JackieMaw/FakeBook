import random
from datetime import datetime, timedelta

USERS = ['Amelia','Muhammad','Olivia','Noah','Sofia','Leo',
'Mia','Oliver','Maya','Arthur','Sophia','Adam','Ava','George',
'Isabella','Alexander','Emily','Oscar','Isla','Theo']

FRIENDS = set()

MESSAGES = [
    "Can't wait to see the Ed Sheeran on Saturday... it's going to be off-da-hook",
    "Wish I hadn't gone to bed so late last night...",
    "Thank you my CheChe for the delicious chocolates!",
    "The internet has absolutely ruined people's brains.",
    "I've finally finished my Maths assignment",
    "Had a really tough day today",
    "So proud of my boyfriend for winning the Bexley Swim Champs xxx",
    "Horrific History Test today... FAIL :-(",
    "Yay Friday! Can't wait to CHILL",
    "Christmas cups are here... just saying!",
    "No seriously, who is doing the official posters for the new Matrix movies? They're so bad!",
    "So over being sick now... what is with all these super-colds?",
    "Any suggestions for dinner tonight? So bored with FOOD!",
    "BC81 tonight - awesome music, felt really pumped.",
    "Did anyone catch the sunset this afternoon? Wow. Just Wow.",
    "Off to see my bestie this weekend... why did you have to move so far AWAY! Selfish!",
    "Why me",
    "Is that ref serious???"
]

class Post():

    def __init__(self, id, name, timestamp, message, likes):
        self.id = id
        self.name = name
        self.timestamp = timestamp
        self.message = message
        self.likes = likes

    def __repr__(self):
        return f'Post({self.name}|{self.timestamp}|{self.message}|{self.likes})'  

    def __str__(self):
        return f'{self.name} [{self.timestamp}] => {self.message} ({self.likes} likes)'

def generate_random_posts():
    num_messages = len(MESSAGES)
    num_users = len(USERS)
    time_now = datetime.now()
    RANDOM_POSTS = {}
    for x in range(101):
        m = random.randint(0,num_messages-1)
        u = random.randint(0,num_users-1)
        l = random.randint(0,5)
        post_time = time_now - timedelta(minutes=3*x)
        RANDOM_POSTS[x] = Post(x, USERS[u], post_time.strftime('%H:%M'), MESSAGES[m], l)
    return RANDOM_POSTS

POSTS = generate_random_posts()

def add_post(user, message):
    x = len(POSTS) + 1
    POSTS[x] = Post(x, user, datetime.now().strftime('%H:%M'), message, 0)
    return x

def print_users():
    print(f'There are {len(USERS)} Users on FakeBook:')
    for user in USERS:
        print(f"     {user}")

def is_friend(name):
    return name in FRIENDS

def add_friend(name):
    if name in USERS:
        FRIENDS.add(name)
        print(f"You are now friends with: {name}")
        return True
    else:
        print(f"Sorry you can't be friends with {name} because they are not on FakeBook!")
        return False

def print_friends():
    print(f'You have {len(FRIENDS)} friends:')
    for friend in FRIENDS:
        print(f"     {friend}")

#============================================
