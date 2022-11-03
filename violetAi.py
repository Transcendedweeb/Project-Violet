import os, violetCommands, violetMetrix, datetime

violet_tuple = ("violet", "violets", "pilots", "pilot", "toilets", "toilet", "violin", "violins", "find", "favorite")
violet_text_list = [""]



def lnkCMD(str):
    str = str.replace(" ","_").strip()
    
    dir = "AIconfig\\modules\\"
    try:
        os.startfile(dir+str)
        violet_text_list[0] = "Request\ncompleted!" # 17 values per line
        violetMetrix.pog_array[0] = "mssboard"
        print("OPENING...")
        log_file = open("AIconfig\\logs.txt", "a")
        moment_in_time = str(datetime.datetime.now().time())
        log_file.write("["+moment_in_time[0:7]+"] " + "Open command acknowledge.\n\n")
        log_file.close()
    except:
        # give not found screen (Error 003)
        # logs maybe?
        print("Error 003: no module found for "+str+" check the directory "+dir)
        log_file = open("AIconfig\\logs.txt", "a")
        moment_in_time = str(datetime.datetime.now().time())
        log_file.write("["+moment_in_time[0:7]+"] " + "Error 003: no module found for "+str+" check the directory "+dir+"\n\n")
        log_file.close()
        



def decoder(input):
    global violet_tuple
    input = input.lower()

    if "carlow" in input:
        input = input.replace("w", "")
    
    for word in violet_tuple:
        if word in input:
            counter = input.find("violet")+7
            input = input[counter::]

            #input = input.replace(" ", "_")
            cmd_found = False
            with open("AIconfig\\cmd_config.txt") as f:
                for line in f:
                    line2 = line.lower()

                    print("Starting new line")
                    print(line2)
                    print(input)
                    
                    # line contains link command
                    if ".lnk" in line2:
                        line2 = line2.replace(".lnk", "").strip()
                        
                        if line2 in input:
                            log_file = open("AIconfig\\logs.txt", "a")
                            moment_in_time = str(datetime.datetime.now().time())
                            log_file.write("["+moment_in_time[0:7]+"] " + "made a connection with .lnk command\n\n")
                            log_file.close()
                            lnkCMD(line)
                            break
                        else:
                            print("not equal")
                    
                    # line contains url command
                    elif ".url" in line2:
                        line2 = line2.replace(".url", "").strip()
                        
                        if line2 in input:
                            log_file = open("AIconfig\\logs.txt", "a")
                            moment_in_time = str(datetime.datetime.now().time())
                            log_file.write("["+moment_in_time[0:7]+"] " + "made a connection with .cmd command\n\n")
                            log_file.close()
                            lnkCMD(line)
                            break
                        else:
                            print("not equal")

                    elif ".key" in line2:
                        line2 = line2.replace(".key", "").strip()

                        # line contains reactive command
                        if line2 in input:
                            log_file = open("AIconfig\\logs.txt", "a")
                            moment_in_time = str(datetime.datetime.now().time())
                            log_file.write("["+moment_in_time[0:7]+"] " + "made a connection with .key command\n\n")
                            log_file.close()
                            violetCommands.getCommand(line2, input)
                            break
                    
                    elif ".cmm" in line2:
                        line2 = line2.replace(".cmm", "").strip()

                        if line2 in input:
                            log_file = open("AIconfig\\logs.txt", "a")
                            moment_in_time = str(datetime.datetime.now().time())
                            log_file.write("["+moment_in_time[0:7]+"] " + "made a connection with .cmm command\n\n")
                            log_file.close()
                            violetCommands.getTextCommand(line2, input)
                            break

                    else:
                        # violet activated, but no command given or understood (Error 002)
                        # maybe logs?
                        print("Error 002: violet activated, but no command given or understood")
                        log_file = open("AIconfig\\logs.txt", "a")
                        moment_in_time = str(datetime.datetime.now().time())
                        log_file.write("["+moment_in_time[0:7]+"] " + "Error 002: Violet activated, but no command given or understood\n\n")
                        log_file.close()
                    
                    print("------------------------------------------")

                f.close()

        
        


# print("\n\n\n\n\n")
# decoder("whello violet open sprites if you will")