def word_count(text):
    wordcount = len(text.split())
    return wordcount

def letter_count(text):
    lettercount={}
    for letter in text:
        lower_case_letter = letter.lower()
        if lower_case_letter not in lettercount:
            lettercount[lower_case_letter] = 1
        else:
            lettercount[lower_case_letter] += 1
    return lettercount

def sort_on(items):
    return items["num"]

def sorted_letter_count(dictionary):
    sorted_letters = []
    for char, num in dictionary.items():
        if char.isalpha():
            sorted_letters.append({"char":char,"num":num})
    sorted_letters.sort(reverse=True,key=sort_on)
    return sorted_letters