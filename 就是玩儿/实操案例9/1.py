def count(a,b):
    count1=0
    for item in a:
        if b.upper()==item or b.lower()==item:
            count1+=1
    return count1
if __name__ == '__main__':
    a='woaizhouguifang,henxihuanxihuanhenxihuan,wozaiyebuyaoretashengqi'
    b=input('请输入要统计的字符：')
    print(f'{b}在{a}中出现了{count(a,b)}次')