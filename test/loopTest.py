
for i in xrange(10):
    print(i)

tests=[(1.00,'1'),
       (1.2,'1.2'),
       (221.254365633,'1.23'),
       (121.23435453456,'1.23'),
       (11.245342334545,'1.23')]

for num,answer in tests:
    result='{0:.4g}'.format(num)
    result2='{0:.4f}'.format(num)
    print result
    print result2
    print "-------------------"
    # if result != answer:
    #     print('Error: {0} --> {1} != {2}'.format(num,result,answer))
    #     exit()
    # else:
    #     print('{0} --> {1}'.format(num,result))