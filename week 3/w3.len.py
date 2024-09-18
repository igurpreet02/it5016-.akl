def function3 (word1,word2):
    len1=len(word1)
    len2=len(word2)
    shortest_lenghts= min (len1, len2)
    return shortest_lenghts

word1=input("enter word1")
word2=input("enter word2")
print(function3(word1,word2))