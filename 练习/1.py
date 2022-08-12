b=input('利润为多少：')
a=int(b)
sum=0
if a<=10:
    sum=a*1.1
elif 20>a>10:
    sum=11+(a-10)*1.075
elif 40>a>=20:
    sum=11+10.75+(a-20)*1.05
elif 60>a>=40:
    sum=21.75+21+(a-40)*1.03
elif 100>a>=60:
    sum=42.75+20.6+(a-60)*1.015
elif a>=100:
    sum=63.35+40.6+(a-100)*1.001
print(sum)
