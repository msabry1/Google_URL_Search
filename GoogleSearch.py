try:
	import re
	import requests
	from colorama import Fore
except ModuleNotFoundError:
	import os
	os.system('pip install requests')
	os.system('pip install colorama')
	import requests
	from colorama import Fore



logo = """    
  ___  ___   _____   _   _       ___       ___  ___   _____   _____  
    /   |/   | /  _  \ | | | |     /   |     /   |/   | | ____| |  _  \ 
   / /|   /| | | | | | | |_| |    / /| |    / /|   /| | | |__   | | | | 
  / / |__/ | | | | | | |  _  |   / / | |   / / |__/ | | |  __|  | | | | 
 / /       | | | |_| | | | | |  / /  | |  / /       | | | |___  | |_| | 
/_/        |_| \_____/ |_| |_| /_/   |_| /_/        |_| |_____| |_____/  
"""
logo2 = """ 
 _____       ___   _____   _____   __    __ 
/  ___/     /   | |  _  \ |  _  \  \ \  / / 
| |___     / /| | | |_| | | |_| |   \ \/ /  
\___  \   / / | | |  _  { |  _  /    \  /   
 ___| |  / /  | | | |_| | | | \ \    / /    
/_____/ /_/   |_| |_____/ |_|  \_\  /_/     
"""
print (f"{Fore.RED} {logo}")
print (f"{Fore.YELLOW} {logo2}")
print (f'\n{Fore.CYAN}                          By @M_50_S Telegram  ')





class GetUrlFromSearch:
    ''' Class To Get Url from Google Search '''
    
    def __init__(self,search_name):
        self.search_name = search_name
    
    
    def Google_Search(self):
        goo_request = requests.get(f'https://www.google.com/search?q={self.search_name}&num=100').text
        goo_find = re.findall(r'https?://w?w?w?.?\w+.\w+\w+\.[a-z?]+' , goo_request)
        return goo_find



def Input():
	file = input(f'{Fore.CYAN}Type Dorks File: ')
	try:
		open_file = open(file,'r').read().splitlines()
		print(f'{Fore.LIGHTBLUE_EX}Wait To Scrape URL......... ')
		for dork in open_file:
			dd = GetUrlFromSearch(dork)
			ddd = dd.Google_Search()
			with open(f'{file}_GoogleSearch.txt' , 'a' ) as opened :
				for url in ddd:
				    opened.write(f'{url}\n')
		print(f'{Fore.GREEN}Search Done and saved in {file}_GoogleSearch.txt ')
	except FileNotFoundError:
		print(f'{Fore.RED}Error File Name.........')
		Input()


if __name__ == '__main__':
	Input()
