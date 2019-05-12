"""
Lazy 한 Generator 함수를 사용한 Sequence 클래스

- re 모듈의 finditer 라는 function 을 활용
"""

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


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
