import requests
from bs4 import BeautifulSoup
from time import sleep
import os 
count = 0
with open('output.txt', 'r') as file:
    for line in file:
        url = line.strip()

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        mail_element = soup.find('div', class_='mobile-portrait-row mail')
        try:
            count = count + 1
            os.system("title "+str(count))
            if mail_element:
                email_address = mail_element.a.get_text().replace(" ","")
                print(email_address.replace("@â€‹","@"))
            else:
                sleep(0)
                
        except:

            print(url + ": " + "Email address not found.")
input()