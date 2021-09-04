# importing vlc module
import vlc
  
# importing time module
import time
  
  
# creating vlc media player object
media_player = vlc.MediaPlayer()
  
# toggling full screen
media_player.toggle_fullscreen()
  
  
# media object
media = vlc.Media("/home/pi/Videos/NEOASPECT.mp4")
  
# setting media to the media player
media_player.set_media(media)
  
# start playing video
media_player.play()
  
# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)