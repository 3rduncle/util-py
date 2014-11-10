#coding:utf-8
import sys,json



attr = ['url','name',u'营养信息.热量(大卡)', 'description','image_url','pic_6n_121']
ignore_attr = [u'别名','baike_alias','com_alias']

def _f(x):
	keys = x.split('.')
	tail = entity
	for key in keys:
		tail = tail[key]
	if type(tail) == type([]): tail = '|'.join(tail)
	re_list.append(tail)

def _if(x):
	keys = x.split('.')
	try:
		tail = entity
		for key in keys:
			tail = tail[key]
		if type(tail) == type([]): tail = '|'.join(tail)
		re_list.append(tail)
	except:
		re_list.append('')

do = 0
white_list = set([ line.decode('utf-8').rstrip('\n') for line in open('final/food_name.txt','r')])
for line in sys.stdin:
	url,entity = line.rstrip('\n').split('\t')
	entity = json.loads(entity,encoding='utf-8')
	name = entity.get('name')
	if not name: continue
	if name not in white_list:continue
	re_list = []
	#map(lambda x: _f(x), attr)
	try:
		map(lambda x: _f(x), attr)
	except:
		continue
	map(lambda x: _if(x), ignore_attr)

	print '\t'.join(re_list).encode('utf-8')
	do += 1

print >>sys.stderr, do
print >>sys.stderr, json.dumps(attr,ensure_ascii=False).encode('utf-8')
