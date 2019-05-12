def gen_AB():
    print("start")
    yield "A"  # 첫번째 next() 실행시, 처음부터 여기까지 실행됨

    print("continue")
    yield "B"  # 두번째 next() 실행시,

    print("end")  # 세번째 next() 실행시, 실행되고 StopIteration


print("type(gen_AB):", type(gen_AB))
print("type(gen_AB()):", type(gen_AB()))

res1 = [x * 3 for x in gen_AB()]
print(type(res1))

for c in res1:
    print("-->", c)

print("===============================")

res2 = (x * 3 for x in gen_AB())
print(type(res2))

for c in res2:
    print("-->", c)
