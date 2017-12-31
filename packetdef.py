# packet.py
# define the binio structures for the UDP packet
import binio
import datetime  
import csv

# timing chart for in-game UDP packet send rate
#UDP off
#UDP 1 60/sec (16ms)
#UDP 2 50/sec (20ms)
#UDP 3 40/sec (25ms)
#UDP 4 30/sec (32ms)
#UDP 5 20/sec (50ms)
#UDP 6 15/sec (66ms)
#UDP 7 10/sec (100ms)
#UDP 8 05/sec (200ms)
#UDP 9 01/sec (1000ms)


HEADER = binio.new([
  (1, binio.types.t_u16,  "buildVersion"),
  (1, binio.types.t_u8,   "seq_packet"),
])

RACE = binio.new([
  (1, binio.types.t_u8,        "game_state"),
  (1, binio.types.t_int8,      "viewedRacerIndex"),
  (1, binio.types.t_int8,      "numRacers"),
  (1, binio.types.t_u8,        "unfThrottle"),
  (1, binio.types.t_u8,        "unfBrake"),
  (1, binio.types.t_int8,      "unfsteering"),
  (1, binio.types.t_u8,        "unfClutch"),
  (1, binio.types.t_u8,        "raceFlags"),
  (1, binio.types.t_u8,        "raceLaps"),
  (1, binio.types.t_float32,   "bestLaptime"),
  (1, binio.types.t_float32,   "lastLaptime"),
  (1, binio.types.t_float32,   "currentLaptime"),
  (1, binio.types.t_float32,   "splittimeahead"),
  (1, binio.types.t_float32,   "splittimebehind"),
  (1, binio.types.t_float32,   "splittime"),
  (1, binio.types.t_float32,   "eventimeremaining"),
  (1, binio.types.t_float32,   "personalfastlap"),
  (1, binio.types.t_float32,   "worldsfastlap"),
  (1, binio.types.t_float32,   "currentsector1time"),
  (1, binio.types.t_float32,   "currentsector2time"),
  (1, binio.types.t_float32,   "currentsector3time"),
  (1, binio.types.t_float32,   "fastestsector1time"),
  (1, binio.types.t_float32,   "fastestsector2time"),
  (1, binio.types.t_float32,   "fastestsector3time"),
  (1, binio.types.t_float32,   "personalfastestsector1time"),
  (1, binio.types.t_float32,   "personalfastestsector2time"),
  (1, binio.types.t_float32,   "personalfastestsector3time"),
  (1, binio.types.t_float32,   "worldfastestsector1time"),
  (1, binio.types.t_float32,   "worldfastestsector2time"),
  (1, binio.types.t_float32,   "worldfastestsector3time"),
  (1, binio.types.t_u16,       "joypad"),
  (1, binio.types.t_u8,        "highestFlag"),
  (1, binio.types.t_u8,        "pitInfo"),
# 
# car state
# 
  (1, binio.types.t_int16,   "oilTempCelsius"),
  (1, binio.types.t_u16,     "oilPressureKPa"),
  (1, binio.types.t_int16,   "waterTempCelsius"),
  (1, binio.types.t_u16,     "waterPressureKPa"),
  (1, binio.types.t_u16,     "fuelPressureKPa"),
  (1, binio.types.t_u8,      "carFlags"),
  (1, binio.types.t_u8,      "fuelCapacity"),
  (1, binio.types.t_u8,      "brake"),
  (1, binio.types.t_u8,      "throttle"),
  (1, binio.types.t_u8,      "clutch"),
  (1, binio.types.t_int8,    "steering"),
  (1, binio.types.t_float32, "fuelLevel"),
  (1, binio.types.t_float32, "speed"),
  (1, binio.types.t_u16,     "rpm"),
  (1, binio.types.t_u16,     "maxRpm"),
  (1, binio.types.t_u8,      "gearNumGears"),
  (1, binio.types.t_u8,      "boostAmount"),
  (1, binio.types.t_int8,    "enforcedPitStopLap"),
  (1, binio.types.t_u8,      "crashState"),

    # Motion and device
  (1, binio.types.t_float32, "odometerKM"),
  (1, binio.types.t_float32, "orientationX"),
  (1, binio.types.t_float32, "orientationY"),
  (1, binio.types.t_float32, "orientationZ"),
  (1, binio.types.t_float32, "localVelocityX"),
  (1, binio.types.t_float32, "localVelocityY"),
  (1, binio.types.t_float32, "localVelocityZ"),
  (1, binio.types.t_float32, "worldVelocityX"),
  (1, binio.types.t_float32, "worldVelocityY"),
  (1, binio.types.t_float32, "worldVelocityZ"),
  (1, binio.types.t_float32, "angularVelocityX"),
  (1, binio.types.t_float32, "angularVelocityY"),
  (1, binio.types.t_float32, "angularVelocityZ"),
  (1, binio.types.t_float32, "localAccelerationX"),
  (1, binio.types.t_float32, "localAccelerationY"),
  (1, binio.types.t_float32, "localAccelerationZ"),
  (1, binio.types.t_float32, "worldAccelerationX"),
  (1, binio.types.t_float32, "worldAccelerationY"),
  (1, binio.types.t_float32, "worldAccelerationZ"),
  (1, binio.types.t_float32, "extentsCentreX"),
  (1, binio.types.t_float32, "extentsCentreY"),
  (1, binio.types.t_float32, "extentsCentreZ"),

  #TIRES
  # access with list_name['tiretemp'][x] where x=0,3 for each tire
  (4, binio.types.t_u8,      "tireFlag"),
  (4, binio.types.t_u8,      "tireTerrain"),
  (4, binio.types.t_float32, "tireY"),
  (4, binio.types.t_float32, "tirerps"),
  (4, binio.types.t_float32, "tireslipspeed"),
  (4, binio.types.t_u8,      "tiretemp"),
  (4, binio.types.t_u8,      "tyreGrip"),
  (4, binio.types.t_float32, "tyreHeightAboveGround"),
  (4, binio.types.t_float32, "tyreLateralStiffness"),
  (4, binio.types.t_u8,      "tyreWear"),
  (4, binio.types.t_u8,      "brakeDamage"),
  (4, binio.types.t_u8,      "suspensionDamage"),
  (4, binio.types.t_int16,   "brakeTempCelsius"),
  (4, binio.types.t_u16,     "tyreTreadTemp"),
  (4, binio.types.t_u16,     "tyreLayerTemp"),
  (4, binio.types.t_u16,     "tyreCarcassTemp"),
  (4, binio.types.t_u16,     "tyreRimTemp"),
  (4, binio.types.t_u16,     "tyreInternalAirTemp"),
  (4, binio.types.t_float32, "wheelLocalPositionY"),
  (4, binio.types.t_float32, "rideHeight"),
  (4, binio.types.t_float32, "suspensionTravel"),
  (4, binio.types.t_float32, "suspensionVelocity"),
  (4, binio.types.t_u16,     "airPressure"),
])

EXTRAS_WEATHER = binio.new([
## extras and weather
  (1, binio.types.t_float32, "engineSpeed"),
  (1, binio.types.t_float32, "engineTorque"),
  (1, binio.types.t_u8,      "aeroDamage"),
  (1, binio.types.t_u8,      "engineDamage"),
  (1, binio.types.t_int8,    "ambientTemperature"),
  (1, binio.types.t_int8,    "trackTemperature"),
  (1, binio.types.t_u8,      "rainDensity"),
  (1, binio.types.t_int8,    "windSpeed"),
  (1, binio.types.t_int8,    "windDirectionX"),
  (1, binio.types.t_int8,    "windDirectionY"),
])


RACER_INFO = binio.new([
  (1, binio.types.t_int16,   "worldPositionX"),
  (1, binio.types.t_int16,   "worldPositionY"),
  (1, binio.types.t_int16,   "worldPositionZ"),
  (1, binio.types.t_u16,     "currentLapDistance"),
  (1, binio.types.t_u8,      "racePosition"),
  (1, binio.types.t_u8,      "lapsCompleted"),
  (1, binio.types.t_u8,      "currentLap"),
  (1, binio.types.t_u8,      "sector"),
  (1, binio.types.t_float32, "lastSectorTime"),
])

def getdata(buf):
  # read in each binio structure: header, race telemetry, extras,
  #   then loop over and store all the individual racer data in a list called 'c'

  i = HEADER.read_dict(buf)
  a = RACE.read_dict(buf)
  b = EXTRAS_WEATHER.read_dict(buf)
  c = []
  tiretemp = []
  tirepsi = []

  for _ in range(0,56):
    each = RACER_INFO.read_dict(buf)
    c.append(each)
  
  # make a list of tire temps/pressures
  # C to F :     F = C * 1.8 + 32
  # Bars are recorded * 100, need to get decimal place back into position
  # Bars to PSI: 1 Bar = 14.5038 PSI

  for i in range(0,4):
    temp = format((( (a['tiretemp'][i]) * 1.8 ) + 32 ), '.2f')
    tiretemp.append(temp)
    b2p = 14.5038
    psi =  format((( a['airPressure'][i]) * b2p / 100) , '.2f')
    tirepsi.append(psi)

  return(i,a,b,c,tiretemp,tirepsi)


def initcsv():
# setup a file to write to based on today's date
# and insert the first row as the header before entering the main loop
  mytime = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
  fname = mytime + '.csv'
  myfile = open(fname, 'w')
  writer = csv.writer(myfile)
  csvheader = ['time', 'lap', 'track', 'sector', 'speed', 'lft', 'rft', 'lrt', 'rrt', 'lfp', 'rfp', 'lrp', 'rrp' ]
  writer.writerow(csvheader)

# after CSV file instantiated and primed, return the new csv writer object
  return (writer)
