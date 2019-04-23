import webbrowser
import bs4
# from selenium import webdriver
import requests

# webbrowser.open('http://google.com')

#type python ./hello.py to run your program!

# print("Hi, glad to see you're looking for internships!  What are your keywords?")

# keywords = []
#
# while True:
#     print('Enter your keyword' + str(len(keywords) + 1) + '(or enter nothing to stop.):')
#     keyword = input()
#     if input == False:
#         break
#     keywords = keywords + [keyword]
# print('Your keywords are:')
# for word in keywords:
#     print('  ' + word)

keywords = []

print("Hi, glad to see you're looking for internships!  What are your keywords?")

while True:
    print('Enter your keyword ' + str(len(keywords) + 1) +
      ' (Or enter nothing to stop.):')
    keyword = input()
    if keyword == '':
        break
    keywords = keywords + [keyword] # list concatenation
print('Your keywords:')
for keyword in keywords:
    print('  ' + keyword)

print('Googling!...')
# for i in range(0,(len(keywords)+1)):
#     res = requests.get('http://google.com/search?q=' + ' '.join(keywords[i])
#     #res.raise_for_status()
#
#     soup = bs4.BeautifulSoup(res.text)
#     linkElems = soup.select('.r a')
#
#     numOpen = min(5, len(linkElems))
#     for i in range(numOpen):
#         webbrowser.open('http://google.com' + linkElems[i].get('href'))
