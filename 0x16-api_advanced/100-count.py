#!/usr/bin/python3
"""Function that queries the Reddit API and prints the top ten hot posts of a subreddit"""

import requests


def count_words(subreddit, word_list, counts={}, next_after=None):
    """Queries Reddit API for the subreddit"""

    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        params={"after": next_after},
        headers={"User-Agent": "Custom-Agent"},
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json()

    titles = [item.get("data").get("title")
              for item in data.get("data").get("children")]

    if not titles:
        return None

    word_list = list(dict.fromkeys(word_list))

    if counts == {}:
        counts = {word: 0 for word in word_list}

    for title in titles:
        words_in_title = title.split(' ')
        for word in word_list:
            for w in words_in_title:
                if w.lower() == word.lower():
                    counts[word] += 1

    if not data.get("data").get("after"):
        sorted_counts = sorted(counts.items(), key=lambda kv: kv[0])
        sorted_counts = sorted(counts.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list, counts,
                           data.get("data").get("after"))
 