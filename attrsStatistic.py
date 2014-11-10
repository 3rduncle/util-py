#coding:utf-8
import sys,json


import collections
data = collections.Counter()
for line in sys.stdin:
	line = line.rstrip('\n')
	url, entity = line.split('\t')
	entity = json.loads(entity, encoding='utf-8')
	data.update([u'实体数'])
	data.update(entity.keys())

ll = data.items()
ll.sort(lambda x,y:-cmp(x[1],y[1]))
for key,value in ll:
	print (key +'\t'+ str(value)).encode('utf-8')
