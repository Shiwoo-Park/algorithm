import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print("SORT by value : ",sorted_x)

sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
print("SORT by value : ",sorted_x)

sorted_x = sorted(x.items(), key=operator.itemgetter(0))
print("SORT by key : ", sorted_x)