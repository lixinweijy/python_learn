# 新知识点2：文件应用
# 文件操作 https://www.runoob.com/python/file-methods.html
# fo = open('商品目录.txt', "w", encoding='utf-8')
# d={'0908998786': '思想与品德（第二版）',  '8886549088': ['模拟电子技术', 66]}
# fo.write(str(d))
# fo.close()

# 文本文件的读取 https://www.cnblogs.com/feigebaqi/p/9560370.html
fi = open('商品目录.txt', 'r', encoding='utf-8')
txt=fi.readlines()
print(txt)
fi.close()