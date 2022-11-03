import datetime, pytz

def Amsterdam():
    time = datetime.datetime.now().time()
    return time.strftime("%H:%M") + " [CEST]\n"

def NewYork():
    tz_US = pytz.timezone('America/New_York')
    time = datetime.datetime.now(tz_US)
    return time.strftime("%H:%M") + " [EDT]\n"

def Tokyo():
    tz_AS = pytz.timezone('Asia/Tokyo')
    time = time = datetime.datetime.now(tz_AS)
    return time.strftime("%H:%M") + " [JST]\n"