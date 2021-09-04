# importing vlc module
import vlc

# importing glob module
import glob

# importing time module
import time
  
# media dirctory path
dpath = "/home/pi/Videos/*"
  
# creating vlc media player object
vlcInstance = vlc.Instance()
#media_player = vlc.MediaPlayer()

mediaList = vlcInstance.media_list_new()

mediaListPlayer = vlcInstance.media_list_player_new()
# toggling full screen
#mediaListPlayer.toggle_fullscreen()
  
# get file list
files = glob.glob(dpath)
for file in files:
     mediaList.add_media(file)
    
    
    
# media object
#    media = vlc.Media(file)
  
# setting media to the media player
mediaListPlayer.set_media_list(mediaList)

# start playing video
mediaListPlayer.play()
  
# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)
    
#    value = media_player.get_length()
#    time.sleep(value/1000)