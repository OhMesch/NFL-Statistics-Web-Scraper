# NFL-Statistics-Web-Scraper
Taking advantage of some prebuild libraries to create a web scraper with the intent of gathering NFL player statistics for analysis.

============
INSTALLATION
============
This repository is dependant on bs4 and requests.
pip install beautifulsoup4
pip install requests

Clone the repository to the desired location. All source files are in the default repro folder. 

=====
USAGE
=====
The driver folder contains examples on using the program. The driverStats.py will gather the nfl stats of every player listed on nfl.com

Running this will create two folders. The logs folder contains a status log generated each time the StatsBuilder class is called. Th
e StatsBuilder class is the main class. The logs contain any errors which occur during stats building.

The PlayerStats folder is created when StatsBuilder is first ran. This folder becomes populated with each nfl player's folder which contains CSVs off all the relevant player stats which can be found on nfl.com

=====
TL:DR
=====
pip install beautifulsoup4
pip install requests

clone repository

Move driverStats.py from drivers/ to same folder as the source files and run. 

The PlayerStats folder will contain a folder for each NFL player full of CSVs of the relevant stat tables.
