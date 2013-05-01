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

import unittest

from fetcher import config
from fetcher import recording

import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)


class TestConfigRecording(unittest.TestCase):

    def setUp(self):
        pass


    def test_recording2BPO(self):
        myrecording=recording.Recording("The Simpsons", "20:15", "2013-04-28", "90", "ard")
        expected_bpo = {"titel": "The Simpsons", "time": "20:15", "date": "2013-04-28", "length": "90",
                        "station": "ard", "quality": "HD", "recurrence": "once"}
 
        bpo= config.convertRecording2BPO(myrecording)
        self.assertEqual(bpo, expected_bpo, "Basic Python Objects differ.")
                         
    def test_BPO2Recording(self):
        expected_recording=recording.Recording("The Simpsons", "20:15", "2013-04-28", "90", "ard")
        bpo = {"titel": "The Simpsons", "time": "20:15", "date": "2013-04-28", "length": "90",
               "station": "ard", "quality": "HD", "recurrence": "once"}
        myrecording=config.convertBPO2Recording(bpo);
        self.assertEqual(myrecording.getTorrentName(), expected_recording.getTorrentName(), "Recordings differ.")

    def test_saveConfig(self):
        myrecording=recording.Recording("The Simpsons", "20:15", "2013-04-28", "90", "ard")
        myrecording2=recording.Recording("Tatort", "20:15", "2013-04-28", "90", "ard", recurrence="weekly")
        myconfig={"recordings": [myrecording, myrecording2, myrecording]}
        
        config.save(myconfig, "/tmp/fetcher.cfg")
        
        
    def test_loadConfig(self):
        myconfig = config.load("/tmp/fetcher2.cfg")
        config.save(myconfig, "/tmp/fetcher3.cfg")
        
    
        
        
        
        
