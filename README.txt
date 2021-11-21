WORKSHOP OVERVIEW

Introduction - 5 mins: Introduction into the outline of the lesson and introduce yourself & Introduce Lauriann's STEM Club 
Presentation – 15 mins: 5 mins Career talk + 10 mins Lesson on Software Development.
Activity – 65 mins: 15 mins Analysis & Design + 30mins Building + 5 mins Testing + 15 mins Retrospective
Feedback forms – 10 mins: Students fill in feedback on how the session went.

Presentation = 15 minutes
About Me and My Job (5 mins)
The PDCA Cycle (3 mins)
Different roles in Software Development (2 mins)
Agile - Incremental Delivery (5 mins) 

Workshop Activity

- PLAN (15mins)
10 mins to do Analysis + Design, 5 mins to Discuss
- DO - Build it! (35mins)
Explain Pair Programming
Print out task list in case anyone wants to move forward faster?
- CHECK - Does it work? (5mins)
Invite someone from another team to check what you have built and see if it works.
- ACT/ADJUST - How did it go? (15mins)
10 mins to do a Retrospective, 5 mins to share
Retrospective, how did it go? what challenges did we face? what should we keep doing?
Use post-its to identify
- Start = yellow/blue, Stop = pink, Continue = green
Required: Post-its, a wall to stick on

================================================
EXERCISE: Build a FakeBook News Feed

(Break into pairs, explain pair programming)

Fast forward a week and your team has already completed these features:

1. Build and Display a List of Users - DONE
2. Build and Display a List of Friends - DONE
3. Check if a User is a Friend - DONE
4. Randomly Generate some Posts for Testing - DONE

Test the features your team already wrote:

print_users()
print_friends()
print(is_friend("Jackie"))
print(POSTS)

And then work on the remaining tasks:

5. Add Friends
6. Build a News Feed
7. Add a Post
8. Like a Post

Work in pairs. Assume we are already logged in for a single user.

Extension Ideas:
Look at the pre-built code...
You can change the names of the 20 Users
Add some more Random Messages
Generate 200 Random Posts instead of 100
Change the pretty_print function to look something like this:
Emily [17:43] +2
     The internet has absolutely ruined people's brains. 


>>>>>>>>>>>>>>>>>MORE DETAILED INSTRUCTIONS<<<<<<<<<<<<<<<<<<<<<<<<<

TASK 1. 
Test the features your team already wrote:
    print_users()
    print_friends()
    print(is_friend("Jackie"))
    print(POSTS)

TASK 2. 
You have no friends! How sad... Add Friends
    a) hard-code adding a friend
    b) ask the user to enter a friends name
    c) ask the user to enter 5 friends name

TASK 3. 
Your news feed is a mess! You are seeing messages from all users and there are too many to read. Filter News Feed.
    a) Build a News Feed to view all Posts 
    b) Build a News Feed to view only Posts from your Friends
    c) Build a News Feed to view only the last 20 Posts from your Friends

TASK 4.
Time to start interacting with the world!
Add a Post, and Like some Posts
    a) Add a Post
    b) Like the Post you Added
    c) Like all Posts from a Friend

====================================================================================

Extension Ideas:
1)
Have you noticed that there is a bug? When you add a new post, it shows it LAST instead of first.
Modify the Post class to save the full timestamp, and sort the posts before displaying them.
2)

====================================================================================
