# -*- coding: utf-8 -*-
import wmi,json
import time

logfile = 'logs_%s.txt' % time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
SW_SHOWNORMAL = 4

#远程执行bat文件
def call_remote_bat(ipaddress,username,password):
    print "call_remote_bat..."
    try:
        #用wmi连接到远程服务器
        conn = wmi.WMI(computer=ipaddress, user=username, password=password)
        print(type(conn))
        for os in conn.Win32_OperatingSystem():
            print os.Caption

        # process_watcher = conn.Win32_Process.watch_for("creation")
        # while True:
        #     new_process = process_watcher()
        #     print new_process.Caption
        process_startup = conn.Win32_ProcessStartup.new()
        process_startup.ShowWindow = SW_SHOWNORMAL
        filename=r"d:\test.bat"   #此文件在远程服务器上
        cmd_callbat=r"cmd /c call %s"%filename
        cmd_callbat2 = "notepad.exe"
        print cmd_callbat
        ret = conn.Win32_Process.Create(CommandLine=cmd_callbat, ProcessStartupInformation=process_startup)  #执行bat文件
        print ret
        # for process in conn.Win32_Process (name="notepad.exe"):
        #     print process.ProcessId, process.Name
        # filename = r"c:\temp\temp.txt"
        # process = conn.Win32_Process
        # process_id, result = process.Create(CommandLine="notepad.exe " + filename)
        # watcher = conn.watch_for (
        #     notification_type="Deletion",
        #     wmi_class="Win32_Process",
        #     delay_secs=1,
        #     ProcessId=process_id
        #     )

        # watcher()
        # print "This is what you wrote:"
        # print open(filename).read()
        return True
    except Exception,e:
        print "error"
        log = open(logfile, 'a')
        log.write(('%s, call bat Failed!\r\n') % ipaddress)
        log.write(str(e))
        log.close()
        return False
    return False

if __name__=='__main__':
    call_remote_bat(ipaddress="10.20.224.45", username="Administrator", password="kingsoft")