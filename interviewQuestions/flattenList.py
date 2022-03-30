"""
Flatten a nested list

inputList = [1, [2, 3], 4, [5, [6, [7]]]]
output = [1, 2, 3, 4, 5, 6, 7]

"""

inputList = [1, [2, 3], 4, [5, [6, [7]]]]

def flatten(inp: list) -> list:
  output_list = []
  for ele in inp:
    if type(ele) == list:
      output_list += flatten(ele)
    else:
      output_list.append(ele)

  return output_list

print(flatten(inputList))