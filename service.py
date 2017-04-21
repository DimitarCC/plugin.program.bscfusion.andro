# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import os

__addon__ = xbmcaddon.Addon()
__cwd__ = xbmc.translatePath(__addon__.getAddonInfo('path')).decode('utf-8')
__icon_msg__ = xbmc.translatePath(os.path.join(__cwd__, 'resources', 'bulsat.png')).decode('utf-8')

xbmc.executebuiltin('RunScript(plugin.program.bscfusion, True)')

if __name__ == '__main__':
    monitor = xbmc.Monitor()
    try:
      while True:
        if monitor.waitForAbort(5):
          # Abort was requested while waiting. We should exit
          break
      xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":"false"},"id":1}')
    except Exception as e:
      xbmc.executebuiltin((u'Notification(%s,%s,%s,%s)' % ('Disabling PVR', 'Fail', '5000', __icon_msg__)).encode('utf-8'))
      pass


