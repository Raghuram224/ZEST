name = input().lower()
word = name

word = ' '.join(word[0].upper() + word[1:] for word in word.split())
print(word)
