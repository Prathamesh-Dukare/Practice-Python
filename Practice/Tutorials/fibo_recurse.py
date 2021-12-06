import time
t1=time.time()
def main(n):
    for i in range(n+1):
        def fibo(x):
            if(x==0):
                return 0
            elif(x==1):
                return 1
            else:
                return fibo(x-1)+fibo(x-2)
        print(fibo(i),end=' ')
num=int(input())
main(num)
t2=time.time()
print('\n',t2-t1)