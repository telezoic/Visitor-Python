#utf-8
#python 2.7.10
#Daniel Sifton

import csv
from webdriverplus import WebDriver
from itertools import *

csvfile = raw_input("Enter the name of the csv input file . . .")
loopcall = raw_input("Infinite loop? (yes/no) . . .")
delay = raw_input("Time delay for each URL visit (in seconds) . . . ")
delay = int(delay)

urls = csv.reader(open(csvfile, "rU"))

if loopcall == "yes":

	for url in cycle(urls):

		browser = WebDriver('firefox', reuse_browser=True)

		browser.maximize_window()

		browser.get(url[0])

		time.sleep(delay)

elif loopcall == "no":

	for url in urls:

		browser = WebDriver('firefox', reuse_browser=True)

		browser.maximize_window()

		browser.get(url[0])

		time.sleep(delay)

		browser.quit()

else:

	print "Please enter yes or no to specify the loop . . . "


		
