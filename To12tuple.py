#!python
import sys,json,md5,time

'''
	usage: cat data.txt | ./To12tuple.py argv > result

	data: name	age image	nationality
		  xxx	20	xxx.jpg China

	argv: a refer txt


'''

class Transformer(object):
	def __init__(self,attrs):
		self.length = len(attrs)
		self.default_datasource = 'url'
		self.sources = [self.default_datasource] * self.length
		self.data_types = ['text'] * self.length
		self.keys = []
		self.type = 'None'
		self.refer = None
		for e,i in zip(attrs,xrange(self.length)):
			if ':' in e:
				e,self.data_types[i] = e.split(':')
			if '<' in e:
				e,self.sources[i] = e.split('<')
			self.keys.append(e)
	def set_type(self,type):
		self.type = type
	def set_datasource(self,data_source):
		self.default_datasource = data_source
		new_sources = []
		for source in self.sources:
			if source == 'url':
				source = self.default_datasource
			new_sources.append(source)
		self.sources = new_sources

	def set_refer(self,path):
		self.refer = {}
		for line in open(path,'r'):
			eles = line.rstrip('\n').split('\t')
			ID = eles[0]
			type = eles[1]
			if eles[2] == 'name':
				name = eles[3]
				self.refer.setdefault(type,{})
				self.refer[name] = {'id':ID,'name':name}

	def process(self,eles):
		# create ID
		assert(len(eles) == self.length)
		if not 'ID' in self.keys:
			str4md5 = ''
			if 'name' in self.keys:
				name_index = self.keys.index('name')
				str4md5 += eles[name_index]
			if 'url' in self.keys:
				url_index = self.keys.index(self.default_datasource)
				str4md5 += eles[url_index]
			ID = md5.new(str4md5).hexdigest()
		else:
			ID_index = self.keys.index('ID')
			ID = eles[ID_index]
		sources = [ eles[self.keys.index(source)] for source in self.sources]
		for ele,key,data_type,source in zip(eles,self.keys,self.data_types,sources):
			if not key or not ele or data_type == 'del' or key == 'ID': continue
			if data_type == 'refer': 
				refer = self.refer[self.type].get(ele,None)
				if not refer:
					print >>sys.stderr, 'type:%s, name: %s not found' % (self.type, ele)
				else:
					ele = json.dumps(refer,ensure_ascii=False).encode('utf-8')

			for sub in ele.split('|'):
				print '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t\t'.format(ID, self.type, key,
					sub, 'raw', source, 'STRUCT', data_type, 'zh-cn', time.time())
				if key == 'name': key = 'alias'


def main():
	#attrs =	['description_src:url','name','heat:num','description','image:url','pic_6n_121<image:url','alias','baike_alias','com_alias'] #food
	#attrs = ['name','heat:num','link_txt','query_txt','description','description_src:url','image:url','pic_4n_78<image:url','pic_6n_121<image:url','ref_pic_4n_78<image:url','ref_pic_6n_121<image:url'] 
	#attrs = ['ID','name','description_src','subtype']
	attrs = ['ID','show_txt','description_src:del']
	transformer = Transformer(attrs)
	transformer.set_type('ReferObj')
	transformer.set_datasource('description_src')
	for line in sys.stdin:
		transformer.process(line.rstrip('\n').split('\t'))



if __name__ == '__main__':
	main()

