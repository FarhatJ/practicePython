"""
We are given a string and we need to reverse words of a given string.

Input : practice code task
Output : task code practice

"""
inp = 'practice code task'

def reverse_str(inp: str)-> str:
  string = inp.split()
  reverse_string = " ".join(reversed(string))
  return reverse_string

print(reverse_str(inp))