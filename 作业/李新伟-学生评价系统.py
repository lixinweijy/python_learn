#coding=gbk
name = input('请输入姓名（若输入回车、n、N则退出）\n')
while (name != '' and name != 'n' and name != 'N'):
    chinese = input('请输入你的语文分数（若输入回车、n、N则退出）\n')
    while (chinese != '' and chinese != 'n' and chinese != 'N'):
        for i in chinese:
            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                B = 1
            else:
                B = 0
                break
        if B == 0:
            print('输入错误，再来一次')
            chinese = input('请输入你的语文分数（若输入回车、n、N则退出）\n')
        else:
            a = eval(chinese)
            break
    if a == 100:
        print('满分')
    elif a > 100 or a < 0:
        print('就扯淡吧，输入有误，请手动重来')
    elif a >= 90:
        print('优秀')
    elif a >= 80:
        print('良好')
    elif a >= 70:
        print('中等')
    elif a >= 60:
        print('及格')
    else:
        print('不及格')

    math = input('请输入你的数学分数（若输入回车、n、N则退出）\n')
    while (math != '' and math != 'n' and math != 'N'):
        for i in math:
            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                B = 1
            else:
                B = 0
                break
        if B == 0:
            print('输入错误，再来一次')
            math = input('请输入你的数学分数（若输入回车、n、N则退出）\n')
        else:
            b = eval(math)
            break
    if b == 100:
        print('满分')
    elif b > 100 or b < 0:
        print('就扯淡吧，输入有误，请手动重来')
    elif b >= 90:
        print('优秀')
    elif b >= 80:
        print('良好')
    elif b >= 70:
        print('中等')
    elif b >= 60:
        print('及格')
    else:
        print('不及格')

    English = input('请输入你的英语分数（若输入回车、n、N则退出）\n')
    while (English != '' and English != 'n' and English != 'N'):
        for i in English:
            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                B = 1
            else:
                B = 0
                break
        if B == 0:
            print('输入错误，再来一次')
            English = input('请输入你的英语分数（若输入回车、n、N则退出）\n')
        else:
            c = eval(English)
            break
    if c == 100:
        print('满分')
    elif c > 100 or c < 0:
        print('就扯淡吧，输入有误，请手动重来')
    elif c >= 90:
        print('优秀')
    elif c >= 80:
        print('良好')
    elif c >= 70:
        print('中等')
    elif c >= 60:
        print('及格')
    else:
        print('不及格')

    PE = input('请输入你的体育分数（若输入回车、n、N则退出）\n')
    while (PE != '' and PE != 'n' and PE != 'N'):
        for i in PE:
            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                B = 1
            else:
                B = 0
                break
        if B == 0:
            print('输入错误，再来一次')
            PE = input('请输入你的体育分数（若输入回车、n、N则退出）\n')
        else:
            d = eval(PE)
            break
    if d == 100:
        print('满分')
    elif d > 100 or d < 0:
        print('就扯淡吧，输入有误，请手动重来')
    elif d >= 90:
        print('优秀')
    elif d >= 80:
        print('良好')
    elif d >= 70:
        print('中等')
    elif d >= 60:
        print('及格')
    else:
        print('不及格')

    labor = input('请输入你的劳动分数（若输入回车、n、N则退出）\n')
    while (labor != '' and labor != 'n' and labor != 'N'):
        for i in PE:
            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                B = 1
            else:
                B = 0
                break
        if B == 0:
            print('输入错误，再来一次')
            labor = input('请输入你的劳动分数（若输入回车、n、N则退出）\n')
        else:
            e = eval(labor)
            break
    if e == 100:
        print('满分')
    elif e > 100 or e < 0:
        print('就扯淡吧，输入有误，请手动重来')
    elif e >= 90:
        print('优秀')
    elif e >= 80:
        print('良好')
    elif e >= 70:
        print('中等')
    elif e >= 60:
        print('及格')
    else:
        print('不及格')

    draw = input('请输入你的美术分数（若输入回车、n、N则退出）\n')
    while (draw != '' and draw != 'n' and draw != 'N'):
        for i in draw:
            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                B = 1
            else:
                B = 0
                break
        if B == 0:
            print('输入错误，再来一次')
            draw = input('请输入你的美术分数（若输入回车、n、N则退出）\n')
        else:
            f = eval(draw)
            break
    if f == 100:
        print('满分')
    elif f > 100 or f < 0:
        print('就扯淡吧，输入有误，请手动重来')
    elif f >= 90:
        print('优秀')
    elif f >= 80:
        print('良好')
    elif f >= 70:
        print('中等')
    elif f >= 60:
        print('及格')
    else:
        print('不及格')

    music = input('请输入你的音乐分数（若输入回车、n、N则退出）\n')
    while (music != '' and music != 'n' and music != 'N'):
        for i in music:
            if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
                B = 1
            else:
                B = 0
                break
        if B == 0:
            print('输入错误，再来一次')
            music = input('请输入你的音乐分数（若输入回车、n、N则退出）\n')
        else:
            g = eval(music)
            break
    if g == 100:
        print('满分')
    elif g > 100 or g < 0:
        print('就扯淡吧，输入有误，请手动重来')
    elif g >= 90:
        print('优秀')
    elif g >= 80:
        print('良好')
    elif g >= 70:
        print('中等')
    elif g >= 60:
        print('及格')
    else:
        print('不及格')

    chinese_good_1 = '非常有文采,真是腹有诗书气自华。'
    chinese_good_2 = '青春正好,文采飞扬。'
    chinese_good_3 = '饱读诗书,满腹经纶。'
    math_good_1 = '逻辑思维能力非常强,继续发展下去前途一片光明。'
    math_good_2 = '数学上能洞悉题目的内涵,非常不错。'
    math_good_3 = '计算方面又快又对,非常不错。'
    English_good_1 = '英语水平很高,不过不能骄傲。'
    English_good_2 = '会一口流利的英语,非常不错。'
    English_good_3 = '英语是你的一大拉分项,希望可以保持下去。'
    PE_good_1 = '强壮的体魄,强壮的你。'
    PE_good_2 = '体育非常棒,可以考虑朝体育方面发展。'
    PE_good_3 = '健步如飞,身体壮硕,壮小伙。'
    labor_good_1 = '主动替同学们分担事情,帮助同学解决问题,很勤快。'
    labor_good_2 = '替老师分担压力,勤快主动。'
    labor_good_3 = '动手能力很强,自己的事情按时保量的完成。'
    draw_good_1 = '画画也画的太逼真了,能送老师一幅吗。'
    draw_good_2 = '给你一支画笔,你能给别人一个世界。'
    draw_good_3 = '手指间画笔转动,不一会儿,一幅栩栩如生的画作便能出现在我们眼中。'
    music_good_1 = '有一副被天使亲吻过的嗓子,唱歌非常好听。'
    music_good_2 = '歌声令人陶醉,可以朝这个方向发展。'
    music_good_3 = '仿佛为唱歌而生,声音可以感染别人。'

    chinese_bad_1 = '需要多喝点墨水哦,要更有文采才行。'
    chinese_bad_2 = '平时注意要多看看文学作品,丰富自己的学识,扩充自己的知识面。'
    chinese_bad_3 = '诗词什么的需要多记,这不仅对答题有利,还有利于充实你的大脑,提高你的文采。'
    math_bad_1 = '要多刷刷题,锻炼数学思维。'
    math_bad_2 = '数学要掌握技巧,搞清楚题目与题目之间的共同点,那样解题才能事半功倍。'
    math_bad_3 = '数学要理解知识点,不能死记公式,那样才能理解题目,做题时有思路。'
    English_bad_1 = '英语方面要多花花课余时间记单词,读文章。'
    English_bad_2 = '英语方面要注意语法语态,分清楚时态,不要混淆了。'
    English_bad_3 = '学习英语需要花费很多时间的,也更需要持之以恒,你那样做的话迟早会成为一个英语大佬的。'
    PE_bad_1 = '不要老呆在寝室里,电脑前,多出去运动运动。'
    PE_bad_2 = '体质不行呀,要不要时间多和老师我出去打打球。'
    PE_bad_3 = '要多跑跑步,锻炼锻炼身体,保持身心健康才行。'
    labor_bad_1 = '年轻人不要懒哦。'
    labor_bad_2 = '要自己的事情自己做,锻炼自己的动手能力。'
    labor_bad_3 = '要从小事开始,从自己的事开始,自己着手完成每一件事。'
    draw_bad_1 = '画画么,多画就有了。'
    draw_bad_2 = '画画有很多技巧的,多花功夫掌握了你一定会成功的。'
    draw_bad_3 = '画画方面的话可以在网上找一些视频多多学习,掌握技巧了之后你的画技肯定会更上一层楼的。'
    music_bad_1 = '多跟着老师学,注意技巧,迟早会唱好听的。'
    music_bad_2 = '平时多多练习,不要放着天籁的嗓子不用。'
    music_bad_3 = '五音不全么,实在不行放弃吧/捂脸。'

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

    average = '成绩均衡发展，没有偏科，很不错，要是有优势学科就更好了，现在需要保持各学科，发展优势学科。'
    bad = '人生在世，总还是有需要努力和发展的地方，不能贪图享乐，要有目标和追求，现在就出发去努力吧，少年!'
    good = '各科都非常优秀，平时非常勤奋努力，努力没有白费，加油少年！'

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
        x = '学习标兵'
    elif 420 <= h < 560:
        x = '优秀学生'
    elif 300 <= h < 420:
        x = '普通学生'
    else:
        x = '差生'

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
    print('{}同学，你的成绩是\n语文:{}  数学:{}  英语:{}  体育:{}  劳动:{}  美术:{}  音乐:{}  总分:{}'.format(name, a, b, c, d, e, f, g, h),
          '\n学生水平:{}'.format(x))
    print('老师评语:{}{}{}{}{}{}{}{}{}{}\n'.format(a1, b1, c1, d1, e1, f1, g1, h1, i1, j1))
    name = input('请输入姓名（若输入回车、n、N则退出）\n')
print('评价结束')