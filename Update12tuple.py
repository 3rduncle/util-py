import sys

id_data = {}
for line in open(sys.argv[1],'r'):
    line = line.rstrip('\n')
    ID = line.split('\t')[0]
    id_data.setdefault(ID,[])
    id_data[ID].append(line)

new_ID = ''
old_ID = ''
buffer = []
for line in sys.stdin:
    line = line.rstrip('\n')
    new_ID = line.split('\t')[0]
    if new_ID != old_ID:
        buffer += id_data.get(old_ID,[])
        if buffer:print '\n'.join(buffer)
        old_ID = new_ID
        buffer = [line]
    else:
        buffer.append(line)
else:
    buffer += id_data.get(new_ID,[])
    print '\n'.join(buffer)
        
    
