s = "ABC"

# 우리가 아는 iteration code
for c in s:
    print(c)

# 실제로 내부적으로 동작하는 iteration code
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break
