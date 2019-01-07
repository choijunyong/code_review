#-*- coding: utf-8 -*-
import sys
from urllib import urlopen
import requests
from bs4 import BeautifulSoup
from collections import Counter


# 네이버주식 상위 30개 긁어와서 텍스트 파일에 쓰기

# url = requests.get("https://finance.naver.com/sise/lastsearch2.nhn")
# html = url.content
# soup = BeautifulSoup(html,'html.parser')
# result = soup.select('td> a')
# with open("/Users/xiilab/Desktop/kiup.txt",'w') as f:
#     for i in result:
#         f.write("\n \t")
#         f.write(str(unicode(i.text).encode('euc-kr')))
#         # print i.text


# 기상청 매분 관측 자료 가지고 와서 텍스트 파일에 쓰기

# url = requests.get("http://www.kma.go.kr/cgi-bin/aws/nph-aws_txt_min")
# html = url.content
# soup = BeautifulSoup(html,'html.parser')
# result = soup.select('tr> td:nth-child(2) > a')
# with open("/Users/xiilab/Desktop/kiup.txt",'w') as f:
#     for i in result:
#         f.write("\n \t")
#         f.write(str(unicode(i.text).encode('euc-kr')))
#         # print (i.text)
# result =[]
# with open("/Users/xiilab/Desktop/memo.txt",'r') as f :
#     result = f.readline(' ')
#     for i in result:
#         print(i)

# 최고 빈도 단어 탑 10 뽑기
# with open('/Users/xiilab/Desktop/memo.txt', 'r') as f:
#     text = f.readline().split()
#     for w in Counter(text).most_common(10):
#         print w


