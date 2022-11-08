from random import *
import time
import requests
from colorama import Fore, Back, Style
import colorama

d=1
gen = ''
t = ''
s = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'

colorama.init()

print(Fore.GREEN + '╔══╗╔╗╔╗╔╗╔╗╔╗╔╗╔╗╔╗─╔══╗────╔═══╗╔════╗╔══╗───╔═══╗─╔══╗╔══╗ \n' +
'║╔═╝║║║║║║║║║║║║║║║║─║╔╗║────╚══╗║╚═╗╔═╝║╔╗║───╚══╗║─║╔╗║║╔╗║ \n'+
'║║──║╚╝║║║║║║║║║║║║║─║║║║─────╔═╝╝──║║──║║║║────╔═╝║─║║║║║║║║ \n'+
'║║──╚═╗║║║╔║║║║║║║╔║─║║║║─────╚═╗╗──║║──║║║║────╚═╗║─║║║║║║║║ \n'+
'║╚═╗─╔╝║║╚╝║║╚╝║║╚╝║╔╝╚╝╚╗───╔══╝║──║║──║╚╝║───╔══╝║╔╝║║║║╚╝║ \n'+
'╚══╝─╚═╝╚══╝╚══╗╚══╝╚════╝───╚═══╝──╚╝──╚══╝───╚═══╝╚═╝╚╝╚══╝ \n'

)

while True:
        for i in range(16):
            gen = gen + s[randint(0, 61)]
        t = 'https://discord.gift/' + gen
        url = 'https://discordapp.com/api/v6/entitlements/gift-codes/' + gen + '?with_application=false&with_subscription_plan=true'
        r = requests.get(url)
        if r.status_code == 404:
            print(Fore.RED + 'invalid | '+ t)
            #print(colored('invalid | '+ t, 'red'))
            d=1

        elif r.status_code == 429:
            print(Fore.CYAN + 'unsuccessful response, rying after 10000 (' + str(d) + '/6)')
            #print(colored('unsuccessful response, rying after 10000 (' + str(d) + '/6)'), 'cyan')
            time.sleep(10)
            if d<6:
                d=d+1
            else:
                d=1
        else:
            #print(colored('valid | '+ t, 'green'))
            print(Fore.CYAN + 'valid | '+ t)
            d=1
            f = open("valid.txt", "a")
            f.write(str(t) + '||| ')
            
        gen = ''
        url = ''
