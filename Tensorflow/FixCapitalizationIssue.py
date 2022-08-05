##Exercise 95: Capitalize It
""""
Many people do not use capital letters correctly, especially when typing on small
devices like smart phones. To help address this situation, you will create a function
that takes a string as its only parameter and returns a new copy of the string that has
been correctly capitalized. In particular, your function must:
• Capitalize the first non-space character in the string,
• Capitalize the first non-space character after a period, exclamation mark or question
mark, and
• Capitalize a lowercase “i” if it is preceded by a space and followed by a space,
period, exclamation mark, question mark or apostrophe.
Implementing these transformations will correct most capitalization errors. For
example, if the function is provided with the string “what time do i have to be there?
what’s the address? this time i’ll try to be on time!” then it should return the string
“What time do I have to be there? What’s the address? This time I’ll try to be on
time!”. Include a main program that reads a string from the user, capitalizes it using
your function, and displays the result.
"""


def fixCapitalizationIssue(givenString):
    listOfSentences = []
    for i in givenString:
        if i in ['!', '?', '.']:
            listOfSentences.append(givenString[0:givenString.index(i) + 1])
            givenString = givenString[givenString.index(i) + 2:]
    newList = []
    for sentence in listOfSentences:
        for x in [sentence.capitalize().split(' ')]:
            for y in x:
                if y == 'i':
                    x[x.index(y)] = 'I'
                elif y == 'i’ll':
                    x[x.index(y)] = 'I’ll'
            newList.append(" ".join(x))
    return " ".join(newList)


if __name__ == "__main__":
    sentence = input()
    fixCapitalizationIssue(sentence)
