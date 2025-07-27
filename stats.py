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