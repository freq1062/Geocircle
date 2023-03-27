# Geocircle

Program written in Python to AFK eggs, buddies, etc. in Pokemon Go; basically I read that the max displacement was about 300-400m/ 4 minutes and decided that a circle was the best shape that had equal distance for whatever time the game checked my displacement. 

The speed limit was also calculated to be about 1.4 ms^-1 achievable, but theoretically it should have been possible to do 2.9ms^-1. 

Kind of scuffed, basically I had the program MouseMover.py move my mouse and type the calculated coordinates from Geocircle.py into another spoofing program called Bermuda(https://github.com/arevi/bermuda), then I had my phone plugged into my computer and would just have the eggs.

Also written for my SL Math Internal Assessment. 

Limitations: Although if you actually wanted to use the coordinates I found that r=350m is ideal, making a circle that has radius >1/2 the radius of the Earth makes the circle go all wonky to the right. Not sure what's causing this issue, I used the Haversine formula to derive everything so who knows. 

In addition, since I used the Haversine formula it is off by however much the Earth is actually an ellipsoid, but that's also a minor issue and saves a ton of processing power. Easiest ellipsoid formula I found was Vincenty's formulae, which have their own limitations near the poles, etc.
