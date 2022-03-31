"""
Replace variable markers with values from dictionary.
Write a function that takes a string and a dictionary as input.
The string will be like Hello <name> and the function will return Hello value
where value is the mapping of character in the dictionary. 

"""

import typing
import re

def templatize(template : str, variables: typing.Dict[str,any]) -> str:
    tmList=[]
    for line in template.split(' '):
        pattern=re.findall(r'<\w.+?>',line)
        if pattern:
            tmList.append(pattern)
    tmList=[item for sublist in tmList for item in sublist]
    for item in tmList:
        key=item[1:-1]
        value=variables[key]
        template=template.replace(item,str(value))
    return template
        
# Key is the template, value is the expected output
variables={
    "name": "Mars",
    "pet": "dog",
    "age": 22, 
}

# Test cases.  Key is the template, value is the expected output
test_cases={
    "Hello <name>!" : "Hello Mars!",
    "Good day, <name>. You look happy <name>": "Good day, Mars. You look happy Mars",
    "Good day, Miss": "Good day, Miss",
    "Hello <name>. How is your <pet>": "Hello Mars. How is your dog",
    "Hello <name>! I am <age>": "Hello Mars! I am 22",
    "Hello <name! I am <age>":"Hello <name! I am 22",
    "Hello <name!": "Hello <name!",
    "Hello name>! I am <age>":"Hello name>! I am 22", 
    "Hello <<name>>!" : "Hello <Mars>!",
}

for template,output in test_cases.items():
      rendered=templatize(template,variables)
      assert rendered == output, f'Expected "{output}" got "{rendered}"'

print("All tests pass")
