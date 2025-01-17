import praw
import requests
import schedule
import time
import logging

logging.basicConfig(filename='reddit_bot.log', level=logging.INFO)


reddit = praw.Reddit(
    client_id='Replace with your client ID',
    client_secret='Replace with your client secret',
    username='Replace with your Reddit username',
    password='Replace with your Reddit password',
    user_agent='Posting-Bot/0.1 by Your-Username'
)

GROQ_API_KEY = 'Replace with your GROQ API key'
GROQ_API_URL = 'Replace with your GROQ API URL'

def generate_content(prompt):

    print("Generating content...")
    response = requests.post(
        GROQ_API_URL,
        headers={'Authorization': f'Bearer {GROQ_API_KEY}'},
        json={'model': 'llama3-8b-8192', 'messages': [{'role': 'user', 'content': 'prompt'}]}
    )
    if response.status_code == 200:
        data = response.json()
        choices = data.get('choices', [])
        if choices:
            content = choices[0].get('message', {}).get('content', '')
            print(f"Generated Content: {content}")
            return content
        else:
            print("No content returned by the API.")
            return None
    else:
        print(f"Error generating content: {response.text}")
        return None


def post_to_reddit():

    content = generate_content()
    if content:
        try:
            print("Posting to Reddit...")
            subreddit = reddit.subreddit('my_bot_subreddit')
            subreddit.submit(title='Daily Post', selftext=content)
            print("Post successful!")
            logging.info("Successfully posted to Reddit with title 'Daily Post'.")

        except Exception as e:
            print(f"Error posting to Reddit: {e}")
    else:
        print("Content generation failed. Skipping Reddit post.")


def comment_on_posts():
    
    try:
        subreddit = reddit.subreddit('my_bot_subreddit')
        print("Fetching posts for commenting...")
        posts = list(subreddit.hot(limit=3))  

        for post in posts:
            if post.num_comments == 0: 
                prompt = f"Write a comment for this Reddit post: {post.title}"
                comment = generate_content(prompt)
                if comment:
                    print(f"Commenting on post: {post.title}")
                    post.reply(comment)
                    print("Comment posted successfully!")
                    logging.info(f"Successfull commented on post: {post.title}")

    except Exception as e:
        print(f"Error commenting on posts: {e}")

def main():

    posting_times = ["22:00", "22:03", "22:06"]

    print("Initializing bot...")

    for post_time in posting_times:

        schedule.every().day.at(post_time).do(post_to_reddit)

    schedule.every().day.at("20:00").do(comment_on_posts) 

    while True:
        print("Waiting for the scheduled time...")
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
