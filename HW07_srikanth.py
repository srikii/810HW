'''python program using dictionaries to test if the check if anagram is present , all characters are present in the sentence and book index.
    author: srikanth'''
from collections import Counter
from collections import defaultdict
import unittest


def list_anagram(x1, x2):  # anagram using lists
    l1 = list(x1)
    l2 = list(x2)
    l1.sort()
    l2.sort()
    return l1 == l2


def defdect_anagram(x1, x2):  # anagram suing default dictionary
    dd = defaultdict(int)
    #dd2 = defaultdict(int)
    for char in x1:
        dd[char] += 1
    for char in x2:
        dd[char] -= 1
    for c in dd:
        if dd[c] != 0:
            return False
    return True


def cntr_anagram(x1, x2):  # anagram using counter
    return Counter(x1) == Counter(x2)


def covers_alplabet(sentence):  # covers all alphabet
    x = set()
    alphabets = set("abcdefghijklmnopqrstuvwxyz")
    sentence = sentence.lower()
    for c in sentence:
            if c == ' ':
                continue
            else:
                x.add(c)
    return x == alphabets


def book_index(words):  # book index using default dictionary
    index = defaultdict(set)
    result = list()
    for word, page in words:
        index[word].add(page)

    for word in sorted(index.keys()):
        result.append([word, sorted(index[word])])

    return result


class listmanupulation(unittest.TestCase):
    def test_list_anagram(self):
        self.assertEqual(list_anagram("hello", "llohe"), True)
        self.assertEqual(list_anagram("hello", "hellow"), False)

    def test_defdect_anagram(self):
        self.assertEqual(defdect_anagram("hello", "llohe"), True)
        self.assertFalse(defdect_anagram("cinema", "icemans"))

    def test_cntr_anagram(self):
        self.assertTrue(cntr_anagram("hello", "llohe"), True)

    def test_covers_alplabet(self):
        self.assertTrue(covers_alplabet(
            "The quick brown fox Jumps OVER THE LAZY DOG"))
        self.assertFalse(covers_alplabet(
            "The quick brown fox jumps over the lazy dog1"))

    def test_book_index(self):
        words = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1), ('woodchuck', 1),
                 ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2), ('could', 2), ('chuck', 1), ('wood', 1)]
        words2 = [['a', [1]], ['chuck', [1, 3]], ['could', [2]], ['how', [3]], ['if', [1]], ['much', [3]],
                  ['wood', [1, 3]], ['woodchuck', [1, 2]], ['would', [2]]]
        self.assertEqual(book_index(words), words2)


def main():

    x1 = input("anagram check\nenter the first word: ")
    x2 = input("enter second world: ")

    print(list_anagram(x1, x2))
    print(defdect_anagram(x1, x2))
    print(cntr_anagram(x1, x2))

    sentence = input("check if sentence contains all alphabets\nEnter input: ")
    print(covers_alplabet(sentence))

    words = [('how', 3), ('much', 3), ('wood', 3), ('would', 2), ('a', 1), ('woodchuck', 1),
             ('chuck', 3), ('if', 1), ('a', 1), ('woodchuck', 2), ('could', 2), ('chuck', 1), ('wood', 1)]
    x = book_index(words)
    print(x)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()