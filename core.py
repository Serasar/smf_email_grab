from bs4 import BeautifulSoup

import requests

members_page = 'https://bitcointalk.org/index.php?action=mlist;sa=search;search=@;fields=email;start='

current_page = 0
step = 30

cookie = {
    "PHPSESSID": "61stogg1iiefepqknu9q0gfu41",
    "SMFCookie129": "a%3A4%3A%7Bi%3A0%3Bs%3A6%3A%22323394%22%3Bi%3A1%3Bs%3A40%3A%22fc93f2b72b4a95c6fca7bf216666a7f640565f95%22%3Bi%3A2%3Bi%3A1645872340%3Bi%3A3%3Bi%3A0%3B%7D",
}



while True:
	page = requests.get(members_page + str(current_page), cookies=cookie) # get page with forum members
	print("Current page:" + str(current_page))
	soup = BeautifulSoup(page.text)
	current_page = current_page + step # Increment so you can see next page
	for link in soup.find_all('img', alt="Email"): # find all emails
		print(link.parent['href'])
		emailfile = open('emails.txt', 'a')
		emailfile.write(str(link.parent['href']))
		emailfile.write('\n')
		emailfile.close