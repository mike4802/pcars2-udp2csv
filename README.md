# pcars2-udp2csv
Ingest UDP stream from Project Cars 2 and write data to CSV file for data visualization

## Introduction

Started playing Project Cars 2 in December 2017 and learned about the UDP stream offering.  After studying the fantastic work of [James Remuscat](https://github.com/jamesremuscat) and his github project called [pcars](https://github.com/jamesremuscat/pcars), I decided to write some code.  I didnt fork the repository, but I did use the code in lots of ways and learned a bunch about handling UDP packets and binary operations in Python.  So my personal thanks and gratitude for his work on this technology.

## Caution
I am not a regular Python programmer.  I will easily win any contest for the nastiest, poor habit and most un-reusable code out there.  So part of this exercise is to see if I can stay interested and motivated enough to try and improve the maturity of what the code should really look like.

## Goals
There were several goals for this.
* Improve Python skills
* Engage github and learn how to manage code the right way
* Create a way to perform data visualizations using Google Sheets and/or Pandas dataframes
* Do something meaningful with lots of network traffic
* Improve PC2 skills or car setups using data collected from this scanner

## Data Visualization
After creating the code, running the script and collecting some data, I created a Jupyter page to start visualizing my driving.  Some of those charts were just examples I found on SNS website and other places.  Not sure if those will help either.

## Raw Data
Including sample CSV captured on 7 lap race at Brands Hatch with an Audi R8. Real track link can be found [HERE](http://www.brandshatch.co.uk/).

## Running the code
Make sure the binio library is installed, then download both packetdef.py and pcars.py.  Need to change the IP address from a.b.c.d to whatever the IP of the device that will be listening.  I've seen other places where no IP is required, but I couldnt get it to work unless I put that in there for the socket definition.  This is most likely a misunderstanding on my part on how to correctly initialize a socket listener for broadcast UDP traffic.

Finally, run the code:
```
# python pcars
```
