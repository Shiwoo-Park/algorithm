"""
Generator 함수를 사용한 Sequence 클래스

- __iter__() 를 보자
- StopIteration 을 직접 발생시킬 필요 X
- 별도의 반복자 Class 필요 X
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
        for word in self.words:
            yield word
        return iter(self.words)


if __name__ == '__main__':
    txt = '"The Time has come" That\'s what he said !!!'

    txt = 'a b c'
    s = Sentence(txt)

    print("input:", txt)
    print("print(s):", s)

    print("looping:")
    for elem in s:
        print(elem)
    print("list(s):", list(s))

    it = iter(s)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
