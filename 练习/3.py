
# a=[4,52,15]
# a.sort()
# print(a)

# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(j,'*',i,'=',i*j,end='\t')
    print()
# # 输出100到200以内的所有素数
# for i in range(100,200):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)