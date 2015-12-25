#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

print sys.getdefaultencoding()

import jieba
import jieba.posseg
import jieba.analyse

print('='*40).decode('utf-8').encode('utf-8')
print('1. 分词').decode('utf-8').encode('utf-8')
print('-'*40).decode('utf-8').encode('utf-8')

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list)).decode('utf-8').encode('utf-8')  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list)).decode('utf-8').encode('utf-8')  # 默认模式

seg_list = jieba.cut("他来到了网易杭研大厦")
print(", ".join(seg_list)).decode('utf-8').encode('utf-8')

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list)).decode('utf-8').encode('utf-8')

print('='*40).decode('utf-8').encode('utf-8')
print('2. 添加自定义词典/调整词典').decode('utf-8').encode('utf-8')
print('-'*40).decode('utf-8').encode('utf-8')

print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False))).decode('utf-8').encode('utf-8')
#如果/放到/post/中将/出错/。
print(jieba.suggest_freq(('中', '将'), True))
#494
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False))).decode('utf-8').encode('utf-8')
#如果/放到/post/中/将/出错/。
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False))).decode('utf-8').encode('utf-8')
#「/台/中/」/正确/应该/不会/被/切开
print(jieba.suggest_freq('台中', True))
#69
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False))).decode('utf-8').encode('utf-8')
#「/台中/」/正确/应该/不会/被/切开

print('='*40).decode('utf-8').encode('utf-8')
print('3. 关键词提取').decode('utf-8').encode('utf-8')
print('-'*40).decode('utf-8').encode('utf-8')
print(' TF-IDF').decode('utf-8').encode('utf-8')
print('-'*40).decode('utf-8').encode('utf-8')

s = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
for x, w in jieba.analyse.extract_tags(s, withWeight=True):
    print('%s %s' % (x, w)).decode('utf-8').encode('utf-8')

print('-'*40).decode('utf-8').encode('utf-8')
print(' TextRank').decode('utf-8').encode('utf-8')
print('-'*40).decode('utf-8').encode('utf-8')

for x, w in jieba.analyse.textrank(s, withWeight=True):
    print('%s %s' % (x, w)).decode('utf-8').encode('utf-8')

print('='*40).decode('utf-8').encode('utf-8')
print('4. 词性标注').decode('utf-8').encode('utf-8')
print('-'*40).decode('utf-8').encode('utf-8')

words = jieba.posseg.cut("我爱北京天安门")
for word, flag in words:
    print('%s %s' % (word, flag)).decode('utf-8').encode('utf-8')

print('='*40).decode('utf-8').encode('utf-8')
print('6. Tokenize: 返回词语在原文的起止位置').decode('utf-8').encode('utf-8')
print('-'*40).decode('utf-8').encode('utf-8')
print(' 默认模式').decode('utf-8').encode('utf-8')
print('-'*40).decode('utf-8').encode('utf-8')

result = jieba.tokenize('永和服装饰品有限公司')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2])).decode('utf-8').encode('utf-8')

print('-'*40).decode('utf-8').encode('utf-8')
print(' 搜索模式').decode('utf-8').encode('utf-8')
print('-'*40).decode('utf-8').encode('utf-8')

result = jieba.tokenize('永和服装饰品有限公司', mode='search')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2])).decode('utf-8').encode('utf-8')
