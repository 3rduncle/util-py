import sys,json

attr = sys.argv[1].decode('utf-8')
for line in sys.stdin:
	line = line.rstrip('\n')
	url,entity = line.split('\t')
	entity = json.loads(entity,encoding='utf-8')
	if attr in entity:
		entity.pop(attr)
	else:
		print >> sys.stderr, '!!' + url
	print url + '\t' + json.dumps(entity,ensure_ascii=False).encode('utf-8')

