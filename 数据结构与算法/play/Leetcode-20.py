# -*- coding:utf-8 -*-
from stack_2 import Stack
# 遍历字符串
# 遇到左边括号，就入栈
# 遇到右边括号，栈是否为空
# 为空——>false
# 不为空，弹出栈顶
# 栈顶元素和右边括号进行匹配,看是否相同类型
# 不同——>false
# 相同继续遍历
# 如果字符串全部匹配完了
# 栈为空——>True
# 栈不为空——>False

def func(string):
    if len(string)%2:
        return False
    stack=Stack()
    dic={
        '(':')',
        '[':']',
        '{':'}'
    }
    for char in string:
        if char in "([{":
            stack.push(dic[char])
        else:
            if stack.is_empty() or stack.pop()!=char:
                return False
    return stack.is_empty()

if __name__ == '__main__':
    print(func("({)}[]"))