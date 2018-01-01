import sys

line = sys.stdin.readline()
lineArr = line.strip().split()

nCount = int(lineArr[0])
mCount = int(lineArr[1])

# Numbers of N
line = sys.stdin.readline()
lineArr = line.strip().split(" ")

if len(lineArr) != int(nCount):
    print("Invalid Input")
    exit(1)

numDic = dict()
for num in lineArr:
    numDic[num] = True

# Numbers of M
if not numDic:
    exit(0)

line = sys.stdin.readline().strip()
count = 1

while line:
    if line in numDic:
        print "True"
    else:
        print "False"

    if count > mCount:
        print("Invalid Input")
        exit(1)

    line = sys.stdin.readline().strip()
    count += 1


"""
30 3
146 157 150 172 104 106 148 151 169 114 178 134 165 127 139 177 192 172 132 123 124 121 131 101 189 102 161 112 184 115
177
131
205
999
151
222
169
20
139
"""
