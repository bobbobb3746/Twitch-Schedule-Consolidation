from tkinter import N, Tk
from tkinter import ttk

import json

# general layout
root = Tk()
root.geometry('800x600')
win = ttk.Frame(root,padding=10)
win.grid()

leftbar = ttk.Frame(win, width=200,padding=10) # frame containing list of all the streamers to watch
leftbar.grid(column=0,row=0)
ttk.Label(leftbar,text="Streamers").grid(column=0,row=0)
with open('streamers.json','r',encoding='utf-8') as streamers: # read list of names of streamers to grab schedules of
    streamerNames = json.load(streamers)['streamers']
    for i in range(len(streamerNames)):
        ttk.Label(leftbar, text=streamerNames[i]).grid(column=0,row=i+1)
streamers.close()

addStreamerFrm = ttk.Frame(win) # data input frame
addStreamerFrm.grid(column=1,row=0,sticky=N)
ttk.Label(addStreamerFrm, text="Streamer name:").grid(column=1,row=0)
streamerEntry = ttk.Entry(addStreamerFrm, width=20)
streamerEntry.grid(column=2,row=0)
def addStreamer():
    ttk.Label(leftbar,text=streamerEntry.get()).grid(column=0)
    rawJson = {}
    with open('streamers.json','r',encoding='utf-8') as streamers: # get streamer names from json file
        rawJson = json.load(streamers)
    streamers.close()
    with open('streamers.json','w',encoding='utf-8') as streamers: # add new streamer and alphabetize list of names
        rawJson['streamers'] += [streamerEntry.get()]
        rawJson['streamers'] = sorted(rawJson['streamers'])
        json.dump(rawJson,streamers)
    streamers.close()
ttk.Button(addStreamerFrm,text="Add streamer",command=addStreamer).grid(column=3,row=0)
root.mainloop()