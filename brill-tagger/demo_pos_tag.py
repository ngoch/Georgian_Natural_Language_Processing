import nltk

text = nltk.word_tokenize("And now for something completely different")
print(nltk.pos_tag(text))
