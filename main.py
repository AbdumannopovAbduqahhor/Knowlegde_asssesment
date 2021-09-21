# 1. Request a list of words from the user. The user input ends when an empty string is entered.
string_ = []
while True:
    words = input('Enter a word: ')
    if not words:
        break
    string_.append(words)
print(string_)

# 2. Request a single symbol X (make sure the user enters just one)
words = ['sometimes', 'rarely', 'jimmy', 'programming', 'can ', 'be']

# 3. Delete from the list those strings, which don’t contain X. Make the deletion in place without
# creating a new list.


# 4. Print the resulting list to the screen.
