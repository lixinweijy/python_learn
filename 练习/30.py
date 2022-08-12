for i in range(123,988):
    bai_1=i//100
    ge_1=i%10
    shi_1=i%100//10
    if ge_1!=bai_1 and bai_1!=shi_1:
        for j in range(i+1,988):
            bai_2 = i // 100
            ge_2 = i % 10
            shi_2 = i % 100 // 10
            if ge_2 != bai_2 and bai_2 != shi_2 and bai_2!=bai_1:
                for k in range(j + 1, 988):
                    bai_3 = i // 100
                    ge_3 = i % 10
                    shi_3 = i % 100 // 10
                    if ge_3 != bai_3 and bai_3 != shi_3 and bai_2 != bai_1 and bai_3!=bai_2:
                        pass