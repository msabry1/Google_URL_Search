from colorama import Fore
from time import sleep
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
def inpuut() :
    path = input('Enter file path ==> ')
    try:
        open_file = open(path , 'r').read().splitlines()
        for line in open_file:
            try:
                ur = line.split("/")[2]
                if ('www.') in ur:
                	ur= ur.replace('www.' , '')
                if ur.count('.') == 2:
                	ur = ur.split('.')[1] + '.'+ ur.split('.')[2]
                with open('result.txt' , 'a') as kk:
                    kk.write(f'\n{ur}')
                opem = open('result.txt').read().splitlines()
                removed = list(dict.fromkeys(opem))
                with open('clean_result.txt' , 'w') as wr:
                	for removed_line in removed:
                		#print(removed_line)
                		wr.write(f'{removed_line}\n')
            except IndexError:
            	continue        
    except FileNotFoundError:
        print('Error File Name')
        inpuut()
inpuut()
 	
