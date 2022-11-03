import pyautogui as keys
import violetAi as AI
import violetWeather as weather
import violetMetrix, violetTimes

def getCommand(line, input):
    if "full mute" in input:
        AI.violet_text_list[0] = "Request\ncompleted!" # 17 values per line
        violetMetrix.pog_array[0] = "mssboard"
        keys.hotkey("ctrl", "alt", "pageup")
    
    elif "mute" in input or "unmute" in input:
        AI.violet_text_list[0] = "Request\ncompleted!" # 17 values per line
        violetMetrix.pog_array[0] = "mssboard"
        keys.hotkey("ctrl", "alt", "pagedown")

    elif "instant replay" in input:
        AI.violet_text_list[0] = "Instant replay\nsaved!" # 17 values per line
        violetMetrix.pog_array[0] = "mssboard"
        keys.hotkey("ctrl", "shift", "s")

    elif "showtime" in input:
        AI.violet_text_list[0] = "Local time:\n"+violetTimes.Amsterdam() + "\nNew York:\n" + violetTimes.NewYork() + "\nTokyo: \n"+ violetTimes.Tokyo()
        violetMetrix.pog_array[0] = "mssboard"
    
    elif "show weather" in input:
        AI.violet_text_list[0] = "Temperature:\n"+weather.getTemp() + "\n\nSky report:\n" + weather.getSky() + "\n\nWindspeed:\n" + weather.getWind()
        violetMetrix.pog_array[0] = "mssboard"

def getTextCommand(line, input):
    empty_list = []
    awnser = input
    with open("AIconfig\\mss_text.txt") as file:
        for line1 in file:
            line1 = line1.replace("[", "").replace("]", "").strip()
            empty_list.append(line1)

        print(empty_list)

        counter = 1
        for item in empty_list:
            if item in awnser:
                final_text = str(empty_list[counter]).replace("\\n", ("\n"))
                AI.violet_text_list[0] = final_text
                violetMetrix.pog_array[0] = "mssboard"
                break
            counter += 1

        file.close()