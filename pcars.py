from socket import *
from io import BytesIO
import sys
import binascii
import packetdef

multicast_port  = 5606
multicast_group = "224.0.0.1"
interface_ip    = "a.b.c.d"

# setup the socket
s = socket(AF_INET, SOCK_DGRAM )
s.bind(("", multicast_port ))
mreq = inet_aton(multicast_group) + inet_aton(interface_ip)
s.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, str(mreq))

# setup the csv file for data viz in jupyter
csvfile = packetdef.initcsv()

#--------------------------------------------------------------------#
# begin loop to dissect only TELEMETRY packet for my own data viz analysis 

while 1:
  data = s.recv(1400)
  x = packetdef.HEADER.read_dict(BytesIO(data))
  
  # check packet type right here and only continue if it's a telemetry packet
  # the 0x3 is isolating the last 2 bits of the 8 bits using a bitwise AND on the last 2 bit slots
  # for values 1 and 2.  The bits slots for 1 byte are:  128 64 32 16 8 4 2 1
  pType = x['seq_packet'] & 0x3

  # if yes, then call getdata to parse the packet and store it all in 'z'
  if pType == 0:
    z = packetdef.getdata(BytesIO(data))
    # where :
    #  z[0] = HEADER
    #  z[1] = RACE
    #  z[2] = EXTRAS_WEATHER
    #  z[3][0] = RACER #1 - me 
    #  z[4][0-3] = LF,RF,LR,RR tire TEMPS
    #  z[5][0-3] = LF,RF,LR,RR tire PSI

    # Tire Temps
    LFt = z[4][0] 
    RFt = z[4][1] 
    LRt = z[4][2] 
    RRt = z[4][3] 

    # Tire Pressures
    LFp = z[5][0] 
    RFp = z[5][1]
    LRp = z[5][2] 
    RRp = z[5][3] 
   
    # RACE vars 
    eventremain    = z[1]['eventimeremaining']
    split          = z[1]['splittime']
    currentlaptime = format(z[1]['currentLaptime'], '.3f')
    speedX         = format((225*(z[1]['speed']/100)), '.2f')   # 225*(speed/100)
  
    # EXTRAS_WEATHER vars 
    aird     = z[2]['aeroDamage'] 
    torque   = z[2]['engineTorque'] 
    engspeed = z[2]['engineSpeed'] 

    # RACER_INFO vars, where z[3][0] is me ;) 
    track  = z[3][0]['currentLapDistance'] 
    lap    = z[3][0]['currentLap']
    sector = z[3][0]['sector'] & 0x3

    # Format and write new csv row to file for data viz / analysis
    csvrow = [currentlaptime, lap, track, sector, speedX, LFt, RFt, LRt, RRt, LFp, RFp, LRp, RRp ]
    print csvrow
    csvfile.writerow(csvrow)
