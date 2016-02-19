def read_file(path):
    # a : append
    # r : read only
    # w : write only
    # r+ : both read and write
    f = open(path, 'r')
    return f.readlines()

def read_write_file(path):
    f = open(path, 'r+')
    return f.readline()

count = 0
lines = read_file("../resources/test")
for line in lines:
    print count, line
    count += 1

