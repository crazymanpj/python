# -*- encoding=utf8 -*-
__author__ = "ADMIN"

from airtest.core.api import *

auto_setup(__file__)
istest = False
# istest = False
isapp = False
istest_pre = False
isuc = True

def stop_qtt():
    stop_app('com.qtt.game.gamecenter.predevtool')
    stop_app('com.jifen.qukan')
    stop_app('com.heitu.game.kxxnc')
    stop_app('com.nuozhen.demo')
    

def watch_window(): 
    if exists(Template(r"tpl1569811555730.png", record_pos=(0.015, -0.108), resolution=(1080, 2160))):
        touch(Template(r"tpl1569811568336.png", record_pos=(-0.159, 0.345), resolution=(1080, 2160)))
        
    if exists(Template(r"tpl1571045818416.png", record_pos=(0.005, -0.061), resolution=(1080, 2160))):
        touch(Template(r"tpl1571910355905.png", record_pos=(-0.156, 0.093), resolution=(1080, 2220)))

def close():
    if exists(Template(r"tpl1569813099093.png", record_pos=(0.422, -0.759), resolution=(1080, 2160))):
        touch(Template(r"tpl1569813099093.png", record_pos=(0.422, -0.759), resolution=(1080, 2160)))

def isneedupdate():
    if exists(Template(r"tpl1569815395964.png", record_pos=(-0.012, 0.107), resolution=(1080, 2160))):
        touch(Template(r"tpl1569815395964.png", record_pos=(-0.012, 0.107), resolution=(1080, 2160)))
        print('升级作物成功')
    
    if exists(Template(r"tpl1569815395964.png", record_pos=(-0.012, 0.107), resolution=(1080, 2160))):
        close()
        
def perpare_start():
    if exists(Template(r"tpl1569229262515.png", record_pos=(-0.017, 0.515), resolution=(1080, 2160))):
        swipe(Template(r"tpl1569229262515.png", record_pos=(-0.017, 0.515), resolution=(1080, 2160)), vector=[0, 0.862])
    
    if exists(Template(r"tpl1571303055427.png", record_pos=(0.434, -0.753), resolution=(1080, 2160))):
        swipe(Template(r"tpl1571303055427.png", record_pos=(0.434, -0.753), resolution=(1080, 2160)), vector=[0, 0.862])

def case_entergame():
    if isapp is False:
        if istest_pre is True:
            touch(Template(r"tpl1569223545958.png", record_pos=(0.191, 0.769), resolution=(1080, 2160)))
            touch(Template(r"tpl1569223557771.png", record_pos=(-0.005, -0.111), resolution=(1080, 2160)))
        else:
            touch(Template(r"tpl1578368451515.png", record_pos=(0.0, 0.78), resolution=(1080, 2220)))
            touch(Template(r"tpl1578368561740.png", record_pos=(0.002, -0.447), resolution=(1080, 2220)))
    else:
        touch(Template(r"tpl1582517061329.png", record_pos=(0.006, 0.777), resolution=(1080, 2220)))

        
    sleep(10)
    if exists(Template(r"tpl1569227868846.png", record_pos=(0.353, -0.341), resolution=(1080, 2160))):
        touch(Template(r"tpl1569227868846.png", record_pos=(0.353, -0.341), resolution=(1080, 2160)))  
    perpare_start()
    if exists(Template(r"tpl1569550668511.png", record_pos=(0.002, 0.022), resolution=(1080, 2160))):
        if exists(Template(r"tpl1571984899964.png", record_pos=(0.22, 0.418), resolution=(1080, 2160))):
            touch(Template(r"tpl1571984948676.png", record_pos=(0.189, 0.548), resolution=(1080, 2160)))
            if exists(Template(r"tpl1571984963248.png", record_pos=(-0.001, 0.344), resolution=(1080, 2160))):
                touch(Template(r"tpl1571984963248.png", record_pos=(-0.001, 0.344), resolution=(1080, 2160)))
        touch(Template(r"tpl1569550687452.png", record_pos=(0.452, -0.834), resolution=(1080, 2160)))
    if exists(Template(r"tpl1573197581557.png", record_pos=(-0.002, -0.045), resolution=(1080, 2160))):
        touch(Template(r"tpl1573197599700.png", record_pos=(0.424, -0.633), resolution=(1080, 2160)))
    if exists(Template(r"tpl1569227765016.png", record_pos=(0.003, -0.056), resolution=(1080, 2160))):
        touch(Template(r"tpl1569227804931.png", record_pos=(0.356, -0.41), resolution=(1080, 2160)))
        
    if exists(Template(r"tpl1579416621271.png", record_pos=(-0.003, -0.013), resolution=(1080, 2220))):
        touch(Template(r"tpl1579416635592.png", record_pos=(-0.011, 0.433), resolution=(1080, 2220)))
    if exists(Template(r"tpl1579416776745.png", record_pos=(0.013, -0.106), resolution=(1080, 2220))):
        touch(Template(r"tpl1579416793313.png", record_pos=(0.446, -0.68), resolution=(1080, 2220)))



    assert_exists(Template(r"tpl1569229693822.png", record_pos=(-0.378, -0.544), resolution=(1080, 2160)), "进入游戏正常")
    
    
    
def case_strengthen():
    #案例：强化种子
    touch(Template(r"tpl1569229982563.png", record_pos=(-0.001, 0.691), resolution=(1080, 2160)))
    if exists(Template(r"tpl1569229997359.png", record_pos=(0.15, 0.587), resolution=(1080, 2160))):
        touch(Template(r"tpl1569229997359.png", record_pos=(0.15, 0.587), resolution=(1080, 2160)))
    # touch(Template(r"tpl1569230031999.png", record_pos=(-0.009, 0.065), resolution=(1080, 2160)), times=10)
    touch(Template(r"tpl1571382378253.png", record_pos=(-0.068, 0.122), resolution=(1080, 2160)), times=10)

    touch(Template(r"tpl1569230067847.png", record_pos=(0.246, 0.727), resolution=(1080, 2160)))
    watch_window()
    
def case_steal_veg():
    #案例：偷菜
    touch(Template(r"tpl1569226674803.png", record_pos=(-0.1, -0.781), resolution=(1080, 2160)))
    assert_exists(Template(r"tpl1569230459676.png", record_pos=(0.303, 0.516), resolution=(1080, 2160)), "偷菜界面显示正常")

    if exists(Template(r"tpl1569230459676.png", record_pos=(0.303, 0.516), resolution=(1080, 2160))):
        if exists(Template(r"tpl1569226686159.png", record_pos=(0.292, -0.232), resolution=(1080, 2160))):
            touch(Template(r"tpl1569226686159.png", record_pos=(0.292, -0.232), resolution=(1080, 2160)))

            if exists(Template(r"tpl1569814655908.png", record_pos=(0.014, 0.836), resolution=(1080, 2160))):
                print('次数已用完')
            else:
                touch(Template(r"tpl1569226696737.png", record_pos=(0.028, 0.729), resolution=(1080, 2160)))
                sleep(5)
                touch(Template(r"tpl1569226707564.png", record_pos=(-0.166, 0.343), resolution=(1080, 2160)))
                touch(Template(r"tpl1569226719096.png", record_pos=(-0.368, 0.725), resolution=(1080, 2160)))
        touch(Template(r"tpl1569226734695.png", record_pos=(0.408, -0.753), resolution=(1080, 2160)))
        
def case_watering():
    #案例：同城浇水
    touch(Template(r"tpl1569468305831.png", record_pos=(0.446, -0.241), resolution=(1080, 2160)))

    if exists(Template(r"tpl1569814398683.png", record_pos=(0.282, -0.443), resolution=(1080, 2160))):
        close()
    elif exists(Template(r"tpl1569468319411.png", record_pos=(0.281, -0.375), resolution=(1080, 2160))):
        touch(Template(r"tpl1569468319411.png", record_pos=(0.281, -0.375), resolution=(1080, 2160)))
        touch(Template(r"tpl1569468329685.png", record_pos=(0.023, 0.715), resolution=(1080, 2160)))
        touch(Template(r"tpl1569468340533.png", record_pos=(-0.17, 0.381), resolution=(1080, 2160)))
        touch(Template(r"tpl1569468355549.png", record_pos=(-0.363, 0.734), resolution=(1080, 2160)))
        touch(Template(r"tpl1569468366030.png", record_pos=(0.417, -0.689), resolution=(1080, 2160)))     
    close()
        
def case_prop():
    #道具商店
    if istest == True:
        touch(Template(r"tpl1569551456567.png", record_pos=(0.271, 0.705), resolution=(1080, 2160)))
        touch(Template(r"tpl1569550573375.png", record_pos=(-0.194, -0.067), resolution=(1080, 2160)))
        watch_window()
        touch(Template(r"tpl1569550573375.png", record_pos=(-0.194, -0.067), resolution=(1080, 2160)))
        watch_window()
        touch(Template(r"tpl1569550573375.png", record_pos=(-0.194, -0.067), resolution=(1080, 2160)))
        watch_window()
        touch(Template(r"tpl1569811498784.png", record_pos=(0.019, -0.555), resolution=(1080, 2160)))
        touch(Template(r"tpl1569811511067.png", record_pos=(-0.194, -0.039), resolution=(1080, 2160)))
        watch_window()
        touch(Template(r"tpl1569811607811.png", record_pos=(0.29, -0.55), resolution=(1080, 2160)))
        touch(Template(r"tpl1569811647039.png", record_pos=(-0.204, -0.041), resolution=(1080, 2160)))
        watch_window()
        touch(Template(r"tpl1569811902474.png", record_pos=(-0.386, 0.706), resolution=(1080, 2160)))
        #收集种子
        touch(Template(r"tpl1569811981828.png", record_pos=(-0.276, 0.755), resolution=(1080, 2160)))
        touch(Template(r"tpl1569812011175.png", record_pos=(0.174, -0.485), resolution=(1080, 2160)))
        touch(Template(r"tpl1569812018730.png", record_pos=(-0.156, -0.489), resolution=(1080, 2160)))
        touch(Template(r"tpl1569812063449.png", record_pos=(0.12, -0.205), resolution=(1080, 2160)))
        if exists(Template(r"tpl1569812051084.png", record_pos=(-0.002, 0.344), resolution=(1080, 2160))):
            touch(Template(r"tpl1569812051084.png", record_pos=(-0.002, 0.344), resolution=(1080, 2160)))
        isneedupdate()
        touch(Template(r"tpl1569812087478.png", record_pos=(0.125, 0.097), resolution=(1080, 2160)))
        if exists(Template(r"tpl1569812051084.png", record_pos=(-0.002, 0.344), resolution=(1080, 2160))):
            touch(Template(r"tpl1569812051084.png", record_pos=(-0.002, 0.344), resolution=(1080, 2160)))
        isneedupdate()
        if exists(Template(r"tpl1573196282189.png", record_pos=(0.203, -0.203), resolution=(1080, 2160))):
            touch(Template(r"tpl1573196282189.png", record_pos=(0.203, -0.203), resolution=(1080, 2160)))
            wait(Template(r"tpl1571130558260.png", record_pos=(-0.406, -0.87), resolution=(1080, 2160)), timeout=65)
            touch(Template(r"tpl1571130711823.png", record_pos=(-0.406, -0.868), resolution=(1080, 2160)))
        else:
            touch(Template(r"tpl1569812112496.png", record_pos=(0.12, 0.398), resolution=(1080, 2160)))
        if exists(Template(r"tpl1569812051084.png", record_pos=(-0.002, 0.344), resolution=(1080, 2160))):
            touch(Template(r"tpl1569812051084.png", record_pos=(-0.002, 0.344), resolution=(1080, 2160)))
        isneedupdate()
        watch_window()
        touch(Template(r"tpl1569812153429.png", record_pos=(-0.377, 0.707), resolution=(1080, 2160)))
        
def case_task():
    #完成任务,完成成就
    touch(Template(r"tpl1569812937727.png", record_pos=(-0.408, -0.772), resolution=(1080, 2160)))
    if exists(Template(r"tpl1569812979038.png", record_pos=(0.293, -0.436), resolution=(1080, 2160))):
        touch(Template(r"tpl1569812979038.png", record_pos=(0.293, -0.436), resolution=(1080, 2160)))
        touch(Template(r"tpl1569813013363.png", record_pos=(-0.165, 0.345), resolution=(1080, 2160)))

    touch(Template(r"tpl1569813035735.png", record_pos=(0.054, -0.606), resolution=(1080, 2160)))

    if exists(Template(r"tpl1569812979038.png", record_pos=(0.293, -0.436), resolution=(1080, 2160))):
        touch(Template(r"tpl1569812979038.png", record_pos=(0.293, -0.436), resolution=(1080, 2160)))
        touch(Template(r"tpl1569813013363.png", record_pos=(-0.165, 0.345), resolution=(1080, 2160)))
    close()
    
def case_tiger():
    #老虎机
    touch(Template(r"tpl1573197823721.png", threshold=0.6, record_pos=(0.424, 0.001), resolution=(1080, 2160)))
    touch(Template(r"tpl1573197840983.png", record_pos=(0.192, -0.064), resolution=(1080, 2160)))
    touch(Template(r"tpl1569813541699.png", record_pos=(-0.1, 0.586), resolution=(1080, 2160)), times=3)
    touch(Template(r"tpl1569813574589.png", record_pos=(0.21, 0.636), resolution=(1080, 2160)))
    sleep(10)
    touch(Template(r"tpl1569813646535.png", record_pos=(0.26, -0.574), resolution=(1080, 2160)))
    touch(Template(r"tpl1569813659764.png", record_pos=(-0.424, -0.812), resolution=(1080, 2160)))  
    
def case_feedback():
    #反馈
    touch(Template(r"tpl1569813713371.png", record_pos=(-0.453, -0.201), resolution=(1080, 2160)))
    touch(Template(r"tpl1569813795073.png", record_pos=(-0.301, -0.124), resolution=(1080, 2160)))
    touch(Template(r"tpl1577086352522.png", record_pos=(-0.361, -0.037), resolution=(1080, 2220)))
    touch(Template(r"tpl1569813814941.png", record_pos=(-0.413, -0.93), resolution=(1080, 2160)))
    touch(Template(r"tpl1569813822785.png", record_pos=(-0.305, 0.041), resolution=(1080, 2160)))
    touch(Template(r"tpl1569813837468.png", record_pos=(0.319, -0.294), resolution=(1080, 2160)))
    
def case_signin():
    #每日签到
    touch(Template(r"tpl1569835784388.png", record_pos=(-0.407, -0.781), resolution=(1080, 2160)))
    if exists(Template(r"tpl1571985715488.png", threshold=0.99, record_pos=(0.012, -0.233), resolution=(1080, 2160))):
        touch(Template(r"tpl1570760028519.png", record_pos=(0.299, -0.234), resolution=(1080, 2220)))
        touch(Template(r"tpl1571051889626.png", record_pos=(-0.247, 0.342), resolution=(1080, 2160)))
        watch_window()
        close()
    else:
        print('can not find image')
        touch(Template(r"tpl1586435328710.png", record_pos=(0.421, -0.708), resolution=(1080, 2220)))

            
def case_offline_earn():
    #离线收益
    stop_app('com.qtt.game.gamecenter.predevtool')
    stop_app('com.jifen.qukan')
    stop_app('com.heitu.game.kxxnc')
    stop_app('com.nuozhen.demo')
    keyevent("HOME")
    sleep(60 * 3)
    case_entergame()
    
def case_video():
    #激励视频
    touch(Template(r"tpl1571130486195.png", record_pos=(0.319, -0.682), resolution=(1080, 2160)))
    sleep(5)
    touch(Template(r"tpl1571130498912.png", record_pos=(0.084, 0.364), resolution=(1080, 2160)))
    sleep(5)
    wait(Template(r"close.png", threshold=0.6, record_pos=(-0.255, -0.126), resolution=(1080, 2220)), timeout=70)
    touch(Template(r"close.png", threshold=0.6, record_pos=(-0.255, -0.126), resolution=(1080, 2220)))
#   wait(Template(r"tpl1571130558260.png", record_pos=(-0.406, -0.87), resolution=(1080, 2160)), timeout=70)
#   touch(Template(r"tpl1571130711823.png", record_pos=(-0.406, -0.868), resolution=(1080, 2160)))
    close()
    
    
def case_harvest():
    #农场收割
    if exists(Template(r"tpl1570781069374.png", record_pos=(-0.318, 0.478), resolution=(1080, 2160))):
        touch(Template(r"tpl1570781069374.png", record_pos=(-0.318, 0.478), resolution=(1080, 2160)))
        if exists(Template(r"tpl1570862697006.png", record_pos=(0.003, 0.334), resolution=(1080, 2160))):
            touch(Template(r"tpl1570862697006.png", record_pos=(0.003, 0.334), resolution=(1080, 2160)))
        else:
            if isapp == True:
                touch(Template(r"tpl1578045014721.png", record_pos=(0.005, 0.401), resolution=(1080, 2220)))
                touch(Template(r"tpl1578045027779.png", record_pos=(0.34, -0.437), resolution=(1080, 2220)))
#                 case_harvest()
                touch(Template(r"tpl1570781069374.png", record_pos=(-0.318, 0.478), resolution=(1080, 2160)))
                if exists(Template(r"tpl1570862697006.png", record_pos=(0.003, 0.334), resolution=(1080, 2160))):
                    touch(Template(r"tpl1570862697006.png", record_pos=(0.003, 0.334), resolution=(1080, 2160)))
            else:
                touch(Template(r"tpl1570781085172.png", record_pos=(-0.127, 0.33), resolution=(1080, 2160)))
                touch(Template(r"tpl1570862697006.png", record_pos=(0.003, 0.334), resolution=(1080, 2160)))
            
        sp = (638, 1237)
        se = (423, 1415)  
        times=2
        for i in range(times):
            swipe(sp, se)
            swipe(se, sp)
        sp = (834, 961)
        se = (223, 1292)
        for i in range(times):
            swipe(sp, se)
            swipe(se, sp)
        sp = (837, 712)
        se = (211, 1065)
        for i in range(times):
            swipe(sp, se, duration=1)
            swipe(se, sp, duration=1)
        sp = (644, 571)
        se = (196, 813)
        for i in range(times):
            swipe(sp, se, duration=1)
            swipe(se, sp, duration=1)

    

if isuc == False:
    stop_qtt()
    keyevent("HOME")
    case_entergame()



case_strengthen()

# #H5版本适用
# if isapp == False:
#     case_steal_veg()
#     case_watering()
#     case_feedback()


case_prop()
case_task()
case_tiger()
case_signin()

if isuc == False:
    case_offline_earn()
    
if istest == False:
    case_video()
    
if istest == False:
    assert_not_exists(Template(r"tpl1578019685448.png", threshold=0.9, rgb=False, record_pos=(-0.397, 0.617), resolution=(1080, 2160)), "去掉debug")
    
    
case_harvest()




    








