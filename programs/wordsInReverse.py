# Question:
# Given a string containing a set of words separated by whitespace, we would like to transform it to a string in which the words appear in the reverse order.
# For example, "Alice likes Bob" transforms to "Bob likes Alice". We do not need to keep the original string.

# Tests to pass:
# 'Frank' returns 'Frank' (test passed)
# '' returns '' (test passed)
# 'Alice likes Bob' returns 'Bob likes Alice' (test passed)
# initially, we will ignore punctuation. So the following will be initial results:
# 'Alice, do you like Bob?' returns 'Bob? like you do Alice,' (test passed)
# ',' returns ',' (test passed)
# ', ?' returns '? ,' (test passed)


def wordInReverse(st):
    words = st.split(' ')
    string = []
    for word in words:
        string.insert(0, word)
    return " ".join(string)



statement = "Alice, do you like Bob?"
print(wordInReverse(statement))