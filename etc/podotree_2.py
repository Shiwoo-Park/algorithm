import sys

def getFibo(n):
    fiboNum = 0
    a = 0
    b = 1
    while n >= fiboNum:
        fiboNum = a+b
        tmp = a + b
        a = b
        b = tmp
    return fiboNum

line = sys.stdin.readline().strip()

inputCount = int(line)

if input == 0:
    exit(0)

line = sys.stdin.readline().strip()
count = 1
while line:
    print getFibo(int(line))
    if count > inputCount:
        exit(0)
    line = sys.stdin.readline().strip()
    count += 1
