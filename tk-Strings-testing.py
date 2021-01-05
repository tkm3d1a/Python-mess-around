phrase = "This is a String"
print(phrase[0])

phrase_len = len(phrase)
print(phrase_len)

count = 0

if count <= phrase_len:
    print(phrase[count])
    count = count + 1  #bad loop

count = 0

for count in phrase:
    print(count)
