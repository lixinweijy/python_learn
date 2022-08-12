for i in range(123,988):
    bai_1=i//100
    ge_1=i%10
    shi_1=i%100//10
    if ge_1!=bai_1!=shi_1:
        print(i)