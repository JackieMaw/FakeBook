from FakeBook import *

#======================================
#    STUDENTS PUT YOUR CODE IN HERE
#======================================

#TASK 1 - TEST EXISTING FEATURES

print("TASK 1) Test Existing Features")

#CHECK WHAT USERS ARE ON FAKEBOOK
print_users() 

#CHECK IF YOU HAVE ANY FRIENDS
print_friends()

print("Is Noah a friend?")
print(is_friend("Noah"))

print("Is Maya a friend?")
print(is_friend("Maya"))

#CHECK THE RANDOMLY GENERATED POSTS
print(POSTS)

#TASK 2 - ADD FRIENDS

#a) Add a Friend (hard-code)

print("TASK 2a) Add a Friend (hard-code)")

add_friend('Noah')
add_friend('Isla')
add_friend('Adam')
add_friend('Muhammad')
add_friend('Oliver')    

#b) Add a Friend - Ask User to choose the name

#print("TASK 2b) Add a Friend - Ask User to choose the name")

#friend = input("Please choose a friend: ")
#add_friend(friend)

#c)

#print("TASK 2c) Add 5 Friends - User to choose the names")

#print("You can choose 5 friends.")
#for i in range(0,5):
#    friend = input("Enter a friend's name: ")
#    add_friend(friend)

#CHECK IF YOU HAVE ANY FRIENDS NOW?

print_friends()

print("Is Noah a friend?")
print(is_friend("Noah"))

print("Is Maya a friend?")
print(is_friend("Maya"))

#TASK 3 - FILTER NEWS FEED

#a) Display News Feed

print("TASK 3a) Display News Feed")

print("===========FAKEBOOK NEWS FEED===========")
for post in POSTS.values():
    print(post)
print("========================================")

#b) Display News Feed for One Friend

print("TASK 3b) Display News Feed for One Friend")

print("===========FAKEBOOK NEWS FEED - Noah ONLY===========")
for post in POSTS.values():
    if post.name == "Noah":
        print(post)
print("=======================================================")

#c) Display News Feed for All Friends

print("TASK 3c) Display News Feed for All Friends")

print("===========FAKEBOOK NEWS FEED - FRIENDS ONLY===========")
for post in POSTS.values():
    if (is_friend(post.name)):
        print(post)
print("=======================================================")

#d) Display News Feed for All Friends - Top 20 Only

print("TASK 3d) Display News Feed for All Friends - Top 20 Only")

print("===========FAKEBOOK NEWS FEED - TOP 20 ===========")
post_count = 0
for post in POSTS.values():
    if is_friend(post.name) and (post_count < 20):
        print(post)
        post_count = post_count + 1
print("==================================================================")

#TASK 4 - POST AND LIKE POSTS

#a) Add a Post

print("TASK 4a) Add a Post")

post_id = add_post("Noah", "Hey Guys Whatsuuuuuuuuuuuupppppp")
print("Added a New Post by Noah with id:")
print(post_id)

print("===========FAKEBOOK NEWS FEED - Noah ONLY===========")
for post in POSTS.values():
    if post.name == "Noah":
        print(post)
print("=======================================================")

#b) Like a Post

print("TASK 4b) Like a Post")

POSTS[post_id].likes += 100

print("===========FAKEBOOK NEWS FEED - Noah ONLY===========")
for post in POSTS.values():
    if post.name == "Noah":
        print(post)
print("=======================================================")

#c) Like all Posts from a Friend

print("TASK 4c) Like all Posts from a Friend")

for post in POSTS.values():
    if post.name == "Isla":
        post.likes += 100

print("===========FAKEBOOK NEWS FEED - Isla ONLY===========")
for post in POSTS.values():
    if post.name == "Isla":
        print(post)
print("=======================================================")