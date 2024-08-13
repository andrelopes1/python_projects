def print_some_characters(word):
  for i in range(len(word)):
    if i % 2 == 0:
      print(word[i])

print_some_characters("watermelon")