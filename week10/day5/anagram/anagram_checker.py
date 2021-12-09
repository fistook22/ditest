class AnagramChecker:
    def __init__(self):
        with open("sowpods.txt") as f:
            self.words = list(map(lambda s: s.strip(), f.readlines()))

    def is_valid_word(self, word):
        return word.upper() in self.words

    def get_anagrams(self, word):
        sorted_word = sorted(word)
        return list(filter(lambda x: sorted(x) == sorted_word, self.words))


ac = AnagramChecker()
# print(ac.words)