# Simple python case tracker from the CDC
from lxml import html
import time
import requests as Q
import os

pi = 314
null = 0

while True:

    if pi > null:

        page = Q.get('https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html')
        tree = html.fromstring(page.content)

        USA_Total_Cases = tree.xpath('/html/body/div[7]/main/div[3]/div/div[4]/div[2]/div/div[1]/div/div[2]/ul/li[1]/text()')
        USA_Deaths = tree.xpath('/html/body/div[7]/main/div[3]/div/div[4]/div[2]/div/div[1]/div/div[2]/ul/li[2]/text()')
        #USA_Total_Cases = 1 //this was here just to make sure it was handling events properly
        #USA_Deaths = 1

        time.sleep(60)

        USA_Total_Cases1 = tree.xpath('/html/body/div[7]/main/div[3]/div/div[4]/div[2]/div/div[1]/div/div[2]/ul/li[1]/text()')
        USA_Deaths1 = tree.xpath('/html/body/div[7]/main/div[3]/div/div[4]/div[2]/div/div[1]/div/div[2]/ul/li[2]/text()')

        if USA_Total_Cases1 != USA_Total_Cases:
            print(USA_Total_Cases1)
            os.system('say "Total number of cases has now been updated"')

        if USA_Deaths1 != USA_Deaths:
            os.system('say "Total number of deaths has now been updated"')
            print(USA_Deaths1)

        time.sleep(60)
