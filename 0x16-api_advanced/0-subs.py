#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == '__main__':
    from 0_subs import number_of_subscribers
    
    if len(sys.argv) < 2:
        print("Error: Please provide a subreddit name as an argument.")
    else:
        subscribers_count = number_of_subscribers(sys.argv[1])
        print(f"{subscribers_count}")
