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
import datetime


from fetcher import recording

import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)

# http://81.95.11.2/torrents/Tatort_13.04.28_20-15_ard_90_TVOON_DE.mpg.HD.avi.otrkey.torrent

class TestRecording(unittest.TestCase):

    def setUp(self):
        pass


    def test_getTorrentName(self):
        myrecording=recording.Recording("The Simpsons", "20:15", "2013-04-28", "90", "ard")
        torrentname= myrecording.getTorrentName()
        self.assertEqual(torrentname, "The_Simpsons_13.04.28_20-15_ard_90_TVOON_DE.mpg.HD.avi.otrkey.torrent",
                         "Wrong torrent name.")

    def test_getTorrentUrl(self):
        myrecording=recording.Recording("The Simpsons", "20:15", "2013-04-28", "90", "ard")
        torrenturl= myrecording.getTorrentUrl()
        self.assertEqual(torrenturl, "http://81.95.11.2/torrents/13.04.28/The_Simpsons_13.04.28_20-15_ard_90_TVOON_DE.mpg.HD.avi.otrkey.torrent",
                         "Wrong torrent name.")

    def test_datetime(self):
        myrecording=recording.Recording("Tatort", "20:15", "2013-04-28", "90", "ard")
        expected_datetime=datetime.datetime(2013, 4, 28, 20, 15)
        self.assertEqual(myrecording.datetime, expected_datetime, "Wrong Datetime")

    def test_next(self):
        myrecording=recording.Recording("Tatort", "20:15", "2013-04-28", "90", "ard", recurrence="weekly")
        self.assertTrue(myrecording.next())
        expected_datetime=datetime.datetime(2013, 5, 5, 20, 15)
        self.assertEqual(myrecording.datetime, expected_datetime, "Wrong Datetime")

    def test_wrongRecurrence(self):
        myrecording=recording.Recording("Tatort", "20:15", "2013-04-28", "90", "ard", recurrence="something")
        self.assertRaises(ValueError, myrecording.next)
