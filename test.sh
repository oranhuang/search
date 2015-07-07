#!/bin/bash
#result=$(python /home/oran/raspberrypi/src/search/htmlparser_weather.py)
#python /home/oran/raspberrypi/src/search/htmlparser_weather.py
#echo -e "$(python /home/oran/raspberrypi/src/search/htmlparser_weather.py)"
#echo -e "$result"

#if [ $result == yes ] ;
#then
#        echo "weather"
#else
#        echo "error for output"
#fi
#LANG=tw_zh.UTF-8
#./htmlparser_weather.py
#echo $LANG
result=$(python jsonparser.py)
#result=$(python /home/oran/raspberrypi/src/search/htmlparser_weather.py)
#result=你好
echo $result
echo $result
