#!/usr/bin/env python3
# -*- coding: utf-8 -*-
name1=input('傻儿子，你叫什么：\n')
s1=float(input('请输入您上次考试的成绩: \n'))
s2=float(input('请输入您这次考试的成绩: \n'))
r=float(s2-s1)
r=float(r/s1)*100
if r>0:
	print('优秀！恭喜傻儿子，',name1,'，你的成绩提升了：%d%%' % r)
elif r<0:
	print('垃圾！真特么是个傻儿子，', name1,'你的成绩掉了： %d%%' % -r)	
else:
	print('原地踏步可不行啊！')
input('Press <Enter> to exit'