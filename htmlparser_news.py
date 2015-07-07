#!/usr/bin/python
# -*- coding: utf-8 -*- 
import urllib
#weatherContent = weatherWeb.read().decode('utf_8')
#weatherWeb.close()

import HTMLParser
import sys
import codecs
import os
import pycurl

class newsParser(HTMLParser.HTMLParser):	
	def __init__(self):
		self.reset()
		#HTMLParser.__init__()
		self.result_str1 = []
		self.result_str2 = []
		self.result_str3 = []
		self.result_str4 = []
		self.result_str5 = []
		self.result_str6 = []
		self.news1 = []
		self.news2 = []
		self.news3 = []
		self.news4 = []
		self.news5 = []
		self.news6 = []
		# the attribute's  flags
		self.string_cnt = 0
		self.headline_found = False
	def handle_starttag(self, tag, attrs):	
	#    #print 'tag %s, %s start from' % (tag, attrs)
		if tag == 'div':
			for name, value in attrs:
				if name == 'class':
					if value == 'headlines specialheadlines':
						#print value
						self.headline_found = True
	def handle_endtag(self, tag):
		if tag == 'div' and self.headline_found == 1:
				#print u'string count = %d' %self.string_cnt
				self.result_str1 = u'今日新聞,%s,%s,%s' %tuple(self.news1)
				self.result_str2 = u'%s,%s,%s' %tuple(self.news2)
				self.result_str3 = u'%s,%s,%s' %tuple(self.news3)
				self.result_str4 = u'%s,%s,%s' %tuple(self.news4)
				self.result_str5 = u'%s,%s,%s' %tuple(self.news5)
				self.result_str6 = u'%s' %tuple(self.news6)
				self.headline_found = False
				print self.result_str1
				print self.result_str2
				print self.result_str3
				print self.result_str4
				print self.result_str5
				print self.result_str6
				#self.speakSpeechFromText(self.result_str.encode('utf8'))
				self.speakSpeechFromText(self.result_str1.encode('utf8'))
				self.speakSpeechFromText(self.result_str2.encode('utf8'))
				self.speakSpeechFromText(self.result_str3.encode('utf8'))
				self.speakSpeechFromText(self.result_str4.encode('utf8'))
				self.speakSpeechFromText(self.result_str5.encode('utf8'))
				self.speakSpeechFromText(self.result_str6.encode('utf8'))
			
	def handle_data(self, data):
		data = data.strip()
        	if self.headline_found:
			if self.string_cnt <= 2:
				self.news1.append(data)
			elif self.string_cnt <=5 and self.string_cnt > 2:
				self.news2.append(data)
			elif self.string_cnt <=8 and self.string_cnt > 5:
				self.news3.append(data)
			elif self.string_cnt <=11 and self.string_cnt > 8:
				self.news4.append(data)
			elif self.string_cnt <=14 and self.string_cnt > 11:
				self.news5.append(data)
			elif self.string_cnt <=17 and self.string_cnt > 14:
				self.news6.append(data)
			self.string_cnt = self.string_cnt + 1	


	def downloadFile(self, url, fileName):
	    fp = open(fileName, "wb")
	    curl = pycurl.Curl()
	    curl.setopt(pycurl.URL, url)
	    curl.setopt(pycurl.WRITEDATA, fp)
	    curl.perform()
	    curl.close()
	    fp.close()

	def getGoogleSpeechURL(self, phrase):
	    googleTranslateURL = "http://translate.google.com/translate_tts?ie=UTF-8&tl=zh-TW&"
	    parameters = {'q': phrase}
	    data = urllib.urlencode(parameters)
	    googleTranslateURL = "%s%s" % (googleTranslateURL,data)
	    return googleTranslateURL

	def speakSpeechFromText(self, phrase):
	    googleSpeechURL = self.getGoogleSpeechURL(phrase)
	    self.downloadFile(googleSpeechURL,"tts.mp3")
	    os.system("mplayer tts.mp3 -af extrastereo=0")


newsWeb = urllib.urlopen("http://news.cnyes.com/")
#weatherWeb = urllib.urlopen("https://tw.news.yahoo.com/weather-forecast")
#weatherWeb = urllib.urlopen("https://weather.yahoo.com/taiwan/taoyuan-city/taoyuan-city-91982232/")
Parser = newsParser()
#print dir(Parser)
newsContent = newsWeb.read().decode('utf_8', 'ignore')
#Parser.feed(urllib.urlopen( \
#	"http://tw.weather.yahoo.com/today.html").read())
newsWeb.close()
#Parser.close()
#
try:
	for line in newsContent.splitlines():
		if hasattr(Parser, 'stop') and Parser.stop:
			if Parser.stop == True:
				#print 'stop parse'
				break
		Parser.feed(line)
except HTMLParser.HTMLParseError, data:
	print "## print Parse: " + data.msg

#Parser.speakSpeechFromText(Parser.result_str)
Parser.close()

#print "Please press enter to continue"
#raw_input()

