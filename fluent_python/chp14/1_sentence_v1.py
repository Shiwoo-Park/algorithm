"""
Sequence 가 반복 가능한 이유

- 인터프리터가 반복을 해야하면 항상 iter(x) 를 자동으로 호출한다.
- iter(x) 가 없고, __getitem__() 이 구현되어있으면, 자동으로 인덱스 0 부터 끝날때까지 항목을 순서대로 가져온다.
- 위 과정이 모두 실패하면 TypeError 를 발생시킨다.
"""

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)


if __name__ == '__main__':
    txt = '"The Time has come" That\'s what he said !!!'
    s = Sentence(txt)

    print("input:", txt)
    print("s[2]:", s[2])
    print("len(s):", len(s))
    print("print(s):", s)

    print("looping:")
    for elem in s:
        print(elem)
    print("list(s):", list(s))
