################################################################################
#      This file is part of OpenELEC - http://www.openelec.tv
#      Copyright (C) 2009-2013 Stephan Raue (stephan@openelec.tv)
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with OpenELEC.tv; see the file COPYING.  If not, write to
#  the Free Software Foundation, 51 Franklin Street, Suite 500, Boston, MA 02110, USA.
#  http://www.gnu.org/copyleft/gpl.html
################################################################################

import os
import sys
import xbmcaddon

__settings__      = xbmcaddon.Addon(id = 'driver.dvb.sundtek-mediatv')
__cwd__           = __settings__.getAddonInfo('path')
__resources_lib__ = xbmc.translatePath(os.path.join(__cwd__, 'resources', 'lib'))
__settings_xml__  = xbmc.translatePath(os.path.join(__cwd__, 'resources', 'settings.xml'))

__mediaclient__   = xbmc.translatePath(os.path.join(__cwd__, 'bin', 'mediaclient'))
__ld_preload__    = xbmc.translatePath(os.path.join(__cwd__, 'lib', 'libmediaclient.so'))
__mediaclient_e__ = 'LD_PRELOAD=' + __ld_preload__ + ' ' + __mediaclient__ + ' -e'

if __name__ == "__main__" and len(sys.argv) == 2 and sys.argv[1] == 'refresh_tuners':
  sys.path.append(__resources_lib__)
  from functions import refresh_sundtek_tuners
  refresh_sundtek_tuners(__settings_xml__, __mediaclient_e__)
  __settings__.openSettings()
