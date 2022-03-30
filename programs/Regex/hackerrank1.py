
import re
#Regex_Pattern = r'^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}'
#user_input = int(input())

#for i in range(0, user_input):

#    pattern = input()
#    if re.search(Regex_Pattern, pattern):
#        print("VALID")
#    else:
#        print("INVALID")


line = int(input())

for i in range(0, line):
    string = input()
    if re.search(r'^(hackerrank)\w+$', string):
        print("1")
    elif re.search(r'^\w+(hackerrank)$', string):
        print("2")
    elif re.search(r'^hackerrank&', string):
        print("0")
    else:
        print("-1")