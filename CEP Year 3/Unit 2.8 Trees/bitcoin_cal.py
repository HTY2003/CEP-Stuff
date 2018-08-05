from math import sqrt
def cube(x):
    if 0<=x: return x**(1./3.)
    return -(-x)**(1./3.)
def cal_br3(blockheight, hashdiff):
    return cube((blockheight-4224000) + (hashdiff))
def cal_br2(blockheight, hashdiff):
    return sqrt(((blockheight-4224000) + (hashdiff)))
def cal_br4(blockheight, hashdiff):
    return sqrt(sqrt(((blockheight-4224000) + (hashdiff))))
blockbase = 499664000
blockheight = 4224000
hashdiff = 109167
inflation = []
for i in range(97):
    print(blockbase)
    for y in range(43800):
        blockheight += 1
        hashdiff += 833.333333333/43800
        blockbase += cal_br4(blockheight, hashdiff)
    if i % 12 == 0:
        inflation.append(blockbase)
for i in range(len(inflation)):
    if i != 0:
        print((inflation[i]-inflation[i-1])/inflation[i-1]*100)
