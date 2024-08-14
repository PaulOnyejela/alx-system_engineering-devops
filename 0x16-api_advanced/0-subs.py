#!/usr/bin/python3
"""
This script queries the Reddit API and returns the number of total subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit: str) -> int:
    """
    Queries the Reddit API and returns the number of total subscribers for a
    given subreddit.

    :param subreddit: The subreddit to query.
    :return: The number of subscribers, or 0 if an error occurs.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Python/1.0 (Holberton School 0x16 task 0)'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    except (requests.RequestException, ValueError):
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
