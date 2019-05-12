"""
Iterator Class 를 별도로 가지고 있는 버전
"""

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
            self.index += 1
            return word
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    txt = '"The Time has come" That\'s what he said !!!'
    s = Sentence(txt)

    print("input:", txt)
    print("print(s):", s)

    print("looping:")
    for elem in s:
        print(elem)
    print("list(s):", list(s))
