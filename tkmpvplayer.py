import tkinter as tk
import mpv
import sys
import os
try:
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

videos = {"VIDEO 1": "vid_encrypted.mp4",
          "VIDEO 2": "This is it.mp3"}


def play_pause(event):
    if not player.pause:
        player.pause = True
    else:
        player.pause = False

def play(key, path):
    player.demuxer_lavf_o=f"decryption_key={key}"#76a6c65c5ea762046bd749a2e632ccbb"
    
    player.play(path)#('vid_encrypted.mp4')


##def handlePropertyChange(name,value):
##    print('property change',name,value)
##    root.title(str(value))
if __name__ == "__main__":
    key, path = sys.argv[1:]
    root=tk.Tk()
    root.title("hi")
    root.state('zoomed')

    player = mpv.MPV(wid=str(int(root.winfo_id())), loop=False)
    if os.path.exists(path):
        play(key, path)
        root.mainloop()
    else:
        print("Video path not found")
    ##player.observe_property('time-pos', handlePropertyChange)

    print('calling player.terminate.')
    player.terminate()
    print('terminate player.returned.')

