#!/usr/bin/python
# -*- coding: utf-8 -*- 
import urllib
#weatherContent = weatherWeb.read().decode('utf_8')
#weatherWeb.close()

import HTMLParser
import sys
import codecs

class weatherParser(HTMLParser.HTMLParser):	
	def __init__(self):
		self.reset()
		#HTMLParser.__init__()
		self.day = []
		self.location = []
		self.temperature = []
		self.humid = []
		self.result_str = []
		# the attribute's  flags
		self.temp_high_found = False 
		self.temp_low_found = False
		self.temp_high_content_found = False
		self.temp_low_content_found = False
		self.rain_chance = False
		self.rain_status = False
		self.day_found = False
		self.stop = False
		self.string_cnt = 0
	def handle_starttag(self, tag, attrs):	
	#    #print 'tag %s, %s start from' % (tag, attrs)
		if tag == 'a':
			for name, value in attrs:
				if name == 'href':
					if value == u'https://tw.news.yahoo.com/weather/台灣/桃園縣/':
						#print value
						self.found = True
	#				#print self.get_starttag_text()
		if tag == 'li':
			for name, value in attrs:
				if name == 'class':
					if value == 'day-name' and self.day == []:
						self.day_found = True
						#print 'day name found'
					if value == 'temp-c high-temp' and self.day_found:
							self.temp_high_found = True
							#print 'temp-c high-temp found'
							#print self.get_starttag_text()
					if value == 'temp-c low-temp' and self.day_found:
							self.temp_low_found = True
							#print 'found low temp'
					if value == 'icon' and self.day_found:
							self.rain_status = True
					if value == 'pop' and self.day_found:
							self.rain_chance = True
							#print 'get rainning chance'
					#if value == 'daily-forecast':
							#self.stop = True
							#print 'stop'
		if tag == 'span':
			for name, value in attrs:
				if name == 'class':
					if value == 'hidetext':
							if self.temp_high_found:
								self.temp_high_content_found = True
								#print self.get_starttag_text()
							elif self.temp_low_found:
								self.temp_low_content_found = True
								#print 'found low temp content'
				

	def handle_endtag(self, tag):
		if tag == 'li':
			if self.temp_high_content_found:
				self.temp_high_content_found = False
				self.temp_high_found = False
				#print self.day
				#print self.temperature_high
			if self.rain_status :
				self.rain_status = False
				self.rain_chance = False
			if self.temp_low_content_found:
				self.temp_low_content_found = False
				self.temp_low_found = False
				self.day_found = False
				#print self.temperature
				if self.string_cnt == 6:
					self.result_str = u' %s,%s,溫度最%s,攝氏%s度,最%s,攝氏%s度' %tuple(self.temperature)
				elif self.sting_cnt == 7:
					self.result_str =  u' %s,%s,降雨機率%s,溫度最%s,攝氏%s度,最%s,攝氏%s度' %tuple(self.temperature)
				#print '%d' % self.string_cnt
				#rint u' %s,' %tuple(self.temperature)
				print self.result_str
				f = open('weather', 'w')
				f.write(self.result_str.encode('utf8'))
				f.close()
			
	#    print 'empty tag %s %s' % (tag, attrs)
	#def handle_endtag(self, tag):
	#    print 'tag %s, end ' % tag
	def handle_data(self, data):
		data = data.strip()
	        #if hasattr(self, 'found') and data:
		#        if data == u'高雄':
        	#	        self.stop = True  
		#                return  
        	#	self.weather.append(data)  
        	if data == u'今天' and self.day_found:
	        #	self.found = True  
		#	self.weather = ['found taoyuan']  
			#weather.append(data)
			self.day = data 
			self.temperature.append(data)		
			self.string_cnt = self.string_cnt + 1	
			#print u'%s' %data
			#print u'%s'%tuple(self.temperature)
			#self.day_found = False
			#print self.day
		if self.temp_high_found and self.temp_high_content_found:
			#self.temperature_high = []
			self.temperature.append(data)
			self.string_cnt = self.string_cnt + 1	
			#print u'%s' %self.temperature
			#print u'%s'%data				
		if self.temp_low_found and self.temp_low_content_found:
			self.temperature.append(data)
			self.string_cnt = self.string_cnt + 1	
			#print u'%s' %data
		if self.rain_status:
			#print u'%s' %data
			self.temperature.append(data)
			self.string_cnt = self.string_cnt + 1	
		if self.rain_chance:
			self.temperature.append(data)
			self.string_cnt = self.string_cnt + 1	
			 
	#    print 'data %s' % data
	#def handle_comment(self, data):
	#    print 'comment %s ' % data
	#
	#def unknown_decl(self, data):
	#    """Override unknown handle method to avoid exception"""
	#    pass



weatherWeb = urllib.urlopen("http://tw.weather.yahoo.com/today")
#weatherWeb = urllib.urlopen("https://tw.news.yahoo.com/weather-forecast")
#weatherWeb = urllib.urlopen("https://weather.yahoo.com/taiwan/taoyuan-city/taoyuan-city-91982232/")
Parser = weatherParser()
#print dir(Parser)
weatherContent = weatherWeb.read().decode('utf_8', 'ignore')
#Parser.feed(urllib.urlopen( \
#	"http://tw.weather.yahoo.com/today.html").read())
weatherWeb.close()
#Parser.close()
#
try:
	for line in weatherContent.splitlines():
		#if hasattr(Parser, 'stop') and Parser.stop:
		if Parser.stop == True:
			#print 'stop parse'
			break
		Parser.feed(line)
except HTMLParser.HTMLParseError, data:
	print "## print Parse: " + data.msg
Parser.close()

print "Please press enter to continue"
raw_input()

