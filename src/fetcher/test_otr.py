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
import urllib.error

from . import otr

import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)

# http://81.95.11.2/torrents/Tatort_13.04.28_20-15_ard_90_TVOON_DE.mpg.HD.avi.otrkey.torrent

class TestGetTorrent(unittest.TestCase):

    def setUp(self):
        pass


    def test_getTorrent(self):
        result = otr.fetchTorrent("http://81.95.11.2/torrents/Tatort_13.04.28_20-15_ard_90_TVOON_DE.mpg.HD.avi.otrkey.torrent")
        self.assertTrue(result, "Couldn't fetch torrent.")

    def test_getTorrentNotAvailable(self):
        result = otr.fetchTorrent("http://81.95.11.2/torrents/File_does_not_exist.torrent")
        self.assertFalse(result, "Missing torrent not detected.")

    def test_getTorrentWrongUrl(self):
        self.assertRaises(urllib.error.URLError, otr.fetchTorrent, "http://192.169.3.1/torrents/File_does_not_exist.torrent")
