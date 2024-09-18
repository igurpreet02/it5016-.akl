def function4(word1):
    first=word1[0]
    last=word1[-1]
    combined=last+first
    return combined.upper()

word1=input("enter the word")
print(function4(word1))