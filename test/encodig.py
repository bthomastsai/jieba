#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding=utf-8
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

print sys.getdefaultencoding()
s=u"中文字 "
print type(s)
#print s
print s.decode('utf-8').encode('utf-8')
