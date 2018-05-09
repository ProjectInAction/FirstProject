# -*- coding: UTF-8 -*-
import string
oStr = input("请输入一串字符:")
 
str_num = 0
spac_num = 0
figue_num = 0
Chinese_num = 0
other_num = 0
 
for strs in oStr:
    if strs in string.ascii_letters:
        str_num +=1
    elif strs.isdigit():
        figue_num +=1
    elif strs.isspace():
        spac_num +=1
    elif strs.isalpha():
        Chinese_num += 1
    else:
        other_num += 1
print ("英文字母有：%d" %str_num)
print ("数字字符有：%d" %figue_num)
print ("空格字符有：%d" %spac_num)
print ("中文字符有：%d" %Chinese_num)
print ("其他字符有：%d" %other_num)
