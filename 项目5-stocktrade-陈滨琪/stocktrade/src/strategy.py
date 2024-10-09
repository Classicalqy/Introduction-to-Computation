import pandas as pd

def turtle(price, w):
    # TODO:实现海龟策略，不要对函数名和参数列表进行修改
    l=len(price)
    price1=[]
    k=0
    if w<=l-1:
        for i in range(0,w):
            price1.append(price[l-1-w+i])
    else:
        for i in range(0,l-1):
            price1.append(price[i])
    maxn=float(price1[0])
    minn=maxn
    for i in range(0,len(price1)):
        maxn=max(maxn,float(price1[i]))
        minn=min(minn,float(price1[i]))
    if minn>float(price[l-1]):
        k+=1
    if maxn<float(price[l-1]):
        k-=1
    return k

def movingaverage(price, sw, lw):
    # TODO:实现均线策略，不要对函数名和参数列表进行修改
    pass

def abcd(price, w, skip_loop):
    # TODO:实现abcd策略，不要对函数名和参数列表进行修改
    pass

def diy(price, arg1=None, arg2=None, arg3=None, arg4=None):
    # TODO:实现diy策略，可以自行增加或删除参数，但不要更改函数名
    pass
