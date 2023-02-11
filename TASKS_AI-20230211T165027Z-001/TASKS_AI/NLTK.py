import nltk
sentence = 'I Love Cat'
is_noun = lambda pos: pos[:2] == 'NN'
tokenized = nltk.word_tokenize(sentence)
noun = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
sentence = sentence.replace(noun[0], 'A ' +noun[0] or ' An ' + noun[0])
print(sentence)   


