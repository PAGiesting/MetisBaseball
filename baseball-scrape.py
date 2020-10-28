#!/usr/bin/python3
# coding: utf-8

# https://www.sports-reference.com/termsofuse.html
# 
# "Notwithstanding other terms of this agreement, we grant the right to 
# teachers to print pages from the Site for distribution to students, 
# provided that proper attribution is given to the URL on the Site where the
# material originated. We also grant the operators of search engines permission
# to use robots to copy materials from the site for the sole purpose of creating
# publicly-available searchable indexes of the materials, but not caches or
# archives of the materials. Search engines are expected to follow the guidelines
# set forth in the robots.txt file that we provide. Except as specifically
# provided in this paragraph, you agree not to use or launch any automated system,
# including without limitation, robots, spiders, offline readers, or like
# devices, that accesses the Site in a manner which sends more request messages
# to the Site server in any given period of time than a typical human would
# normally produce in the same period by using a conventional on-line Web
# browser to read, view, and submit materials. SRL reserves the right to
# revoke the exceptions granted in this paragraph, either generally or in
# specific cases, as well as the right to deny service to any user found
# violating the provisions of this paragraph."
# 
# "You may not frame, capture, harvest, or collect any part of the Site or 
# Content without SRL's advance written consent."

import requests
import time
import pickle

base_url = 'https://baseball-reference.com'
years = list(range(1901-1901,2020-1901))
seasons = ['/leagues/MLB/' + str(year) + '.shtml' for year in range(1901,2020)]

season_html = []
for i in years:
    season_html.append(requests.get(base_url+seasons[i]))
    # per their robots.txt, wait 3 sec between requests
    print(i,season_html[i])
    time.sleep(3.1)

with open('baseball_data.pkl','wb') as cellar:
    pickle.dump(season_html,cellar)
