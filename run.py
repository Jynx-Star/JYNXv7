import os, platform, time, sys
os.system('xdg-open https://t.me/jynxhub')
try:
 import requests
except:
	os.system("pip uninstall requests chardet urllib3 idna certifi -y")
        os.system("pip install chardet urllib3 idna certifi requests")

print('\u001b[37m \x1b[38;5;196m->\033[1;97mChecking For Update...')
os.system('git pull --quiet ')
bit = platform.architecture()[0]
if bit == "64bit":
 print('\u001b[37m \x1b[38;5;196m->\033[1;97m64Bit Found')
 time.sleep(2)
 from jynx import ruspt
 ruspt()
 
 
 
if bit == "32bit":
 print('\u001b[37m \x1b[38;5;196m-> \033[1;97m32Bit Found')
 time.sleep(2)
 from jynx import ruspt
 ruspt()
