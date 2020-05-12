c1,c2,c3,c4,c5,c6=[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]
p1,p2,p3,p4,p5,p6,p7,p8,p9=[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]


def sum_lis():
    s=[]
    x1,x2,x3,x4,x5,x6,x7,x8,x9=0,0,0,0,0,0,0,0,0
    while(x1<4):
        while(x2<4):
            while (x3 < 4):
                while (x4 < 4):
                    while (x5 < 4):
                        while (x6 < 4):
                            while (x7 < 4):
                                while (x8 < 4):
                                    while (x9 < 4):
                                        s.append(p1[x1]+p2[x2]+p3[x3]+p4[x4]+p5[x5]+p6[x6]+p7[x7]+p8[x8]+p9[x9])
                                        x9+=1
                                    x8+=1
                                    x9=0
                                x8=0
                                x7+=1
                            x7=0
                            x6+=1
                        x6=0
                        x5+=1
                    x5=0
                    x4+=1
                x4=0
                x3+=1
            x3=0
            x2+=1
        x2=0
        x1+=1
    return s



def sum2_lis():
    s=[]
    x1,x2,x3,x4,x5,x6=0,0,0,0,0,0
    while(x1<6):
        while (x2 < 6):
            while (x3 < 6):
                while (x4 < 6):
                    while (x5 < 6):
                        while (x6 < 6):
                            s.append(c1[x1]+c2[x2]+c3[x3]+c4[x4]+c5[x5]+c6[x6])
                            x6+=1
                        x6=0
                        x5+=1
                    x5=0
                    x4+=1
                x4=0
                x3+=1
            x3=0
            x2+=1
        x2=0
        x1+=1
    return s


a=sum_lis()
b=sum2_lis()

def check(s1,s2):
    i=0
    j=0
    p=[]
    while(i<len(s1)):
        while(j<len(s2)):
            if(s1[i]>s2[j]):    
                p.append(1)
            else:
                p.append(0)
            j+=1
        j=0
        i+=1
    return p

m=check(a,b)

print("The Probability is:",sum(m)/(len(a)+len(b)))
