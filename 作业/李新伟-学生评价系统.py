#coding=gbk
name = input('������������������س���n��N���˳���\n')
while (name != '' and name != 'n' and name != 'N'):
    chinese = input('������������ķ�����������س���n��N���˳���\n')
    while (chinese != '' and chinese != 'n' and chinese != 'N'):
        for i in chinese:
            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                B = 1
            else:
                B = 0
                break
        if B == 0:
            print('�����������һ��')
            chinese = input('������������ķ�����������س���n��N���˳���\n')
        else:
            a = eval(chinese)
            break
    if a == 100:
        print('����')
    elif a > 100 or a < 0:
        print('�ͳ����ɣ������������ֶ�����')
    elif a >= 90:
        print('����')
    elif a >= 80:
        print('����')
    elif a >= 70:
        print('�е�')
    elif a >= 60:
        print('����')
    else:
        print('������')

    math = input('�����������ѧ������������س���n��N���˳���\n')
    while (math != '' and math != 'n' and math != 'N'):
        for i in math:
            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                B = 1
            else:
                B = 0
                break
        if B == 0:
            print('�����������һ��')
            math = input('�����������ѧ������������س���n��N���˳���\n')
        else:
            b = eval(math)
            break
    if b == 100:
        print('����')
    elif b > 100 or b < 0:
        print('�ͳ����ɣ������������ֶ�����')
    elif b >= 90:
        print('����')
    elif b >= 80:
        print('����')
    elif b >= 70:
        print('�е�')
    elif b >= 60:
        print('����')
    else:
        print('������')

    English = input('���������Ӣ�������������س���n��N���˳���\n')
    while (English != '' and English != 'n' and English != 'N'):
        for i in English:
            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                B = 1
            else:
                B = 0
                break
        if B == 0:
            print('�����������һ��')
            English = input('���������Ӣ�������������س���n��N���˳���\n')
        else:
            c = eval(English)
            break
    if c == 100:
        print('����')
    elif c > 100 or c < 0:
        print('�ͳ����ɣ������������ֶ�����')
    elif c >= 90:
        print('����')
    elif c >= 80:
        print('����')
    elif c >= 70:
        print('�е�')
    elif c >= 60:
        print('����')
    else:
        print('������')

    PE = input('�������������������������س���n��N���˳���\n')
    while (PE != '' and PE != 'n' and PE != 'N'):
        for i in PE:
            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                B = 1
            else:
                B = 0
                break
        if B == 0:
            print('�����������һ��')
            PE = input('�������������������������س���n��N���˳���\n')
        else:
            d = eval(PE)
            break
    if d == 100:
        print('����')
    elif d > 100 or d < 0:
        print('�ͳ����ɣ������������ֶ�����')
    elif d >= 90:
        print('����')
    elif d >= 80:
        print('����')
    elif d >= 70:
        print('�е�')
    elif d >= 60:
        print('����')
    else:
        print('������')

    labor = input('����������Ͷ�������������س���n��N���˳���\n')
    while (labor != '' and labor != 'n' and labor != 'N'):
        for i in PE:
            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                B = 1
            else:
                B = 0
                break
        if B == 0:
            print('�����������һ��')
            labor = input('����������Ͷ�������������س���n��N���˳���\n')
        else:
            e = eval(labor)
            break
    if e == 100:
        print('����')
    elif e > 100 or e < 0:
        print('�ͳ����ɣ������������ֶ�����')
    elif e >= 90:
        print('����')
    elif e >= 80:
        print('����')
    elif e >= 70:
        print('�е�')
    elif e >= 60:
        print('����')
    else:
        print('������')

    draw = input('�������������������������س���n��N���˳���\n')
    while (draw != '' and draw != 'n' and draw != 'N'):
        for i in draw:
            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                B = 1
            else:
                B = 0
                break
        if B == 0:
            print('�����������һ��')
            draw = input('�������������������������س���n��N���˳���\n')
        else:
            f = eval(draw)
            break
    if f == 100:
        print('����')
    elif f > 100 or f < 0:
        print('�ͳ����ɣ������������ֶ�����')
    elif f >= 90:
        print('����')
    elif f >= 80:
        print('����')
    elif f >= 70:
        print('�е�')
    elif f >= 60:
        print('����')
    else:
        print('������')

    music = input('������������ַ�����������س���n��N���˳���\n')
    while (music != '' and music != 'n' and music != 'N'):
        for i in music:
            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                B = 1
            else:
                B = 0
                break
        if B == 0:
            print('�����������һ��')
            music = input('������������ַ�����������س���n��N���˳���\n')
        else:
            g = eval(music)
            break
    if g == 100:
        print('����')
    elif g > 100 or g < 0:
        print('�ͳ����ɣ������������ֶ�����')
    elif g >= 90:
        print('����')
    elif g >= 80:
        print('����')
    elif g >= 70:
        print('�е�')
    elif g >= 60:
        print('����')
    else:
        print('������')

    chinese_good_1 = '�ǳ����Ĳ�,���Ǹ���ʫ�����Ի���'
    chinese_good_2 = '�ഺ����,�Ĳɷ��'
    chinese_good_3 = '����ʫ��,�������ڡ�'
    math_good_1 = '�߼�˼ά�����ǳ�ǿ,������չ��ȥǰ;һƬ������'
    math_good_2 = '��ѧ���ܶ�Ϥ��Ŀ���ں�,�ǳ�����'
    math_good_3 = '���㷽���ֿ��ֶ�,�ǳ�����'
    English_good_1 = 'Ӣ��ˮƽ�ܸ�,�������ܽ�����'
    English_good_2 = '��һ��������Ӣ��,�ǳ�����'
    English_good_3 = 'Ӣ�������һ��������,ϣ�����Ա�����ȥ��'
    PE_good_1 = 'ǿ׳������,ǿ׳���㡣'
    PE_good_2 = '�����ǳ���,���Կ��ǳ��������淢չ��'
    PE_good_3 = '�������,����׳˶,׳С�'
    labor_good_1 = '������ͬѧ�Ƿֵ�����,����ͬѧ�������,���ڿ졣'
    labor_good_2 = '����ʦ�ֵ�ѹ��,�ڿ�������'
    labor_good_3 = '����������ǿ,�Լ������鰴ʱ��������ɡ�'
    draw_good_1 = '����Ҳ����̫������,������ʦһ����'
    draw_good_2 = '����һ֧����,���ܸ�����һ�����硣'
    draw_good_3 = '��ָ�仭��ת��,��һ���,һ�����������Ļ������ܳ������������С�'
    music_good_1 = '��һ������ʹ���ǹ���ɤ��,����ǳ�������'
    music_good_2 = '������������,���Գ��������չ��'
    music_good_3 = '�·�Ϊ�������,�������Ը�Ⱦ���ˡ�'

    chinese_bad_1 = '��Ҫ��ȵ�īˮŶ,Ҫ�����Ĳɲ��С�'
    chinese_bad_2 = 'ƽʱע��Ҫ�࿴����ѧ��Ʒ,�ḻ�Լ���ѧʶ,�����Լ���֪ʶ�档'
    chinese_bad_3 = 'ʫ��ʲô����Ҫ���,�ⲻ���Դ�������,�������ڳ�ʵ��Ĵ���,�������Ĳɡ�'
    math_bad_1 = 'Ҫ��ˢˢ��,������ѧ˼ά��'
    math_bad_2 = '��ѧҪ���ռ���,�������Ŀ����Ŀ֮��Ĺ�ͬ��,������������°빦����'
    math_bad_3 = '��ѧҪ���֪ʶ��,�������ǹ�ʽ,�������������Ŀ,����ʱ��˼·��'
    English_bad_1 = 'Ӣ�﷽��Ҫ�໨������ʱ��ǵ���,�����¡�'
    English_bad_2 = 'Ӣ�﷽��Ҫע���﷨��̬,�����ʱ̬,��Ҫ�����ˡ�'
    English_bad_3 = 'ѧϰӢ����Ҫ���Ѻܶ�ʱ���,Ҳ����Ҫ��֮�Ժ�,���������Ļ�������Ϊһ��Ӣ����еġ�'
    PE_bad_1 = '��Ҫ�ϴ���������,����ǰ,���ȥ�˶��˶���'
    PE_bad_2 = '���ʲ���ѽ,Ҫ��Ҫʱ������ʦ�ҳ�ȥ�����'
    PE_bad_3 = 'Ҫ�����ܲ�,������������,�������Ľ������С�'
    labor_bad_1 = '�����˲�Ҫ��Ŷ��'
    labor_bad_2 = 'Ҫ�Լ��������Լ���,�����Լ��Ķ���������'
    labor_bad_3 = 'Ҫ��С�¿�ʼ,���Լ����¿�ʼ,�Լ��������ÿһ���¡�'
    draw_bad_1 = '����ô,�໭�����ˡ�'
    draw_bad_2 = '�����кܶ༼�ɵ�,�໨������������һ����ɹ��ġ�'
    draw_bad_3 = '��������Ļ�������������һЩ��Ƶ���ѧϰ,���ռ�����֮����Ļ����϶������һ��¥�ġ�'
    music_bad_1 = '�������ʦѧ,ע�⼼��,����ᳪ�����ġ�'
    music_bad_2 = 'ƽʱ�����ϰ,��Ҫ����������ɤ�Ӳ��á�'
    music_bad_3 = '������ȫô,ʵ�ڲ��з�����/������'

    A = 0
    A1 = 0
    B = 0
    B1 = 0
    C = 0
    C1 = 0
    D = 0
    D1 = 0
    E = 0
    E1 = 0
    F = 0
    F1 = 0
    G = 0
    G1 = 0

    if a >= 90:
        A = 1
        if a - 90 == 0 or a - 90 == 1 or a - 90 == 4 or a - 90 == 7:
            a1 = chinese_good_1
        elif a - 90 == 3 or a - 90 == 6 or a - 90 == 9:
            a1 = chinese_good_2
        else:
            a1 = chinese_good_3
    elif a < 60:
        A1 = -1
        if a - 20 < 0:
            a1 = chinese_bad_1
        elif a - 40 < 0:
            a1 = chinese_bad_2
        else:
            a1 = chinese_bad_3
    else:
        a1 = ''

    if b >= 90:
        B = 1
        if b - 90 == 0 or b - 90 == 1 or b - 90 == 4 or b - 90 == 7:
            b1 = math_good_1
        elif b - 90 == 3 or b - 90 == 6 or b - 90 == 9:
            b1 = math_good_2
        else:
            b1 = math_good_3
    elif b < 60:
        B1 = -1
        if b - 20 < 0:
            b1 = math_bad_1
        elif b - 40 < 0:
            b1 = math_bad_2
        else:
            b1 = math_bad_3
    else:
        b1 = ''

    if c >= 90:
        C = 1
        if c - 90 == 0 or c - 90 == 1 or c - 90 == 4 or c - 90 == 7:
            c1 = English_good_1
        elif c - 90 == 3 or c - 90 == 6 or c - 90 == 9:
            c1 = English_good_2
        else:
            c1 = English_good_3
    elif c < 60:
        C1 = -1
        if c - 20 < 0:
            c1 = English_bad_1
        elif c - 40 < 0:
            c1 = English_bad_2
        else:
            c1 = English_bad_3
    else:
        c1 = ''

    if d >= 90:
        D = 1
        if d - 90 == 0 or d - 90 == 1 or d - 90 == 4 or d - 90 == 7:
            d1 = PE_good_1
        elif d - 90 == 3 or d - 90 == 6 or d - 90 == 9:
            d1 = PE_good_2
        else:
            d1 = PE_good_3
    elif d < 60:
        D1 = -1
        if d - 20 < 0:
            d1 = PE_bad_1
        elif d - 40 < 0:
            d1 = PE_bad_2
        else:
            d1 = PE_bad_3
    else:
        d1 = ''

    if e >= 90:
        E = 1
        if e - 90 == 0 or e - 90 == 1 or e - 90 == 4 or e - 90 == 7:
            e1 = labor_good_1
        elif e - 90 == 3 or e - 90 == 6 or e - 90 == 9:
            e1 = labor_good_2
        else:
            e1 = labor_good_3
    elif e < 60:
        E1 = -1
        if e - 20 < 0:
            e1 = labor_bad_1
        elif e - 40 < 0:
            e1 = labor_bad_2
        else:
            e1 = labor_bad_3
    else:
        e1 = ''

    if f >= 90:
        F = 1
        if f - 90 == 0 or f - 90 == 1 or f - 90 == 4 or f - 90 == 7:
            f1 = draw_good_1
        elif f - 90 == 3 or f - 90 == 6 or f - 90 == 9:
            f1 = draw_good_2
        else:
            f1 = draw_good_3
    elif f < 60:
        F1 = -1
        if f - 20 < 0:
            f1 = draw_bad_1
        elif f - 40 < 0:
            f1 = draw_bad_2
        else:
            f1 = draw_bad_3
    else:
        f1 = ''

    if g >= 90:
        G = 1
        if g - 90 == 0 or g - 90 == 1 or g - 90 == 4 or g - 90 == 7:
            g1 = music_good_1
        elif g - 90 == 3 or g - 90 == 6 or g - 90 == 9:
            g1 = music_good_2
        else:
            g1 = music_good_3
    elif g < 60:
        G1 = -1
        if g - 20 < 0:
            g1 = music_bad_1
        elif g - 40 < 0:
            g1 = music_bad_2
        else:
            g1 = music_bad_3
    else:
        g1 = ''

    average = '�ɼ����ⷢչ��û��ƫ�ƣ��ܲ���Ҫ��������ѧ�ƾ͸����ˣ�������Ҫ���ָ�ѧ�ƣ���չ����ѧ�ơ�'
    bad = '�����������ܻ�������ҪŬ���ͷ�չ�ĵط�������̰ͼ���֣�Ҫ��Ŀ���׷�����ھͳ���ȥŬ���ɣ�����!'
    good = '���ƶ��ǳ����㣬ƽʱ�ǳ��ڷ�Ŭ����Ŭ��û�а׷ѣ��������꣡'

    if 90 > a >= 60 and 90 > b >= 60 and 90 > c >= 60 and 90 > d >= 60 and 90 > e >= 60 and 90 > f >= 60 and 90 > g >= 60:
        h1 = average
    else:
        h1 = ''

    if a >= 90 and b >= 90 and c >= 90 and d >= 90 and e >= 90 and f >= 90 and g >= 90:
        i1 = good
    else:
        i1 = ''

    if a < 60 and b < 60 and c < 60 and d < 60 and e < 60 and f < 60 and g < 60:
        j1 = average
    else:
        j1 = ''

    h = a + b + c + d + e + f + g
    if h >= 560:
        x = 'ѧϰ���'
    elif 420 <= h < 560:
        x = '����ѧ��'
    elif 300 <= h < 420:
        x = '��ͨѧ��'
    else:
        x = '����'

    H = A + B + C + D + E + F + G
    H1 = A1 + B1 + C1 + D1 + E1 + F1 + G1

    if H == 4:
        if A + B + C + D > 2:
            if a1 != '':
                a1 = ''
            if b1 != '':
                b1 = ''
        else:
            if e1 != '':
                e1 = ''
            if f1 != '':
                f1 = ''
    if H == 5:
        if A + B + C + D + E > 3:
            if a1 != '':
                a1 = ''
            if c1 != '':
                c1 = ''
            if d1 != '':
                d1 = ''
        else:
            if b1 != '':
                b1 = ''
            if f1 != '':
                f1 = ''
            if g1 != '':
                g1 = ''
    if H == 6:
        if A + B + C + D + E + F > 4:
            if a1 != '':
                a1 = ''
            if c1 != '':
                c1 = ''
            if d1 != '':
                d1 = ''
            if f1 != '':
                f1 = ''
    if H == 7:
        b1 = ''
        d1 = ''
        f1 = ''
        g1 = ''

    if H1 == -4:
        if A + B + C + D < -2:
            if a1 != '':
                a1 = ''
            if b1 != '':
                b1 = ''
        else:
            if e1 != '':
                e1 = ''
            if f1 != '':
                f1 = ''
    if H1 == -5:
        if A + B + C + D + E < -3:
            if a1 != '':
                a1 = ''
            if c1 != '':
                c1 = ''
            if d1 != '':
                d1 = ''
        else:
            if b1 != '':
                b1 = ''
            if f1 != '':
                f1 = ''
            if g1 != '':
                g1 = ''
    if H1 == -6:
        if A + B + C + D + E + F < -4:
            if a1 != '':
                a1 = ''
            if c1 != '':
                c1 = ''
            if d1 != '':
                d1 = ''
            if f1 != '':
                f1 = ''
    if H1 == -7:
        b1 = ''
        d1 = ''
        f1 = ''
        g1 = ''
        a1 = ''
        e1 = ''
    print('{}ͬѧ����ĳɼ���\n����:{}  ��ѧ:{}  Ӣ��:{}  ����:{}  �Ͷ�:{}  ����:{}  ����:{}  �ܷ�:{}'.format(name, a, b, c, d, e, f, g, h),
          '\nѧ��ˮƽ:{}'.format(x))
    print('��ʦ����:{}{}{}{}{}{}{}{}{}{}\n'.format(a1, b1, c1, d1, e1, f1, g1, h1, i1, j1))
    name = input('������������������س���n��N���˳���\n')
print('���۽���')