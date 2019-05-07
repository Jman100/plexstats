# Plexstats
Python script that checks the tautulli API and outputs results to an inkyphat e-ink display

# General Setup Guide
1. Install Tautulli (https://tautulli.com/). This software will connect to your plex server and centralize a bunch of stats and stuff. 
2. Get your API key in the tautulli settings page under Web Interface. You'll want to use the get_activity command. The endpoint is /api/v2, for example http://192.168.0.50/api/v2?apikey=YOUR_KEY_HERE&cmd=get_activity. Test this in your browser, it should spit out JSON about what is currently playing on your plex server.
3. Buy and setup your Raspberry Pi and the inkyphat e-ink display, found here: https://shop.pimoroni.com/products/inky-phat. Follow this guide to setup the python library and required things for the display: https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat
4. Insert your API link into the plexstats.py file. Test it by running the file using `python plexstats.py`
5. Type `crontab -e` on your raspberry pi and add a line to run the plexstats.py file every X minutes, however often you want the screen to refresh. An example of the crontab line is in the getting started with inkyphat page linked above

# Disclaimers
- I'm a novice, so this code probably isn't the best. 
- The lines where I write the JSON output to a file and re-check it is so that the screen only updates when there's new data. This could probably be done better
