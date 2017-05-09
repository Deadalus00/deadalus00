
#break 直接退出循环
n=1
while n<=100:   #while 条件a 
    if n >20:   #   if 条件b：
        break   #       break
    print(n)
    n=n+1
print('end')

#continue 跳过某部分迭代
n=0
while n<100:
    n=n+1
    if n % 2 == 1: # 如果n是奇数，则跳过此循环
        continue
    print(n)

#endless loop
while True:
    print('Hail to the meaningless life.')
