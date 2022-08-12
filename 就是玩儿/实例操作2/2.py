print('--------(1)---------')
print('➊   林黛玉')
print('➋   薛宝钗')
print('➌   贾元春')
print('➍   贾探春')
print('➎   史湘云')
print('--------(2)---------')
name1='林黛玉'
name2='薛宝钗'
name3='贾元春'
name4='贾探春'
name5='史湘云'
print('➊\t'+name1)
print('➋\t'+name2)
print('➌\t'+name3)
print('➍\t'+name4)
print('➎\t'+name5)
print('--------(3)---------')
name=['林黛玉','薛宝钗','贾元春','贾探春','史湘云']
num=['➊','➋','➌','➍','➎']
for i in range(5):
    print(num[i],name[i])
print('--------(4)---------')
d={'➊':'林黛玉','➋':'薛宝钗','➌':'贾元春','➍':'贾探春','➎':'史湘云'}
for item in d:
    print(item,d[item])
print('--------(5)---------')
for num,name in zip(num,name):
    print(num,name)


