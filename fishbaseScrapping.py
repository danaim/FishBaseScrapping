#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def getSpecies(genus,species):
    browser = webdriver.Firefox()
    browser.get("https://www.fishbase.se")
    time.sleep(5)
    genusElem = browser.find_element(By.ID,'acGenus')
    speciesElem = browser.find_element(By.ID,'acSpecies')
    genusElem.send_keys(genus)
    speciesElem.send_keys(species)
    speciesElem.submit()
    time.sleep(5)
    html = browser.page_source
    time.sleep(5)
    #print(html)
    browser.close()
    return html



"""
'<!-- Start Prior r -->' in htmlpython
start = html.find('<!-- Start Prior r -->') + len('<!-- Start Prior r -->')
end = html.find('<!-- Start vulnerability-->')
substring = html[start:end]
print(substring)
"""

def getPrior(html):
    if '<!-- Start Prior r -->' not in html:
        return "No priors for this species"
    else:
        start = html.find('<!-- Start Prior r -->') + len('<!-- Start Prior r -->')
        end = html.find('<!-- Start vulnerability-->')
        substring = html[start:end]
        start2 = substring.find("Prior r = ") + len("Prior r = ")
        end2 = substring.find(", 95%")
        prior = substring[start2:end2]
        print(prior)



