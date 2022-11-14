from matplotlib import pyplot as plt
import math
import numpy as np

def f(sign):
    #change path as required
    with open("C://Users//sapam//Desktop//PYPY//m1" + sign + "m2//v1.txt", "r") as v_1:
        data_v1 = [float(x) for x in v_1.read().split("\n")]
    with open("C://Users//sapam//Desktop//PYPY//m1" + sign + "m2//vd.txt", "r") as v_d:
        data_vd = [float(x) for x in v_d.read().split("\n")]
    res = [i / j for i, j in zip(data_vd, data_v1)]
    #print(res)

    def avg(ls):
        n = len(ls)
        if n <= 1:
            return ls[0]
        return sum(ls)/float(n)

    def std(data):
        n = len(data)
        if n <= 1:
            return 0.0
        sd = 0.0
        for el in data:
            sd += (float(el) - avg(data))**2
        return math.sqrt(sd / float(n-1))
    
    print()
    print(chr(92)+"item", "Average of data is " + str(round(avg(res),3)))
    print(chr(92)+"item", "SD of data is " + str(round(std(res),3)))
    
    outc, outc2 = 0, 0
    av, sd = avg(res), std(res)
    for r in res:
        if r < av-sd or r > av+sd:
            outc += 1
            if r < av-2*sd or r > av+2*sd:
                outc2 += 1

    #print(outc, outc2, len(res))
    print(chr(92)+"item", "Fraction Data outside average +/- SD: " + str(round(outc/len(res),3)))
    print(chr(92)+"item", "Fraction Data outside average +/- 2xSD: " + str(round(outc2/len(res),3)))


    a = np.array(res)
    fig, ax = plt.subplots(figsize =(10, 7))
    #ax.hist(a, bins = [0.43,0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5])
    #ax.hist(a, bins = [0.47, 0.48, 0.49, 0.50, 0.51, 0.52, 0.53, 0.54])
    #plt.show()

for i in ["=", "lt", "gt"]:
    f(i)