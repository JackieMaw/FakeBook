from FakeBook import *

#======================================
#    STUDENTS PUT YOUR CODE IN HERE
#======================================

#TASK 1 - TEST EXISTING FUNCTIONS

print("TASK 1)")

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

#a) Hard-code adding a Friend

print("TASK 2a)")

add_friend('Noah')
add_friend('Isla')
add_friend('Adam')
add_friend('Muhammad')
add_friend('Oliver')    

#b) Ask the User to Choose a Friend

#print("TASK 2b)")

#friend = input("Please choose a friend: ")
#add_friend(friend)

#c) Ask the User to Choose 5 Friends

#print("TASK 2c)")

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

#a) Print News Feed

print("TASK 3a)")

print("===========FAKEBOOK NEWS FEED===========")
for post in POSTS.values():
    pretty_print(post)
print("========================================")

#b) Print News Feed for One Friend

print("TASK 3b)")

print("===========FAKEBOOK NEWS FEED - Noah ONLY===========")
for post in POSTS.values():
    if post.name == "Noah":
        pretty_print(post)
print("=======================================================")

#c) Display News Feed for All Friends

print("TASK 3c)")

print("===========FAKEBOOK NEWS FEED - FRIENDS ONLY===========")
for post in POSTS.values():
    if (is_friend(post.name)):
        pretty_print(post)
print("=======================================================")

#d) Display News Feed for All Friends - Top 20 Only

print("TASK 3d)")

print("===========FAKEBOOK NEWS FEED - TOP 20 ===========")
post_count = 0
for post in POSTS.values():
    if is_friend(post.name) and (post_count < 20):
        pretty_print(post)
        post_count = post_count + 1
print("==================================================================")

#TASK 4 - POST AND LIKE POSTS

#a) Add a Post

print("TASK 4a)")

post_id = add_post("Noah", "Hey Guys Whatsuuuuuuuuuuuupppppp")
print("Added a New Post by Noah with id:")
print(post_id)

print("===========FAKEBOOK NEWS FEED - Noah ONLY===========")
for post in POSTS.values():
    if post.name == "Noah":
        pretty_print(post)
print("=======================================================")

#b) Like a Post

print("TASK 4b)")

print("Liking my new post...")
POSTS[post_id].likes += 100

print("===========FAKEBOOK NEWS FEED - Noah ONLY===========")
for post in POSTS.values():
    if post.name == "Noah":
        pretty_print(post)
print("=======================================================")

#c) Like all Posts from a Friend

print("TASK 4c)")

for post in POSTS.values():
    if post.name == "Isla":
        post.likes += 100

print("===========FAKEBOOK NEWS FEED - Isla ONLY===========")
for post in POSTS.values():
    if post.name == "Isla":
        pretty_print(post)
print("=======================================================")
