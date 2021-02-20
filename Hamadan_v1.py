import time
import requests
import time as mm
import sys as n
import os
from pip._vendor.colorama import Fore, Style
def slow(M):  ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 20)


def slow2(M):  ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 25)


def slow1(M):  ## By Twitter : @Matrix0700
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
def meun():
    meun = Fore.LIGHTWHITE_EX + '''
     [1]From Hex To ARM64
     [2]From ARM64 To HEX
     [00]exit
    '''
    slow(meun)
def logo():
    Logo = '''

                             __
               ---_ ...... _/_ -
              /  .      ./ .'*\ \ 
              : '         /__-'   \.
             /                      )
           _/                  >   .'
         /   .   .       _.-" /  .'
         \           __/"     /.'/|
           \ '--  .-" /     //' |\|
            \|  \ | /     //_ _ |/|
             `.  \:     //|_ _ _|\|
             | \/.    //  | _ _ |/| @Xcodeone1
              \_ | \/ /    \ _ _ \\\ 
                  \__/      \ _ _ \|\ 
        '''
    title = '''
    
▒█░▒█ █▀▀█ █▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀▄ 
▒█▀▀█ █▄▄█ █░▀░█ █▄▄█ █░░█ █▄▄█ █░░█ 
▒█░▒█ ▀░░▀ ▀░░░▀ ▀░░▀ ▀▀▀░ ▀░░▀ ▀░░▀
    '''
    slow1(Fore.LIGHTRED_EX + Logo + Fore.LIGHTWHITE_EX + title)
os.system('clear')
logo()
meun()
numper = int(input(Fore.LIGHTWHITE_EX + Style.BRIGHT + '#Enter number>>  '))
os.system('clear')
while True:
    if numper == 00:
        break
    if numper == 1:
        os.system('clear')
        logo()
        Hex_input = input(Fore.LIGHTGREEN_EX+"Put Hex value you want Converte to ARM64 instruction :")
        os.system('clear')
        hex_url = "https://armconverter.com:443/api/convert"
        hex_cookies = {"__cfduid": "d9cf886854153f1d87ce3aab9bca0edbd1613734618"}
        hex_headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:85.0) Gecko/20100101 Firefox/85.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://armconverter.com/?disasm",
            "Content-Type": "text/plain;charset=UTF-8",
            "Origin": "https://armconverter.com",
            "Connection": "close"}
        hex_json = {"hex": Hex_input}
        re = requests.post(hex_url, headers=hex_headers, cookies=hex_cookies, json=hex_json)
        data = re.json()
        asm = data['asm']
        asmIn = asm['arm64']
        logo()
        slow(Fore.LIGHTGREEN_EX + "From HEX To ARM64 instructions : " + Fore.LIGHTCYAN_EX + asmIn[1])
        exit()
    if numper == 2:
        os.system('clear')
        logo()
        arm64_input = input(Fore.LIGHTGREEN_EX+"Put the ARM64 instruction you want Converte to hex : ")
        os.system('clear')
        arm64_url = "https://armconverter.com:443/api/convert"
        arm64_cookies = {"__cfduid": "d9cf886854153f1d87ce3aab9bca0edbd1613734618"}
        arm64_headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:85.0) Gecko/20100101 Firefox/85.0",
            "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate",
            "Referer": "https://armconverter.com/?code=b.eq%20%230x188", "Content-Type": "text/plain;charset=UTF-8",
            "Origin": "https://armconverter.com", "Connection": "close"}
        arm64_json = {"arch": ["arm64", "arm", "thumb"], "asm":arm64_input, "offset": ""}
        Read =requests.post(arm64_url, headers=arm64_headers, cookies=arm64_cookies, json=arm64_json)
        ARM64 = Read.json()
        hex = ARM64['hex']
        hex1 = hex['arm64']
        logo()
        slow(Fore.LIGHTGREEN_EX +"From ARM64 instructions To  HEX : " + Fore.LIGHTCYAN_EX + hex1[1] )
        exit()
