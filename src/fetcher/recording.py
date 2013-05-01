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

import datetime

import logging
logger = logging.getLogger(__name__)

TORRENT_TEMPLATE="{titel}_{date}_{time}_{station}_{length}_TVOON_DE.mpg.{quality}.avi.otrkey.torrent"

class Recording(object):
    def __init__(self, titel, time, date, length, station, quality="HD", recurrence="once"):
        self.titel=titel;
        self.datetime=datetime.datetime.strptime("{0} {1}".format(date, time), "%Y-%m-%d %H:%M")
        self.length=length
        self.station=station
        self.quality=quality
        self.recurrence=recurrence
    
    def getTorrentName(self):
        torrentname=TORRENT_TEMPLATE.format(titel=self.titel.replace(" ", "_"), date=self.datetime.strftime("%y.%m.%d"),
                                            time=self.datetime.strftime("%H-%M"),
                                            station=self.station, length=self.length, quality=self.quality)
        return torrentname
        
    def next(self):
        if self.recurrence is None:
            return False
        
        if (self.recurrence=="weekly"):
            delta = datetime.timedelta(days=7)
            self.datetime+=delta
        elif(self.recurrence=="once"):
            self.recurrence=None
            return False
        else:
            raise ValueError("Recurrence '{0}' not known.".format(self.recurrence))
        
        return True