import sys,json

for line in sys.stdin:
	line = line.rstrip('\n')
	url,entity = line.split('\t')
	entity = json.loads(entity,encoding='utf-8')
	for attr in sys.argv[1:]:
		attr = attr.decode('utf-8')
		values = entity.get(attr)
		if values:
			if type(values) != type([]): values = [values]
			for value in values:
				print value.strip().encode('utf-8')
		else:
			print >> sys.stderr, '!! %s has not %s' %  (url, attr.encode('utf-8'))

