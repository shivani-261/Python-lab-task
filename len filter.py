words=["anjali","priyanshi","om","ashvi","ram"]
long_words=filter(lambda word:len(word)>=4,words)

print(list(long_words))
