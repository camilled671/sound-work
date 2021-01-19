#while True:
    #print("sound level :" +input.sound_level())
    #if input.sound_level()>5:
            #light.set_all(light.rgb(255, 0, 255))
    #else:
        #light.set_all(light.rgb(255, 0, 255))  
#while True:
    #print("light level: " + str(input.light_level()))
    #if input.light_level() >11:
        #music.power_down.play_until_done()
    #else:
        #music.stop_all_sounds()
#while True:
    #print("light level:") + str(input.light_level())
    #if input.light_level() > 11 :
        #music.play_melody("E D C D E E E D D D E G G E D C D E E E E D E D C ", 120)
        #music.set_volume(1000)
    #else :
            #music.stop_all_sounds()
while True:
    print("sound level :" +input.sound_level())
    if input.sound_level()>33: 
        music.play_melody("E D C D E E E D D D E G G E D C D E E E E D E D C ", 120)
    else :
        music.stop_all_sounds()