# Copyright (C) 2013 Sven Klomp (mail@klomp.eu)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301, USA.

import json

from . import recording

import logging
logger = logging.getLogger(__name__)

def convertRecording2BPO(recording):
    bpo={}
    bpo["titel"]=recording.titel
    bpo["date"]=recording.datetime.strftime("%Y-%m-%d")
    bpo["time"]=recording.datetime.strftime("%H:%M")
    bpo["length"]=recording.length
    bpo["station"]=recording.station
    bpo["quality"]=recording.quality
    bpo["recurrence"]=recording.recurrence
    return bpo

def convertBPO2Recording(bpo):
    myrecording=recording.Recording(bpo["titel"], bpo["time"], bpo["date"], bpo["length"], bpo["station"],
                                    bpo["quality"], bpo["recurrence"])
    return myrecording

def save(config, filename):
    bpo={ "recordings": []}
    for key in config.keys():
        if key=="recordings":
            for myrecording in config["recordings"]:
                if (myrecording.recurrence is not None):
                    bpo["recordings"].append(convertRecording2BPO(myrecording))
        else:
            bpo[key]=config[key]  
        
    fp=open(filename, "w")
    json.dump(bpo, fp, indent=4)


def load(filename):
    config = {"recordings" : []}
    
    fp=open(filename)
    bpo=json.load(fp)
    
    for key in bpo.keys():
        if (key=="recordings"):
            for bpo_recording in bpo[key]:
                config[key].append(convertBPO2Recording(bpo_recording))
        else:
            config[key]=bpo[key]
    return config