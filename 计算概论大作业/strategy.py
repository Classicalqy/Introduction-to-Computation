#2300011447 陈启钰 计算概论大作业
import pandas as pd
def f1(p,w):#截取序列
        p1=[]
        l=len(p)
        if l<w:
            p1=p
        else:
            p1=p[l-w:l]
        return p1

def aver(p):#计算平均值
        return sum(p)/len(p) if len(p)>0 else 0

def turtle(price, w):
    ans=[0]
    for i in range (1,len(price)):
        a=f1(price[0:i+1],w)
        maxn=a[0]
        minn=a[0]
        for j in range(0,len(a)-1):#算出区间最大值和最小值
            maxn=max(maxn,a[j])
            minn=min(minn,a[j])
        if a[len(a)-1]>maxn:
            ans.append(-1)
        elif a[len(a)-1]<minn:
            ans.append(1)
        else:
            ans.append(0)
    return ans

def movingaverage(price, sw, lw):
    ans=[0]
    for i in range(1,len(price)):
        smat1=aver(f1(price[0:i],sw))#把四个参数都计算出来
        smat2=aver(f1(price[0:i+1],sw))
        lmat1=aver(f1(price[0:i],lw))
        lmat2=aver(f1(price[0:i+1],lw))
        if smat1<lmat1 and smat2>lmat2:
            ans.append(-1)
        elif smat1>lmat1 and smat2<lmat2:
            ans.append(1)
        else:
            ans.append(0)
    return ans    

def abcd(price, w, skip_loop):
    ans=[0]
    ma=[]
    def jiaoji(x,y):#以下是两个有关集合运算的函数
        return list(set(x)&set(y))
    def jianfa(x,y):
        return list(set(x)-set(y))
    for i in range(0,len(price)):
        ma.append(aver(f1(price[0:i+1],w)))
    A=[]
    B=[]
    C=[]
    D=[]
    for a in range(len(price)):#开始遍历
        A.append(a)
        for b in range(a,len(price),skip_loop):
            if ma[b]>ma[a]:
                B.append(b)
                for c in range(b,len(price),skip_loop):
                    if ma[c]<ma[b] and ma[c]>ma[a]:
                        C.append(c)
                        for d in range(c,len(price),skip_loop):
                            if ma[d]>ma[b]:
                                D.append(d)
    for i in range(1,len(price)):#判断
        k=0
        if i in jianfa(jiaoji(A,C),jiaoji(B,D)):
            k+=1
        if i in jianfa(jiaoji(B,D),jiaoji(A,C)):
            k-=1
        ans.append(k)
    return ans

def diy(price, w, arg2=None, arg3=None, arg4=None):
    ans=[0]
    for i in range(1,len(price)):
        judge1=1#这两个参量用来判断一个区间是否一直增大或者一直减小
        judge2=1
        if i<w:
            ans.append(0)
        else:
            for j in range(0,w):
                if price[i-j]<price[i-j-1]:
                    judge1=0
                if price[i-j]>price[i-j-1]:
                    judge2=0
            if judge1==1:
                ans.append(-1)
            elif judge2==1:
                ans.append(1)
            else:
                ans.append(0)
    return ans
