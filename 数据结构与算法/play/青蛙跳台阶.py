# coding=gbk
"""
������̨��
n��̨��
1�ο�����1��̨��Ҳ������2��̨��
����Ҫ������n��̨�ף��ж���������
"""
stars = int(input("�����м���̨��:\n"))
def fog(stars):
    if stars == 1:
        return 1
    elif stars == 2:
        return 2
    else:
        return fog(stars-1)+fog(stars-2)

print(f"��{fog(stars)}�ַ���")
