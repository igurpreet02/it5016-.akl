def count_vowels(text):
    vowels="aeious"
    count=0

    for character in text:
        if character.lower()in vowels:
            count +=1
    return count
def main():
    text=input("enter the text:")
    vowelscount=count_vowels(text)
    print(f"number of vowels in {text}:{vowelscount}")

main()