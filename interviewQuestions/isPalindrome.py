"""
Given a string. the task is to check if the string is palindrome or not.

Input: khokho
Output: The entered string is not palindrome

Input: amaama
Output: The entered string is palindrome

"""

def is_palindrome(inp: str) -> str:
  if inp == inp[::-1]:
    result = "The entered string is Palindrome"
  else:
    result = "The entered string is not Palindrome"
  return result

for s in ('khokho', 'amaama'):
  print(is_palindrome(s))