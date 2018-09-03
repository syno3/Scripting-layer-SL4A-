"""
Copyright [2018] [festus murimi]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
#-*-coding:utf8;-*-

#this scripts request url using request module
#load the data and stores it in a variable
#uses html parser and stores necessary data
#load the data in PY4A google tts

__author__ = "festus murimi"
__license__ = "Apache V2.0"
__copyright__ = "copyright(c), 2018"
__email__ = "sinotechxvista@gmail.com"
#importing modules needed

import time
import androidhelper
import urllib.request
import sys
#from html.parser import HTMLparser
#import xml.dom

#setting necessary variables

droid = androidhelper.Android()
url = input("please enter the website\n")
#terminal colors

red = '\033[91m'
white = '\033[1;97m'
green = '\033[1;32m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'

#this function removes all tags in the DATA received

class MYHTMLparser(HTMLparser):
    def handle_data(self,data):
        request = input("do you want to display data received? [Y\N]\n")
        if request.upper == 'Y':
            print("***-----------&&&-----------***\n\n") 
            print(green+data)
            time.sleep(5)
            droid.ttsSpeak(data)
        elif request.upper == 'N':
            droid.ttsSpeak(data)
        else:
            print(red+"please enter a valid input\n")
            time.sleep(5)
            return parser
         
parser = MYHTMLparser()
parser.feed(DATA)
#this checks whether http:// is present in url variable

if url.startswith('http://'):
    #send data using urllib.request
    with urllib.request.urlopen("url") as DATA:
        parser
else:
    url.append(0, 'http://')
    with urllib.request.urlopen("url") as DATA:
        parser
    


