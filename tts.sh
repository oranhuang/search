#!/bin/bash 
say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&tl=zh-TW&q=$*"; } 
say $*
