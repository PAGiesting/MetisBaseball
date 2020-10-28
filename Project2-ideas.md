# Project 2: Regression

Goal: predict a numeric variable using data scraped from websites.

* I plan to scrape both training and testing data. I expect that's what's meant.

##### Standups on Wed or Thurs of Holy Week

Ideas:

* Commercial property values related to contamination, number of different types of environmental hazard sites within one mile of site. Also throw in all the conventional features I can think of: square footage, proximity to an interstate ramp, age of building.
  * EPA, state gov't may be scrapable or may have an API.
  * Scouting report: Train wreck. EPA has an API for future and I saved a link.
* BeerAdvocate
  * Scouting report: Lots of beers, welcome to scrape, but not enough features.
* Petrology - review paper I put in Metis folder
  * Pulled some references, too advanced for regression
* Agriculture - chemical applications, etc.
  * California has a huge database. My random query broke the server. Awesome.
* Stanford Encyclopedia of Philosophy
  * Impossible to find anything to regress.
* TV Tropes
  * ditto
* Homestar Runner Wiki
  * do i even need to check
* jeepforum, jeepz, etc.
  * ditto
* Journals, especially funky old journals like Am Min or Am J Science
  * too hard to figure out in time allotted
* Materials - alloys, semiconductors
  * poked at alloy data, it's too hard to find big wads of it
* Mining
  * where would I go to get 1000 data points with 10 features?
* Space agency data, although a lot of this will be in APIs or the like
  * Exoplanet data
    * http://exoplanet.eu/catalog/, not enough features
    * https://exoplanets.nasa.gov/exoplanet-catalog/, not enough features
    * could I bridge the two? still not enough features, I think
    * http://phl.upr.edu/projects/habitable-exoplanets-catalog/data/database
      * That last is a hard-core database with a zillion defined variable names.
      * Provides a .csv, not suitable for a scraping exercise
  * Star catalogs
    * All are databases
  * Meteorite data... oooh, I know about those
    * databases
    * scrapable catalogs of Martians, lunars, etc. are too small, too few features
* Earthquake data
  * databases
* Baseball stats & drug use or other factors over time
  * Influence of teammates (peers) on batting or pitching performance
  * Age
  * Focus on fast players in the 80s vs other decades
  * Or on the early vs. late 60s. Start with comparing 1962 to 1968. Extend this to finding other years where pitching or hitting (or speed) dominates:
    * WAR for pitchers
    * WAR for hitters
    * Runs scored, etc.
    * Stolen bases, doubles, triples
    * Which ones have the largest contribution to games won for teams in varying years?
    * 1962 is a good year to start because it's the first 162 game season.
    * Predict games won
    * Can I cast retrospective odds for winning WS and map this back onto playoffs?
      * Discuss the "playoffs = crapshoot" hypothesis



World Series ratings data: https://www.baseball-almanac.com/ws/wstv.shtml

ASG ratings data: https://www.baseball-almanac.com/asgbox/asgtv.shtml

Population data: https://www.multpl.com/united-states-population/table/by-year

#### Initial thoughts on looking at hitting data

Clearly there is some oscillation in several statistics over time.

Some stat vs. stat plots are stratified / bimodal.



#### Notes early in regression

Go back and do a correlation assessment of attendance versus each of my flagship & on deck variables. Compare this to the coefficients from a LassoCV regression.

https://stackoverflow.com/questions/29432629/plot-correlation-matrix-using-pandas

Pick only about 4 variables for poly=2 features:

4 linear, 4 squared, 3 + 2 + 1 = 6 cross, 1 intercept = 15 features