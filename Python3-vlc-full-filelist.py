# importing vlc module
import vlc

# importing glob module
import glob

# importing time module
import time
  
# media dirctory path
dpath = "/home/pi/Videos/*"
  
# creating vlc media player object
media_player = vlc.MediaPlayer()
  
# toggling full screen
media_player.toggle_fullscreen()
  
# get file list
files = glob.glob(dpath)
for file in files:
    
# media object
    media = vlc.Media(file)
  
# setting media to the media player
    media_player.set_media(media)

# start playing video
    media_player.play()
  
# wait so the video can be played for 5 seconds
# irrespective for length of video
    time.sleep(5)
    
    value = media_player.get_length()
    time.sleep(value/1000+5)
    