#质数筛
import random
def binar(num):
    s_list = []
    c = num
    while(c!=0):
        b = c % 2
        c = int(c/2)
        s_list.append(b)
    return s_list
n=int(input())
for i in range(5):
    Detcet = 1
    marker = 0
    f = binar(n - 1)

    a = random.randint(2,n//2)
    while(marker!=n-1):
        marker = 2*marker
        un = Detcet
        Detcet = (Detcet*Detcet)%n
        if Detcet == 1:

            if un != 1 and un != n - 1:

                print("No")
                exit()

        g = f.pop()
        if(g ==1):

            marker=marker+1
            Detcet=(Detcet*a)%n

    if Detcet!=1:

        print("No")
        exit()

print("Yes")
