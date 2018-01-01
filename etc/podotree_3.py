import sys

# 1st Array
line = sys.stdin.readline().strip()
arr1Count = int(line)

line = sys.stdin.readline()
arr1 = line.strip().split()

if len(arr1) != arr1Count:
    print("Invalid input")
    exit(1)

# 2nd Array
line = sys.stdin.readline().strip()
arr2Count = int(line)

line = sys.stdin.readline()
arr2 = line.strip().split()

if len(arr2) != arr2Count:
    print("Invalid input")
    exit(1)

# Kth
k = sys.stdin.readline()
if not k:
    print("Invalid input")
    exit(1)

k = int(k.strip())
if k > arr1Count + arr2Count:
    print("Invalid input")
    exit(1)

counter = 0
arr1Index = 0
arr2Index = 0
smallNum = None
while counter < k:
    if arr1Index < arr1Count:
        n1 = int(arr1[arr1Index])
    if arr2Index < arr2Count:
        n2 = int(arr2[arr2Index])
    if arr1Index < arr1Count and arr2Index < arr2Count:
        if n1 > n2:
            smallNum = n2
            arr2Index += 1
        else:
            smallNum = n1
            arr1Index += 1
    else:
        if arr1Index < arr1Count:
            smallNum = n1
            arr1Index += 1
        else:
            smallNum = n2
            arr2Index += 1
    counter += 1
    print "COUNTER : %s"%(counter)
    print "INDEX : %s/%s, %s/%s"%(arr1Index, arr1Count, arr2Index , arr2Count)
    print "smallNum : ",smallNum
    print ""

print smallNum