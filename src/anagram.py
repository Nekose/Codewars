def anagrams(word: str, words: list) -> list:
    returnlist = []
    for element in words:
        if detect_anagram(word,element) is True:
            returnlist.append(element)
    return returnlist

def detect_anagram(word1: str, word2: str) -> bool:
    word1dict = build_word_dict(word1)
    word2dict = build_word_dict(word2)
    if word1dict == word2dict:
        return True
    else:
        return False

def build_word_dict(word: str) -> dict:
    worddict = {}
    for letter in word:
        if letter in worddict:
            worddict[letter] += 1
        else:
            worddict[letter] = 1
    return worddict


testanagram = ["bob","bbo","boo","bbb"]

print(anagrams("bob",testanagram))