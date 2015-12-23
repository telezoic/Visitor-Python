# Visitor-Python
A URL driven slideshow in Python - an IR showcase tool for the screen or the wall during your next wine + cheese! 

Load a .csv file of URLs, set the type of loop, set the length of time for each visit. 

###What you need


    import csv  
    import time
    from webdriverplus import WebDriver
    from itertools import *
    

Firefox is the default broswer for webdriverplus, if you want to use something else see the<a href="https://webdriver-plus.readthedocs.org/en/latest/browsers.html"> webdriverplus docs</a>

Webdriver plus requires an up to date version of <a href="http://www.seleniumhq.org/"> selenium </a> to function. Do it this way: `pip install -U selenium` . . . if you please.

###Usage

1: Prep your .csv of URLs (no headers) and place it in the same folder as visitor.py

2: Start up the script and identify the .csv, specify the loop, set the length of time to "delay" at each URL. 

3: Have a glass of wine, a piece of cheese, and enjoy the show. 

4: Bring it down by closing the browser, or if you must, a CTRL + C 



###Road Map

1: ~~Write documentation~~

2: ~~Package as a GUI~~

3: Bundle as an executable

4: Get it working with the library's digital signage




