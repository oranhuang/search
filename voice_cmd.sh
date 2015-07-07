#!/bin/bash
#echo "Recording your Speech ( 5 secs....)"
#arecord -D default -q -f S16_LE -t raw -r 16000 -c 1 -d 5 | flac - -f --endian=little --channels=1 --best --sample-rate=16000 --bps=16 --sign=signed -s -o voice_cmd.flac
 
echo "Converting Speech to Text..."
wget -q -U "Mozilla/5.0" --post-file voice_cmd.flac --header "Content-Type: audio/x-flac; rate=16000" -O - "https://www.google.com/speech-api/v2/recognize?output=json&lang=zh-tw&key=AIzaSyCI4xaS6DWdzOCm-Vk3J8VNUlN16EmCnQY&client=chromium&maxresults=6&pfilter=2" > sst.json

json_result=$(python2 jsonparser.py)
echo $json_result

# TTS example
#say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&tl=zh-TW&q=$*"; } 
#say $*

if [ "$json_result" == "weather" ];
then
        echo "weather"
	python2 htmlparser_weather.py 
elif [ "$json_result" == "news" ];
then
	echo "news"
	python2 htmlparser_news.py
else
        echo "error for output"
fi

#IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&tl=zh-TW&q=$*"

#echo "You Said:"
#value=`cat stt.txt`
#echo "$value"
