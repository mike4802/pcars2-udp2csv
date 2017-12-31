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

# setup the csv file for BI
csvfile = packetdef.initcsv()

#--------------------------------------------------------------------#
# begin loop to dissect only TELEMETRY packet for my own BI analysis 

while 1:
  data = s.recv(1400)
  x = packetdef.HEADER.read_dict(BytesIO(data))
  
  # check packet type right here and only continue if it's a telemetry packet
  pType = x['seq_packet'] & 0x3

  # if yes, then call getdata to parse the packet and store it all in 'z'
  if pType == 0:
    z = packetdef.getdata(BytesIO(data))
    # where :
    #  z[0] = HEADER
    #  z[1] = RACE
    #  z[2] = EXTRAS_WEATHER
    #  z[3][0] = RACER #1 - me 

    # format using :  format(var,'.2f') for 2 dec places
    # C to F :     F = C * 1.8 + 32
    LFt = format((( (z[1]['tiretemp'][0]) * 1.8 ) + 32 ), '.2f')
    RFt = format((( (z[1]['tiretemp'][1]) * 1.8 ) + 32 ), '.2f')
    LRt = format((( (z[1]['tiretemp'][2]) * 1.8 ) + 32 ), '.2f')
    RRt = format((( (z[1]['tiretemp'][3]) * 1.8 ) + 32 ), '.2f')

    # Bars are recorded * 100, need to get decimal place back into position
    # Bars to PSI: 1 Bar = 14.5038 PSI 
    b2p = 14.5038
    LFp = format((( z[1]['airPressure'][0]) * b2p / 100) , '.2f') 
    RFp = format((( z[1]['airPressure'][1]) * b2p / 100) , '.2f') 
    LRp = format((( z[1]['airPressure'][2]) * b2p / 100) , '.2f') 
    RRp = format((( z[1]['airPressure'][3]) * b2p / 100) , '.2f') 
  
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

# Format and write new csv row to file for BI analysis
    csvrow = [currentlaptime, lap, track, sector, speedX, LFt, RFt, LRt, RRt, LFp, RFp, LRp, RRp ]
    print csvrow
    csvfile.writerow(csvrow)
