#!/usr/bin/env python3
# -*- coding: utf-8 -*-
sentence=input('Sentence: \n')

screen_width=80
text_width=len(sentence)
box_width=text_width+6
left_margin=(screen_width - box_width)//2

print()
print(''* left_margin + '+'+'-'*(box_width-2)+'+')
print(''* (left_margin*4) + '| '+' '*text_width +'| ')
print(''* (left_margin*4) + '| '+     sentence  +'| ')
print(''* (left_margin*4) + '| '+' '*text_width +'| ')
print(''* left_margin + '+'+'-'*(box_width-2)+'+')
print()