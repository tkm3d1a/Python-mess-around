phrase = "This is a String"
print(phrase[0])

phrase_len = len(phrase)
print(phrase_len)

count = 0

if count <= phrase_len:
    print(phrase[count])
    count = count + 1  # bad loop

count = 0

for count in phrase:  # will print the letters one by one, new line for each print
    print(count)


# below is a bad implementation, doesnt even do anything.  don't know syntax for shit...
# count = 0
# newPhrase = ""
#
# for count in phrase_len:
#     newPhrase = newPhrase + phrase[count]
#     print(newPhrase)