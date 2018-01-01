# pcars2-udp2csv
Ingest UDP stream from Project Cars 2 and write data to CSV file for data visualization

## Introduction

Started playing Project Cars 2 in December 2017 and learned about the UDP stream offering.  After studying the fantastic work of [James Remuscat](https://github.com/jamesremuscat) and his github project called [pcars](https://github.com/jamesremuscat/pcars), I decided to write some code.  I didnt fork the repository, but I did use the code in lots of ways and learned a bunch about handling UDP packets and binary operations in Python.  So my personal thanks and gratitude for his work on this technology.

Original UDP packet breakdown found here:

http://forum.projectcarsgame.com/showthread.php?40113-HowTo-Companion-App-UDP-Streaming

## Caution
I am not a regular Python programmer, so part of this exercise is to improve the code over time.

## Goals
There were several goals for this.
* Improve Python skills
* Engage github and learn how to manage code the right way
* Create a way to perform data visualizations using Google Sheets and/or Pandas dataframes
* Do something meaningful with lots of network traffic
* Improve PC2 skills or car setups using data collected from this scanner

## Data Visualization
After creating the code, running the script and collecting some data, I created a Jupyter page to start visualizing my driving.  Some of those charts were just examples I found on SNS website and other places.  Not sure if those will help either.  Also, I'm continually updating that notebook and that's by design, so I'm just including a snapshot of what you can do with a notebook like that after you get the CSV into a Pandas dataframe.

## Raw Data
Including sample CSV captured on 7 lap race at Brands Hatch with an Audi R8. Real track link can be found [HERE](http://www.brandshatch.co.uk/).

## Running the code
Make sure the binio library is installed, then download both packetdef.py and pcars.py.  Need to change the IP address from a.b.c.d to whatever the IP of the device that will be listening.  I've seen other places where no IP is required, but I couldnt get it to work unless I put that in there for the socket definition.  This is most likely a misunderstanding on my part on how to correctly initialize a socket listener for broadcast UDP traffic.

Finally, run the code:
```
# python pcars.py
```

![Win!](https://github.com/mike4802/pcars2-udp2csv/blob/master/data/bh_win.jpeg)
