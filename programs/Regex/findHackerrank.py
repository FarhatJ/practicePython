"""
 Each conversation fits in 1 line and there are N such conversations. Each conversation has at most 1 word that says hackerrank (all in lowercase). We would like you to help us figure out whether a conversation:

1. Starts with hackerrank
2. Ends with hackerrank
3. Start and ends with hackerrank

Output Format

For every line,

Print 1 if the conversation starts with hackerrank
Print 2 if the conversation ends with hackerrank
Print 0 if the conversation starts and ends with hackerrank
Print -1 if none of the above. 

"""
import re

for _ in range(int(input())):
    s=input()
    if re.search(r'^hackerrank(.*hackerrank)?$',s):
        print(0)
    elif re.search(r'^hackerrank',s):
        print(1)
    elif re.search(r'hackerrank$',s):
        print(2)
    else:
        print(-1)