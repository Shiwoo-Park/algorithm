# coding=utf-8

# 8이라는 숫자를 모두 카운팅
def count8(n):
    ret = 0
    target = "8"
    for i in xrange(n):
        s = str(i)
        for c in s:
            if c == target:
                ret += 1
    return ret

def main():
    cnt = count8(10000)
    print("Count of 8 = %s \n"%cnt )
    assert cnt == 4000

main()
