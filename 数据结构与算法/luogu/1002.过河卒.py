#һ���ĸ����������ֱ��ʾ B �������������ꡣ
B=input("").split()
x1=int(B[0])
y1=int(B[1])
x2=int(B[2])
y2=int(B[3])
B=[x1,y1]
forbid=[[x2,y2],[x2-1,y2+2],[x2-1,y2-2],[x2-2,y2-1],[x2-2,y2+1],[x2+1,y2+2],[x2+1,y2-2],[x2+2,y2-1],[x2+2,y2+1]]
flag=0
for i in range(1,x1+1):
    pass