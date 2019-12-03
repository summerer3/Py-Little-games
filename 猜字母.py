# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

import random
letter_list = ['a', 'b', 'c', 'd', 'e', 'f','g',
 'h', 'i', 'j', 'k', 'l','m', 'n',
 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']
letter = letter_list[random.randint(0, 25)]
idx0 = letter_list.index(letter)
count = 0
while True:
    count += 1
    if count > 5:
        print('游戏失败。')
        break
    g = input('输入猜测的字母：')
    if g in letter_list:
        idx = letter_list.index(g)
        if g == letter:
            print('回答正确！')
            break
        elif idx > idx0:
            print('大了！')
        else:
            print('小了！')
