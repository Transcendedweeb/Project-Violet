import pyowm

key = "49f014361226f499993c9afdfc62525c"
OpenWMap = pyowm.OWM(key)
mgr = OpenWMap.weather_manager()

observation = mgr.weather_at_place("Rotterdam, NL")
w = observation.weather

def getTemp():
    global w
    cel = int(w.temperature('celsius')["temp"])
    far = int((int(cel) * 9/5) + 32)
    return str(cel) + " °C, " + str(far) + " °F"

def getSky():
    global w
    sky = w.detailed_status
    return str(sky)

def getWind():
    global w
    speed = str(w.wind()["speed"])

    return speed + " knot"