import uiautomator2 as u2
import os
import sys

d = u2.connect('10.12.194.140')
print(d.info)
d.app_uninstall('com.cmcm.gamemoney_sdk')
apkfile = 'http://10.12.129.43:8080/job/gamesdk/96/artifact/cmgameSdkDemo/app/build/outputs/apk/release/app-release.apk'
print(apkfile)
d.app_install(apkfile)
cmd = r'monkey -v -v --throttle 300 --pct-touch 25 --pct-motion 20 --pct-nav 20 --pct-majornav 15 --pct-appswitch 5 --pct-anyevent 5 --pct-trackball 0 --pct-syskeys 0 -p com.cmcm.gamemoney_sdk 3000  -s 1'
print(cmd)
ret = d.adb_shell(cmd)
print(ret)
