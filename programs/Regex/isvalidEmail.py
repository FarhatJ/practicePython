"""
Program to check whether your given email id is valid or not.

"""
import re
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
user_input = input()
if re.search(pattern, user_input):
	print("Valid")
else:
	print("Invalid")