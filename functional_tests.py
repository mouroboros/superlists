from selenium import webdriver
import os


browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title

