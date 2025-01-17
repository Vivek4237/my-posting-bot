# my-posting-bot
This bot automatically posts generated content to a subreddit and comments on other posts using the GROQ AI API. 


Features
1. Automatically posts daily content to a specified subreddit.
2. Comments on other posts within the subreddit using AI-generated responses.
3. Logs successful posts and comments.

Libraries :
> Python 3.6 or Higher
> pip install praw (Python Reddit API Wrapper library )
> pip install requests 
> pip install schedule (library for task scheduling)

Setup Instruction :
> Clone or Download the Code
> Create a Reddit Application
> Go to [Reddit's Developer Portal](https://www.reddit.com/prefs/apps).
> Click Create App or Create Another App.
- Fill out the form:
  -  App Type: Select "Script".
  -  Name : Provide a name for your bot.
  -  Redirect URI : Use `http://localhost:8080` (or any dummy URI).
  - Save the app.
> Configure Reddit API Credentials
> Replace the placeholders in the `reddit = praw.Reddit()` section of the script:
  ```
  reddit = praw.Reddit(
      client_id='your_client_id',
      client_secret='your_client_secret',
      username='your_username',
      password='your_password',
      user_agent='your_user_agent'
  )
```
> Select Target Subreddit
> Schedule Timings (The times should follow a 24-hour format.)
> Open a terminal and navigate to the folder containing `reddit_bot.py`
> Run the script
