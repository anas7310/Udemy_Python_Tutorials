'''
Real-World Example: MultiThreading for I/O bound tasks
Scenario: Web Scraping
Web-Scraping often involves making numerous network requests to fetch web pages. These tasks are I/O bound because they spend a lot of time waiting for responses from servers. Multithreading can significantly improve the performance by allowing multiple web pages to be fetched concurrently.
'''
import time

'''
https://python.langchain.com/docs/introduction/
https://python.langchain.com/docs/concepts/
https://python.langchain.com/docs/tutorials/
'''

import threading
import requests
from bs4 import BeautifulSoup

urls = [
'https://python.langchain.com/docs/introduction/',
'https://python.langchain.com/docs/concepts/',
'https://python.langchain.com/docs/tutorials/',
'https://python.langchain.com/docs/introduction/',
'https://python.langchain.com/docs/concepts/',
'https://python.langchain.com/docs/tutorials/',
'https://python.langchain.com/docs/introduction/',
'https://python.langchain.com/docs/concepts/',
'https://python.langchain.com/docs/tutorials/',
'https://python.langchain.com/docs/introduction/',
'https://python.langchain.com/docs/concepts/',
'https://python.langchain.com/docs/tutorials/',
'https://python.langchain.com/docs/introduction/',
'https://python.langchain.com/docs/concepts/',
'https://python.langchain.com/docs/tutorials/',
'https://python.langchain.com/docs/introduction/',
'https://python.langchain.com/docs/concepts/',
'https://python.langchain.com/docs/tutorials/', 
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'fetched {len(soup.text)} characters from {url}')

threads = []
t= time.time()
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"All webpages fetched in {time.time() - t}")


t2=time.time()
for url in urls:
    fetch_content(url)
print(f"All webpages fetched in {time.time() - t2}")
