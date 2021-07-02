# imports PRAW
import praw
import time
import OAuth2Util

# CHANGE THESE VARIABLES
sub = "SUBREDDIT HERE"

# connects to user agent
r = praw.Reddit("Reddit dat-boi v2.0 made by /u/ImInThatCorner and contribituion from /u/UnknownDeveloper")
o = OAuth2Util.OAuth2Util(r)
o.refresh(force=True)

# creates array with comment ids that have already been replied to
comment_ids = []

# starts the program
def run(subreddit):
    # gets the subreddit to where the bot will run
    sub = r.get_subreddit(subreddit)
    # gets the comments to a limit of 250 comments
    comments = sub.get_comments(limit=250)
    # runs a for loop that runs through every comment
    for comment in comments:
        # gets comment and stores it as comment_text
        comment_text = comment.body.lower()
        # checks if the comment has the necessary text and if it hasn't been replied to yet
        if comment_text == "here comes dat boi" and comment.id not in comment_ids:
            try:
                # replies to comment
                comment.reply("waddup")
                # stores comment id in array for comment_ids
                comment_ids.append(comment.id)
            except:
                print("Failed... Trying again")
                break


# runs program with teenagers subreddit
while True:
    run(sub)
    time.sleep(10)
