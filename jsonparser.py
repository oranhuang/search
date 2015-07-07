#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sys
from pprint import pprint
import codecs

#json_data=open('sst.json').read()
#data = json.loads(json_data)
#pprint(data)
#with open('sst.json') as data_file:    
#	data = json.load(data_file)
#
#pprint(data)
#data = []
#with open('sst.json') as f:
#    for line in f:
        #data.append(json.loads(line))
	
#	print json.dumps(json.loads(line))
#print dir(data)
#data_u = data.decode('utf8')
#print u'%s' % (data_u)
#pprint u(data)
#print len(data)
#print data[1]

#########################################
f = open('sst.json', 'r')
filestr = f.read().decode('utf8')
#print filestr
#filestr.split()
#print filestr
if not((filestr.find(u'天氣')) == -1):
	print 'weather'
elif not((filestr.find(u'新聞')) == -1):
	print 'news'
	#if filestr.find('你好') == True:
	#	print 'yes'
