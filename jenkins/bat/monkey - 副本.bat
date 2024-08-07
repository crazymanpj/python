rem call gradle -g d:\gradle\.gradle\
call gradle clean
call gradle assembleRelease --stacktrace
echo test
call adb uninstall com.cmcm.gamemoney_sdk
call adb install %WORKSPACE%\cmgameSdkDemo\app\build\outputs\apk\release\app-release.apk"
call adb shell monkey -v -v --throttle 300 --pct-touch 25 --pct-motion 20 --pct-nav 20 --pct-majornav 15 --pct-appswitch 5 --pct-anyevent 5 --pct-trackball 0 --pct-syskeys 0 -p com.cmcm.gamemoney_sdk 3000  -s 1
call adb shell CLASSPATH=/sdcard/monkey.jar:/sdcard/framework.jar exec app_process /system/bin tv.panda.test.monkey.Monkey -p com.cmcm.gamemoney_sdk --uiautomatordfs --running-minutes %time% -v -v