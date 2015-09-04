sample = ["abba", 'abab', 'capp', 'ddid', 'dddi', 'bbaa', 'eheh', 'hehe']


def anagram_group(words):
    anagrams = {}
    for word in words:
        anagram_key = "".join(sorted(word))
        anagrams.setdefault(anagram_key, []).append(word)
    return anagrams

print anagram_group(sample)
