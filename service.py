# -*- coding: utf-8 -*-

import xbmc

xbmc.executebuiltin('RunScript(plugin.program.bscfusion, False)')

monitor = xbmc.Monitor()
while not monitor.abortRequested():
  xbmc.sleep(250)

xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":"false"},"id":1}')
