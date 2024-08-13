#!/usr/bin/python3
"""
    Uses Reddit API to get all hot posts
"""
import requests

def recurse(subreddit, hot_list=[]):
    """Get all hot posts from a subreddit"""
    def fetch_posts(subreddit, after=""):
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
        headers = {'User-Agent': 'request'}
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            return None, None

        r_json = response.json()
        posts = r_json.get("data").get("children")
        next_after = r_json.get("data").get("after")

        return posts, next_after

    posts, after = fetch_posts(subreddit)
    if posts is None:
        return None

    for post in posts:
        hot_list.append(post.get("data").get("title"))

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list)
