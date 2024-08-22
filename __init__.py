# __init__.py 为初始化加载文件
import json
import os
import sys
import threading
import time
import random
# 导入系统资源模块
from ascript.android.system import R
# 导入动作模块
from ascript.android import action
# 导入节点检索模块
from ascript.android import node
# 导入图色检索模块
from ascript.android import screen
from ascript.android.screen import Ocr
from ascript.android.screen import FindImages
import datetime
from ascript.android.node import Selector
import re
from ascript.android.screen import FindColors
# 显示一个窗口
from ascript.android.ui import WebWindow
from ascript.android.system import R
# from git import Repo
import subprocess

print("开始暴富")
# 线程停止标志
areaPattern = ['3432', '3369', '3348', '3313', '3163', '牛仔很忙', '3118', '3105', '3086', '3073', '3057']
# 活动时间
# 14:30、17:30猜谜大会
activity_time = ['9:30', '12:00', '14:30', '15:30', '16:00', '19:00', '19:30', '20:00', '20:20', '20:35', '21:00',
                 '21:35']
account_pattern = ["591330415", '2tezhongbudui']


# account_pattern = ["591330415", '5tezhongbudui', '4tezhongbudui', '3tezhongbudui', '2tezhongbudui']


# areaPattern = ['3105', '3086', '3073', '3057', '3103']
# 点击角色，1-2-3
def clickRole(rolenumber):
    time.sleep(1)
    is_start = True
    while 1:
        print("寻找开始游戏按钮")
        # startGame = Ocr.mlkitocr_v2(rect=[415, 436, 1594, 897], pattern='开始游戏')
        # start_game = FindImages.find_template([R.img("选角界面开始游戏按钮.png"), ], confidence=0.95)
        start_game = FindImages.find([R.img("选角界面开始游戏按钮1080.png"), ], rect=[824, 445, 1277, 717],
                                     confidence=0.95)
        if start_game:
            if rolenumber == 1:
                print("点击第一个角色")
                action.click(103, 174, 20)
                action.click(103, 174, 20)
            if rolenumber == 2:
                print("点击第二个角色")
                action.click(105, 321, 20)
                action.click(105, 321, 20)
            if rolenumber == 3:
                print("点击第三个角色")
                action.click(107, 472, 20)
                action.click(107, 472, 20)

            print("开始游戏")
            time.sleep(1.5)
            action.click(start_game["center_x"], start_game["center_y"], 20)
            # action.click(startGame[0].center_x, startGame[0].center_y, 20)
            time.sleep(1.5)
            action.click(start_game["center_x"], start_game["center_y"], 20)
            # action.click(startGame[0].center_x, startGame[0].center_y, 20)
            time.sleep(5)
            break
        # 如果卡在了选角界面
        while is_start:
            if Ocr.mlkitocr_v2(rect=[824, 445, 1277, 717], pattern='开始游戏'):
                continue
            else:
                is_start = False


def click_change_role_by_word():
    while 1:
        change_Role = Ocr.mlkitocr_v2(pattern='切换角色')
        if change_Role:
            print("切换角色，坐标", change_Role[0].center_x, change_Role[0].center_y)
            action.click(change_Role[0].center_x, change_Role[0].center_y, 20)
            time.sleep(4)
            if Ocr.mlkitocr_v2(pattern='切换角色'):
                click_change_role_by_word()
            else:
                break
        if FindImages.find([R.img("左下方切换按钮灰度1080.png"), ], confidence=0.95) or FindImages.find(
                [R.img("设置按钮灰度1080.png"), ], rect=[2, 562, 1275, 715], confidence=0.95):
            changeRole()
            break
        if FindImages.find([R.img("选角界面开始游戏按钮1080.png"), ], rect=[824, 445, 1277, 717],
                                     confidence=0.95):
            break

# 待完善
def changeRole():
    # 判断当前是否有BOSS宝箱
    while 1:
        # 寻找设置按钮
        print("寻找设置按钮")
        time.sleep(1)
        settingText = Ocr.mlkitocr_v2(rect=[851, 588, 1251, 713], pattern='设置')
        # 取色
        # settingColor = FindColors.find(
        #     "901,653,#EDE5E5|917,645,#F7F6F5|929,651,#EFEAE9|937,667,#C8BFB7|931,679,#B3A39B|917,683,#AB9B92|901,677,#B5A4A4|899,671,#C4B6AF|913,671,#C4B6AF")
        # 原图
        # settingImg = FindImages.find_template([R.img("2.png"), ], confidence=0.95)
        settingImg = FindImages.find([R.img("设置1080.png"), ], rect=[8, 550, 1273, 705], confidence=0.95)
        # if settingText:
        #     time.sleep(1)
        #     print("点击设置文字，坐标", settingText[0].center_x, settingText[0].center_y)
        #     action.click(settingText[0].center_x, settingText[0].center_y, 20)
        #     # print("点击设置，坐标", setting["center_x"], setting["center_y"])
        #     # action.click(setting["center_x"], setting["center_y"], 20)
        #     break
        # elif settingImg:
        #     time.sleep(1)
        #     print("点击设置文字图片，坐标", settingImg["center_x"], settingImg["center_y"])
        #     action.click(settingImg["center_x"], settingImg["center_y"], 20)
        #     break

        if settingImg:
            time.sleep(1)
            print("点击设置图片，坐标", settingImg["center_x"], settingImg["center_y"])
            action.click(settingImg["center_x"], settingImg["center_y"], 20)
            break
        # if settingColor:
        #     time.sleep(1)
        #     print("点击设置颜色，坐标", settingColor.x, settingColor.y)
        #     action.click(settingColor.x, settingColor.y, 20)
        #     break
        else:
            print("寻找左下方切换按钮")
            bottomToolbar = FindImages.find([R.img("左下方切换按钮灰度1080.png"), ], confidence=0.95)
            # bottomToolbar = FindImages.find_template([R.img("左下方切换按钮.png"), ], confidence=0.95)
            if bottomToolbar:
                print("点击左下方切换按钮，坐标", bottomToolbar["center_x"], bottomToolbar["center_y"])
                action.click(bottomToolbar["center_x"], bottomToolbar["center_y"], 20)
                time.sleep(1.5)
            else:
                # 暂时方案，如果卡住，可能是由于刚好最后一个boss出了宝箱，无法点击
                action.click(453, 534, 20)
        # time.sleep(2)
    # while 1:
    #     change_Role = Ocr.mlkitocr_v2(pattern='切换角色')
    #     if change_Role:
    #         print("切换角色，坐标", change_Role[0].center_x, change_Role[0].center_y)
    #         action.click(change_Role[0].center_x, change_Role[0].center_y, 20)
    #         time.sleep(1.5)
    #         break
    #     if FindImages.find([R.img("左下方切换按钮灰度1080.png"), ], confidence=0.95) or FindImages.find(
    #             [R.img("设置按钮灰度1080.png"), ], rect=[2, 562, 1275, 715], confidence=0.95):
    #         changeRole()
    #         break
    click_change_role_by_word()


def change_account():
    # 判断当前是否有BOSS宝箱
    while 1:
        # 寻找设置按钮
        print("寻找设置按钮")
        time.sleep(1)
        # gp = GPStack()
        # gp.add(GrayImage())
        # res = gp.run()
        # 展示处理后的图像
        # ImageWindow.show(res.image)
        settingText = Ocr.mlkitocr_v2(rect=[851, 588, 1251, 713], pattern='设置')
        # 灰度处理过的图片
        # settingImg = FindImages.find([R.img("设置按钮.png"), ], rect=[602, 597, 1597, 897], confidence=0.95)
        settingImg = FindImages.find([R.img("设置按钮灰度1080.png"), ], rect=[2, 562, 1275, 715], confidence=0.95)
        # 原图
        # settingImg = FindImages.find_template([R.img("2.png"), ], confidence=0.95)

        # if settingText:
        #     time.sleep(1)
        #     print("点击设置文字，坐标", settingText[0].center_x, settingText[0].center_y)
        #     action.click(settingText[0].center_x, settingText[0].center_y, 20)
        #     # print("点击设置，坐标", setting["center_x"], setting["center_y"])
        #     # action.click(setting["center_x"], setting["center_y"], 20)
        #     break
        # elif settingImg:
        #     time.sleep(1)
        #     print("点击设置文字图片，坐标", settingImg["center_x"], settingImg["center_y"])
        #     action.click(settingImg["center_x"], settingImg["center_y"], 20)
        #     break

        if settingImg:
            time.sleep(1)
            print("点击设置图片，坐标", settingImg["center_x"], settingImg["center_y"])
            action.click(settingImg["center_x"], settingImg["center_y"], 20)
            break
        # elif settingText:
        #     time.sleep(1)
        #     print("点击设置文字，坐标", settingText[0].center_x, settingText[0].center_y)
        #     action.click(settingText[0].center_x, settingText[0].center_y, 20)
        #     # print("点击设置，坐标", setting["center_x"], setting["center_y"])
        #     # action.click(setting["center_x"], setting["center_y"], 20)
        #     break
        else:
            print("寻找左下方切换按钮")
            bottomToolbar = FindImages.find([R.img("左下方切换按钮灰度1080.png"), ], confidence=0.95)
            # bottomToolbar = FindImages.find_template([R.img("左下方切换按钮.png"), ], confidence=0.95)
            if bottomToolbar:
                print("点击左下方切换按钮，坐标", bottomToolbar["center_x"], bottomToolbar["center_y"])
                action.click(bottomToolbar["center_x"], bottomToolbar["center_y"], 20)
                time.sleep(1.5)
            else:
                # 暂时方案，如果卡住，可能是由于刚好最后一个boss出了宝箱，无法点击
                action.click(453, 534, 20)
        # time.sleep(2)
    while 1:
        change_Role = Ocr.mlkitocr_v2(pattern='切换账号')
        if change_Role:
            print("切换角色，坐标", change_Role[0].center_x, change_Role[0].center_y)
            action.click(change_Role[0].center_x, change_Role[0].center_y, 20)
            break
        if FindImages.find([R.img("左下方切换按钮灰度1080.png"), ], confidence=0.95) or FindImages.find(
                [R.img("设置按钮灰度1080.png"), ], rect=[2, 562, 1275, 715], confidence=0.95):
            changeRole()
            break


# 关闭新服7天登录提示
def closeNewAreaTip():
    is_close = False
    for i in range(0, 10):
        # time.sleep(0.1)
        print("查找新服连登提示")
        # new_area_tip = FindImages.find_template([R.img("新服连登关闭按钮.png"), ], rect=[1202, 78, 1555, 338],
        #                                       confidence=0.95)
        # new_area_tip = FindImages.find_template([R.img("新服连登七天.png"), ], rect=[214, 542, 750, 877], confidence=0.95)
        new_area_tip = FindImages.find([R.img("新服连登七天1080.png"), ], rect=[163, 361, 574, 659], confidence=0.95)
        # new_area_tip = FindImages.find_template([R.img("新服连登提示.png"), ], confidence=0.95)
        if new_area_tip:
            while 1:
                # new_area_tip_close = FindImages.find_template([R.img("新服连登关闭按钮.png"), ], rect=[1202, 78, 1555, 338],
                # confidence=0.95)
                new_area_tip_close = FindImages.find([R.img("新服连登关闭按钮1080.png"), ], rect=[1015, 54, 1251, 274],
                                                     confidence=0.95)
                print("查找关闭按钮")
                if new_area_tip_close:
                    action.click(new_area_tip_close["center_x"], new_area_tip_close["center_y"], 20)
                    print("关闭新服签到提示，点击", new_area_tip_close["center_x"], new_area_tip_close["center_y"])
                    is_close = True
                    time.sleep(1)
                    break
                time.sleep(1)
        if is_close:
            break


# def close_new_area_tip(stop_event):
#     while not stop_event.is_set():
#         # time.sleep(0.1)
#         print("查找新服连登提示")
#         # new_area_tip = FindImages.find_template([R.img("新服连登关闭按钮.png"), ], rect=[1202, 78, 1555, 338],
#         #                                       confidence=0.95)
#         new_area_tip = FindImages.find_template([R.img("新服连登七天.png"), ], rect=[214, 542, 750, 877], confidence=0.95)
#         # new_area_tip = FindImages.find_template([R.img("新服连登提示.png"), ], confidence=0.95)
#         if new_area_tip:
#             new_area_tip_close = FindImages.find_template([R.img("新服连登关闭按钮.png"), ], rect=[1202, 78, 1555, 338],
#                                                     confidence=0.95)
#             print("查找关闭按钮")
#             if new_area_tip_close:
#                 action.click(new_area_tip_close["center_x"], new_area_tip_close["center_y"], 20)
#                 print("关闭新服签到提示，点击", new_area_tip_close["center_x"], new_area_tip_close["center_y"])
#                 is_close = True
#             time.sleep(1)


def close_new_area_tip(stop_event):
    # 待定
    # time.sleep(5)
    # while not stop_event.is_set():
    for i in range(0, 20):
        # time.sleep(0.1)
        print("查找新服连登提示线程")
        if stop_event.is_set():
            print("停止查找新服连登提示线程")
            break
        # new_area_tip = FindImages.find_template([R.img("新服连登关闭按钮.png"), ], rect=[1202, 78, 1555, 338],
        #                                       confidence=0.95)
        # new_area_tip = FindImages.find_template([R.img("新服连登七天.png"), ], rect=[214, 542, 750, 877], confidence=0.95)
        new_area_tip = FindImages.find([R.img("新服连登七天1080.png"), ], rect=[163, 361, 574, 659], confidence=0.95)

        # new_area_tip = FindImages.find_template([R.img("新服连登提示.png"), ], confidence=0.95)
        if new_area_tip:
            # new_area_tip_close = FindImages.find_template([R.img("新服连登关闭按钮.png"), ], rect=[1202, 78, 1555, 338],
            #                                         confidence=0.95)
            new_area_tip_close = FindImages.find([R.img("新服连登关闭按钮1080.png"), ], rect=[1015, 54, 1251, 274],
                                                 confidence=0.95)

            print("查找关闭按钮")
            if new_area_tip_close:
                action.click(new_area_tip_close["center_x"], new_area_tip_close["center_y"], 20)
                print("关闭新服签到提示，点击", new_area_tip_close["center_x"], new_area_tip_close["center_y"])
                is_close = True
            # time.sleep(1)
        return_tip = FindImages.find([R.img("回归提示.png"), ], rect=[445, 28, 1136, 463], confidence=0.95)
        if return_tip:
            return_tip_close = FindImages.find([R.img("回归提示关闭.png"),],rect= [681,4,1217,411] ,confidence= 0.95)
            if return_tip_close:
                action.click(return_tip_close["center_x"], return_tip_close["center_y"], 20)
                print("关闭回归活动提示")
                time.sleep(2)
        different_login_status = FindImages.find([R.img("不一致的登录状态.png"), ], rect=[260, 112, 1048, 605], confidence=0.95)
        if different_login_status:
            confirm_btn = FindImages.find([R.img("确定按钮.png"), ], rect=[328, 145, 971, 556], confidence=0.95)
            if confirm_btn:
                action.click(confirm_btn["center_x"], confirm_btn["center_y"], 20)
                print("登录状态不一致提示")
        time.sleep(1)


# 判断当前时间是否是否是星期一、星期三或星期五的晚上9点30分后
def is_specific_day_and_time():
    # 获取当前时间
    now = datetime.datetime.now()

    # 检查当前时间是否是星期一、星期三或星期五
    if now.weekday() in [0, 2, 4]:  # 0=Monday, 2=Wednesday, 4=Friday
        # 获取当前时间的小时和分钟
        current_hour = now.hour
        current_minute = now.minute

        # 检查当前时间是否是晚上9点30分后
        if current_hour > 21 or (current_hour == 21 and current_minute >= 30):
            return True

    return False


# 判断当前时间是否是在指定时间内
def is_current_time_within_five_minutes(time_list):
    # 获取当前时间
    current_time = datetime.datetime.now().time()

    # 定义5分钟的时间差
    # time_delta = datetime.timedelta(minutes=5)
    time_delta = datetime.timedelta(minutes=2)

    for time_str in time_list:
        # 将time_str转换为datetime.time对象
        time = datetime.datetime.strptime(time_str, "%H:%M").time()

        # 将当前时间转换为datetime对象
        current_time_dt = datetime.datetime.combine(datetime.date.today(), current_time)
        time_dt = datetime.datetime.combine(datetime.date.today(), time)

        # 如果当前时间在目标时间的前后5分钟内，返回True
        if abs((current_time_dt - time_dt).total_seconds()) <= time_delta.total_seconds():
            return True

    # 如果当前时间不在任何一个时间的前后5分钟内，返回False
    return False


# 关闭活动提示---动作
def close_activity_tips():
    # activityTips = FindImages.find_template([R.img("活动提示.png"), ], confidence=0.95)
    activityTips = FindImages.find([R.img("活动提示1080.png"), ], rect=[340, 177, 947, 544], confidence=0.95)
    print("关闭活动提示线程")
    if activityTips:
        time.sleep(1)
        # 查找活动取消按钮
        # closeActivityTips = FindImages.find_template([R.img("取消活动按钮.png"), ],
        #                                              confidence=0.95)
        closeActivityTips = FindImages.find([R.img("取消活动按钮1080.png"), ], rect=[370, 189, 919, 534],
                                            confidence=0.95)
        if closeActivityTips:
            time.sleep(0.5)
            # 如果找到取消按钮，点击取消
            action.click(closeActivityTips["center_x"], closeActivityTips["center_y"], 20)
            print("关闭活动提示框,坐标：", closeActivityTips["center_x"], closeActivityTips["center_y"])


def closeActivityTips(stop_event):
    print("线程开始执行")
    time.sleep(0.5)
    # for i in range(0,10):
    #     print(i)
    while not stop_event.is_set():
        # while 1:
        # 12:00 - 浪漫舞会
        if is_specific_day_and_time():
            print("当前为周一/周三/周五晚上9点半后，检测魔王入侵活动按钮")
            close_activity_tips()
            time.sleep(1)
        else:
            if is_current_time_within_five_minutes(activity_time):
                # 判断是否有活动提示框
                print("临近活动时间，判断是否有活动提示框")
                close_activity_tips()
                # activityTips = FindImages.find_template([R.img("活动提示.png"),],rect= [431,177,1199,715] ,confidence= 0.95)
                # if activityTips:
                #     time.sleep(1)
                #     # 查找活动取消按钮
                #     closeActivityTips =FindImages.find_template([R.img("取消活动按钮.png"),],rect= [397,195,1182,701] ,confidence= 0.95)
                #     if closeActivityTips:
                #         time.sleep(0.5)
                #         # 如果找到取消按钮，点击取消
                #         action.click(closeActivityTips["center_x"], closeActivityTips["center_y"], 20)
                #         print("关闭活动提示框")
            time.sleep(1)
    print("线程结束")


# 判断巢1是否满怒
def is1stNestFull():
    time.sleep(1)
    # return FindImages.find_template([R.img("巢1怒气已满.png"), ], confidence=0.95)
    return FindImages.find([R.img("巢1怒气已满1080.png"), ], rect=[4, 0, 503, 540], confidence=0.95)


def isWorldFull():
    return FindImages.find([R.img("魔王体力已空.png"), ], rect=[12, 16, 372, 417], confidence=0.95)


# 打1层巢穴魔王
def fight1stLairDemon(no):
    # 开始时间
    start_time = time.time()
    # 持续时间（秒）
    # 默认从第一个开始打
    duration = 27
    # 第一个boss的坐标
    coordinates = [122, 209]
    # 如果是第二个
    if no == 2:
        print("巢一boss1 -> 巢一boss2")
        duration = 27
        # 第二个boss的坐标
        coordinates = [112, 260]
    if no == 3:
        print("巢一boss2 -> 巢一boss3")
        # 待完善
        duration = 38
        # 第三个boss的坐标
        coordinates = [151, 326]
    if no == 4:
        print("巢一boss3 -> 巢一boss4")
        duration = 44
        # 第四个boss的坐标
        coordinates = [157, 379]
    if no == 5:
        print("巢一boss4 -> 巢一boss5")
        duration = 62
        # 第五个boss的坐标
        coordinates = [100, 429]
    # 回到1
    if no == 1:
        print("巢一boss5 -> 巢一boss1")
        coordinates = [122, 209]
        duration = 35
    print(duration)
    while True:
        # 当前时间
        if is1stNestFull():
            return
        current_time = time.time()
        action.click(coordinates[0], coordinates[1], 20)
        # 检查是否超过持续时间
        if current_time - start_time > duration:
            break
        # 等待0.5秒
        time.sleep(0.5)


# 识图判断巢穴1-5是否存活
def is_demon_alive_1_to_5(demon_id):
    demon_is_alive = None
    if demon_id == 1:
        demon_is_alive = FindImages.find([R.img("4阶魔偶已刷新.png"), ], rect=[6, 139, 348, 473], confidence=0.95)
    if demon_id == 2:
        demon_is_alive = FindImages.find([R.img("4阶无涯已刷新.png"), ], rect=[2, 133, 354, 451], confidence=0.95)
        # print("demon_id:",demon_id,":",2)
    if demon_id == 3:
        demon_is_alive = FindImages.find([R.img("5阶巨猿已刷新.png"), ], rect=[2, 167, 336, 459], confidence=0.95)
        # print("demon_id:",demon_id,":",3)
    if demon_id == 4:
        demon_is_alive = FindImages.find([R.img("5阶蛛妖已刷新.png"), ], rect=[4, 155, 336, 445], confidence=0.95)
        # print("demon_id:",demon_id,":",4)
    if demon_id == 5:
        demon_is_alive = FindImages.find([R.img("5阶穷奇已刷新1.png"), ], rect=[0, 157, 354, 465], confidence=0.95)
        # print("demon_id:",demon_id,":",5)
    return demon_is_alive


# 通过识图
def fight1stLairDemonByPic(no):
    # 4阶魔偶坐标 122,209
    # 4阶无涯坐标 112,260
    # 5阶巨猿坐标 151,326
    # 5阶蛛妖坐标 157,379
    # 5阶穷奇坐标 100,429
    # 持续时间（秒）
    # 默认从第一个开始打
    # duration = 27
    # # 第一个boss的坐标
    # coordinates = [122,209]
    # demon_is_alive = FindImages.find([R.img("4阶魔偶已刷新.png"), ], rect=[6, 139, 348, 473], confidence=0.95)
    # 如果是第二个
    if no == 2:
        print("-> 巢一boss2")
        # 第二个boss的坐标
        coordinates = [112, 260]
    if no == 3:
        print("-> 巢一boss3")
        # 待完善
        # 第三个boss的坐标
        coordinates = [151, 326]
    if no == 4:
        print("-> 巢一boss4")
        # 第四个boss的坐标
        coordinates = [157, 379]
    if no == 5:
        print("-> 巢一boss5")
        # 第五个boss的坐标
        coordinates = [100, 429]
    # 回到1
    if no == 1:
        print("-> 巢一boss1")
        coordinates = [122, 209]
    while True:
        # 当前时间
        if is1stNestFull():
            return
        action.click(coordinates[0], coordinates[1], 20)
        # 检查是否超过持续时间
        is_demon_dead = not is_demon_alive_1_to_5(no)
        if is_demon_dead:
            # print(is_demon_dead)
            action.click(coordinates[0], coordinates[1], 20)
            action.click(coordinates[0], coordinates[1], 20)
            break
        # 等待0.5秒
        time.sleep(0.5)


# 点击主界面boss按钮
def click_main_demon():
    while 1:
        if FindImages.find_template([R.img("群仙斗.png"),],rect= [6,6,475,268] ,confidence= 0.95):
            close_interface = FindImages.find([R.img("关闭按钮.png"), ], confidence=0.95)
            if close_interface:
                action.click(close_interface["center_x"], close_interface["center_y"], 20)
                time.sleep(2)
        # 找到魔王按钮
        # demonButton = FindImages.find_template([R.img("魔王按钮.png"), ], confidence=0.95)
        demonButton = FindImages.find([R.img("魔王按钮1080.png"), ], rect=[860, 4, 1273, 246], confidence=0.95)
        if demonButton:
            # 点击魔王按钮
            action.click(demonButton["center_x"], demonButton["center_y"], 20)
            print("点击魔王按钮")
            # 如果两秒后还有魔王按钮，说明未点击成功，重新执行
            time.sleep(2)
            # if FindImages.find([R.img("魔王按钮1080.png"), ], rect=[860, 4, 1273, 246], confidence=0.95):
            #     click_main_demon()
            break
            #
            # if FindImages.find([R.img("巢穴按钮1080.png"), ], rect=[778, 8, 1259, 463], confidence=0.95):
            #     break
            # else:
            #     click_main_demon()
        # 如果没找到魔王按钮，点击右上角切换按钮
        else:
            # aboveChangeButton = FindImages.find_template([R.img("右上角切换按钮.png"), ], confidence=0.95)
            aboveChangeButton = FindImages.find([R.img("右上角切换按钮1080.png"), ], rect=[890, 0, 1277, 284],
                                                confidence=0.95)
            print("未找到魔王按钮，寻找右上方切换按钮")
            if aboveChangeButton:
                action.click(aboveChangeButton["center_x"], aboveChangeButton["center_y"], 20)
                print("点击右上方切换按钮")
                time.sleep(1)
            close_world = FindImages.find([R.img("魔王界面关闭按钮.png"), ], rect=[973, 14, 1241, 221], confidence=0.95)
            if close_world:
                action.click(close_world["center_x"], close_world["center_y"], 20)
                time.sleep(1)


def click_go_to_nest():
    while 1:
        # goToNest = FindImages.find_template([R.img("前往巢穴按钮.png"), ], confidence=0.95)
        goToNest = FindImages.find([R.img("前往巢穴按钮1080.png"), ], rect=[673, 348, 1263, 709], confidence=0.95)
        if goToNest:
            action.click(goToNest["center_x"], goToNest["center_y"], 20)
            break

# 进入巢穴魔王
def go1stLairDemon():
    # 如果卡在了选角界面
    # start_game = Ocr.mlkitocr_v2(rect=[850,413,1275,715], pattern='开始游戏')
    # if start_game:
    #     action.click(start_game[0].center_x, start_game[0].center_y, 20)
    #     time.sleep(5)
    print("进击巢一")
    # 点击主界面魔王按钮
    click_main_demon()
    # while 1:
    #     # 找到魔王按钮
    #     # demonButton = FindImages.find_template([R.img("魔王按钮.png"), ], confidence=0.95)
    #     demonButton = FindImages.find([R.img("魔王按钮1080.png"), ], rect=[860, 4, 1273, 246], confidence=0.95)
    #     if demonButton:
    #         action.click(demonButton["center_x"], demonButton["center_y"], 20)
    #         time.sleep(2)
    #         if FindImages.find([R.img("魔王按钮1080.png"), ], rect=[860, 4, 1273, 246], confidence=0.95):
    #
    #         break
    #     # 如果没找到魔王按钮，点击右上角切换按钮
    #     else:
    #         # aboveChangeButton = FindImages.find_template([R.img("右上角切换按钮.png"), ], confidence=0.95)
    #         aboveChangeButton = FindImages.find([R.img("右上角切换按钮1080.png"), ], rect=[890, 0, 1277, 284], confidence=0.95)
    #         if aboveChangeButton:
    #             action.click(aboveChangeButton["center_x"], aboveChangeButton["center_y"], 20)
    #             time.sleep(1)
    time.sleep(2)
    while 1:
        # nestButton = FindImages.find_template([R.img("巢穴按钮.png"), ], confidence=0.95)
        nestButton = FindImages.find([R.img("巢穴按钮1080.png"), ], rect=[778, 8, 1259, 463], confidence=0.95)
        if nestButton:
            action.click(nestButton["center_x"], nestButton["center_y"], 20)
            time.sleep(1)
            break
        if FindImages.find([R.img("魔王按钮1080.png"), ], rect=[860, 4, 1273, 246], confidence=0.95):
            click_main_demon()
    while 1:
        # nest1stButton = FindImages.find_template([R.img("巢穴1层按钮.png"), ], confidence=0.95)
        nest1stButton = FindImages.find([R.img("巢穴1层按钮1080.png"), ], rect=[2, 2, 1277, 320], confidence=0.95)
        if nest1stButton:
            action.click(nest1stButton["center_x"], nest1stButton["center_y"], 20)
            time.sleep(1)
            break
    click_go_to_nest()
    # while 1:
    #     # goToNest = FindImages.find_template([R.img("前往巢穴按钮.png"), ], confidence=0.95)
    #     goToNest = FindImages.find([R.img("前往巢穴按钮1080.png"), ], rect=[673, 348, 1263, 709], confidence=0.95)
    #     if goToNest:
    #         action.click(goToNest["center_x"], goToNest["center_y"], 20)
    #         break
    # zeroTime = True
    # isFirstTime = True
    while 1:
        if FindImages.find([R.img("巢穴1层.png"), ], rect=[929, 0, 1277, 195], confidence=0.95):
            print("已进入巢穴")
            break
        if FindImages.find([R.img("前往巢穴按钮1080.png"), ], rect=[673, 348, 1263, 709], confidence=0.95):
            click_go_to_nest()
    while 1:
        if is1stNestFull():
            break
        # zeroTime = True
        # demon_list = [3,1,2,5,4]
        demon_list = [1, 2, 3, 4, 5]
        for demon_id in demon_list:
            fight1stLairDemonByPic(demon_id)
        # if zeroTime:
        #     fight1stLairDemon(0)
        #     zeroTime = False
        # for i in range(1, 6):
        #     if isFirstTime:
        #         if i == 1:
        #             isFirstTime = False
        #             continue
        #     fight1stLairDemon(i)


def go_to_world():
    while 1:
        if FindColors.find(
                "829,602,#EC3834|829,606,#EC3835|823,610,#EC3834|820,607,#EC3834|820,603,#EC3834|820,600,#EC3834|821,597,#EC3834|824,595,#EC3834") or FindImages.find(
                [R.img("boss次数为0.png"), ], rect=[661, 550, 1251, 705], confidence=0.95):
            close_world = FindImages.find([R.img("魔王界面关闭按钮.png"), ], rect=[973, 14, 1241, 221], confidence=0.95)
            while 1:
                action.click(close_world["center_x"], close_world["center_y"], 20)
                time.sleep(1)
                if not FindImages.find([R.img("魔王界面关闭按钮.png"), ], rect=[973, 14, 1241, 221], confidence=0.95):
                    break
            return 0
        # goToNest = FindImages.find_template([R.img("前往巢穴按钮.png"), ], confidence=0.95)
        goToWorld = FindImages.find([R.img("立即前往魔王按钮.png"), ], rect=[802, 425, 1211, 707], confidence=0.95)
        if goToWorld:
            action.click(goToWorld["center_x"], goToWorld["center_y"], 20)
            print("点击进入世界魔王")
            time.sleep(1)
            if FindImages.find([R.img("弹窗提示体力不足.png"), ], rect=[366, 173, 927, 526], confidence=0.95):

                while 1:
                    close_world = FindImages.find([R.img("魔王界面关闭按钮.png"), ], rect=[677, 8, 1271, 389],
                                                  confidence=0.95)
                    action.click(close_world["center_x"], close_world["center_y"], 20)
                    time.sleep(1)
                    if not FindImages.find([R.img("魔王界面关闭按钮.png"), ], rect=[677, 8, 1271, 389],
                                           confidence=0.95):
                        return 0

            time.sleep(1)
            if FindImages.find([R.img("立即前往魔王按钮.png"), ], rect=[802, 425, 1211, 707], confidence=0.95):
                go_to_world()
            else:
                return 1


# 进入世界魔王
def go3stWorldDemon():
    # 如果卡在了选角界面
    start_game = Ocr.mlkitocr_v2(rect=[850, 413, 1275, 715], pattern='开始游戏')
    if start_game:
        action.click(start_game[0].center_x, start_game[0].center_y, 20)
        time.sleep(5)
    print("进击世界魔王")

    click_main_demon()
    time.sleep(2)


    while 1:
        # nestButton = FindImages.find_template([R.img("巢穴按钮.png"), ], confidence=0.95)
        nestButton = FindImages.find([R.img("巢穴按钮1080.png"), ], rect=[778, 8, 1259, 463], confidence=0.95)
        if nestButton:
            action.click(nestButton["center_x"], nestButton["center_y"], 20)
            time.sleep(1)
            break
        if FindImages.find([R.img("魔王按钮1080.png"), ], rect=[860, 4, 1273, 246], confidence=0.95):
            click_main_demon()
    while 1:
        world_btn = FindImages.find([R.img("魔王按钮黑底.png"), ], rect=[659, 10, 1277, 502], confidence=0.95)
        if world_btn:
            action.click(world_btn["center_x"], world_btn["center_y"], 20)
            time.sleep(1)
            break
    while 1:
        world_3_btn = FindImages.find([R.img("世界魔王三层.png"), ], rect=[24, 6, 1265, 221], confidence=0.95)
        if world_3_btn:
            action.click(world_3_btn["center_x"], world_3_btn["center_y"], 20)
            print("点击世界魔王三")
            time.sleep(1)
            break
    # while 1:
    #     # nestButton = FindImages.find_template([R.img("巢穴按钮.png"), ], confidence=0.95)
    #     world_button = FindImages.find([R.img("世界魔王按钮白底.png"), ], rect=[846, 10, 1259, 328], confidence=0.95)
    #     if world_button:
    #         action.click(world_button["center_x"], world_button["center_y"], 20)
    #         print("点击世界魔王按钮")
    #         time.sleep(1)
    #         break
    #     if FindImages.find([R.img("魔王按钮1080.png"), ], rect=[860, 4, 1273, 246], confidence=0.95):
    #         click_main_demon()
    # while 1:
    #     if FindImages.find([R.img("世界六层.png"),],rect= [24,22,1257,254] ,confidence= 0.95):
    #         nestButton = FindImages.find([R.img("巢穴按钮1080.png"), ], rect=[778, 8, 1259, 463], confidence=0.95)
    #         if nestButton:
    #             action.click(nestButton["center_x"], nestButton["center_y"], 20)
    #     world_3_btn = FindImages.find([R.img("世界魔王三层.png"),],rect= [24,6,1265,221] ,confidence= 0.95)
    #     if world_3_btn:
    #         action.click(world_3_btn["center_x"], world_3_btn["center_y"], 20)
    #         print("点击世界魔王三")
    #         time.sleep(1)
    #         break
    is_blank = go_to_world()
    if is_blank == 0:
        return 0
    # while 1:
    #     # nest1stButton = FindImages.find_template([R.img("巢穴1层按钮.png"), ], confidence=0.95)
    #     world3stButton = FindImages.find([R.img("世界魔王三层按钮.png"),],rect= [116,56,1106,191] ,confidence= 0.95)
    #     if world3stButton:
    #         action.click(world3stButton["center_x"], world3stButton["center_y"], 20)
    #         time.sleep(1)
    #         break
    # while 1:
    #     # goToNest = FindImages.find_template([R.img("前往巢穴按钮.png"), ], confidence=0.95)
    #     goToWorld = FindImages.find([R.img("立即前往魔王按钮.png"),],rect= [802,425,1211,707] ,confidence= 0.95)
    #     if goToWorld:
    #         time.sleep(1)
    #         action.click(goToWorld["center_x"], goToWorld["center_y"], 20)
    #         break
    while 1:
        if FindImages.find([R.img("世界魔王三层标识.png"), ], rect=[967, 2, 1275, 209], confidence=0.95):
            print("已进入世界魔王三层")
            break
    while 1:
        # if FindImages.find([R.img("魔王体力已空.png"),],rect= [4,54,346,405] ,confidence= 0.95):
        #     break
        if FindColors.find(
                "118,149,#E00105|135,156,#FF0005|148,154,#FF0005|173,151,#D30205|108,154,#FF0005|158,163,#FF0005|132,163,#DE0205|139,163,#DE0205|181,163,#FF0005"):
            break
        # zeroTime = True
        # demon_list = [3,1,2,5,4]
        # world_alive = FindImages.find([R.img("6阶炼狱存活.png"),R.img("6阶巨猿存活.png"),R.img("6阶无涯存活.png"),],rect= [0,147,368,451] ,confidence= 0.95)
        if FindImages.find([R.img("6阶炼狱存活.png"), ], rect=[4, 131, 368, 482], confidence=0.95):
            while FindImages.find([R.img("6阶炼狱存活.png"), ], rect=[4, 131, 368, 482], confidence=0.95):
                print("->6阶炼狱")
                action.click(164, 205)
                time.sleep(0.8)
                if FindColors.find(
                        "118,149,#E00105|135,156,#FF0005|148,154,#FF0005|173,151,#D30205|108,154,#FF0005|158,163,#FF0005|132,163,#DE0205|139,163,#DE0205|181,163,#FF0005"):
                    break
        elif FindImages.find([R.img("6阶巨猿.png"), ], rect=[4, 131, 368, 482], confidence=0.95):
            while FindImages.find([R.img("6阶巨猿.png"), ], rect=[4, 131, 368, 482], confidence=0.95):
                print("->6阶巨猿")
                action.click(179, 265)
                time.sleep(0.8)
                if FindColors.find(
                        "118,149,#E00105|135,156,#FF0005|148,154,#FF0005|173,151,#D30205|108,154,#FF0005|158,163,#FF0005|132,163,#DE0205|139,163,#DE0205|181,163,#FF0005"):
                    break
        elif FindImages.find([R.img("6阶无涯存活.png"), ], rect=[4, 133, 389, 469], confidence=0.95):
            while FindImages.find([R.img("6阶无涯存活.png"), ], rect=[4, 133, 389, 469], confidence=0.95):
                print("->6阶无涯")
                action.click(181, 318)
                time.sleep(0.8)
                if FindColors.find(
                        "118,149,#E00105|135,156,#FF0005|148,154,#FF0005|173,151,#D30205|108,154,#FF0005|158,163,#FF0005|132,163,#DE0205|139,163,#DE0205|181,163,#FF0005"):
                    break
        elif FindImages.find([R.img("6阶尸将已刷新.png"), ], rect=[2, 131, 360, 459], confidence=0.95):
            print("->6阶尸将")
            action.click(190, 377)
            time.sleep(0.8)
            if FindColors.find(
                    "118,149,#E00105|135,156,#FF0005|148,154,#FF0005|173,151,#D30205|108,154,#FF0005|158,163,#FF0005|132,163,#DE0205|139,163,#DE0205|181,163,#FF0005"):
                break
        elif FindImages.find([R.img("6阶穷奇已刷新.png"), ], rect=[2, 141, 370, 486], confidence=0.95):
            print("->6阶穷奇")
            action.click(170, 427)
            time.sleep(0.8)
            if FindColors.find(
                    "118,149,#E00105|135,156,#FF0005|148,154,#FF0005|173,151,#D30205|108,154,#FF0005|158,163,#FF0005|132,163,#DE0205|139,163,#DE0205|181,163,#FF0005"):
                break
        else:
            action.click(566, 381)
            time.sleep(0.8)


def traverse_from_start_infinite(areaPattern, start):
    n = len(areaPattern)
    IArea = 0
    while 1:
        while 1:
            print(areaPattern[(start + IArea) % n])
            # i += 1
            areaId = areaPattern[(start + IArea) % n]
            print("寻找选服按钮")
            # res = Ocr.mlkitocr_v2(rect=[385, 330, 1194, 836], pattern='选服')
            res = Ocr.mlkitocr_v2(rect=[385, 284, 953, 655], pattern='选服')
            if res:
                print("点击", res[0].text, "，坐标", res[0].center_x, res[0].center_y)
                action.click(res[0].center_x, res[0].center_y, 20)
                break
        time.sleep(1)
        while 1:
            # 寻找区服
            # area = Ocr.mlkitocr_v2(rect=[191, 98, 1388, 768], pattern=areaId)
            area = Ocr.mlkitocr_v2(rect=[360, 142, 1082, 597], pattern=areaId)
            if area:
                print("找到区服", area[0].text)
                action.click(area[0].center_x, area[0].center_y + 50, 20)
                break
            else:
                print("下滑选区")

                action.Touch.down(469, 565, 20)
                action.Touch.move(459, 246, 3000)
                action.Touch.up(459, 246, 1000)

                # action.Touch.down(459,246, 20)
                # action.Touch.move(469,565, 3000)
                # action.Touch.up(469,565, 1000)
                time.sleep(2)

        for i in range(1, 4):
            stop_event = threading.Event()
            # stop_event_new_area = threading.Event()
            clickRole(i)
            # 启动关闭活动提示线程
            activity_thread = threading.Thread(target=closeActivityTips, args=(stop_event,))
            close_new_area_tip_thread = threading.Thread(target=close_new_area_tip)
            try:
                activity_thread.start()
                close_new_area_tip_thread.start()
            # thread2.start()
            except:
                print("Error: unable to start thread")
            # closeNewAreaTip()
            # 待定
            time.sleep(5)
            go1stLairDemon()
            changeRole()
            stop_event.set()
            if i == 3:
                while 1:
                    # backToMain = FindImages.find_template([R.img("角色界面返回按钮.png"), ], confidence=0.95)
                    backToMain = FindImages.find([R.img("角色界面返回按钮1080.png"), ], rect=[848, 0, 1277, 304],
                                                 confidence=0.95)
                    if backToMain:
                        print("回到主界面")
                        action.click(backToMain["center_x"], backToMain["center_y"], 20)
                        break
        IArea += 1


# 从任何位置返回主界面
def from_anywhere_back_to_main():
    # is_already_change_role = False
    # 判断是否达到主界面，“点击选服”作为标志
    print("返回主界面")
    while not FindImages.find([R.img("主界面标识.png"), ], rect=[374, 318, 961, 621], confidence=0.95):
        # 判断是否处于选角色界面
        back_to_main = FindImages.find([R.img("角色界面返回按钮1080.png"), ], rect=[848, 0, 1277, 304], confidence=0.95)
        if back_to_main:
            action.click(back_to_main["center_x"], back_to_main["center_y"], 20)
        # 判断当前是否有战力标识，有的话会点击设置返回主界面
        elif FindImages.find([R.img("战力标志.png"), ], rect=[4, 8, 276, 104], confidence=0.95):
            # if is_already_change_role:
            #     continue
            # else:
            changeRole()
        else:
            # 如果当前有界面遮挡
            close_interface = FindImages.find([R.img("关闭按钮.png"), ], confidence=0.95)
            if close_interface:
                action.click(close_interface["center_x"], close_interface["center_y"], 20)
                # is_already_change_role = True


def log_off_function():
    while 1:
        print("寻找注销按钮")
        log_off = FindImages.find([R.img("注销.png"), ], confidence=0.95)
        if log_off:
            action.click(log_off["center_x"], log_off["center_y"], 20)
            print("点击注销按钮")
            time.sleep(2)
            if FindImages.find_template([R.img("注销.png"), ], confidence=0.95):
                log_off_function()
            else:
                break
        if FindImages.find_template([R.img("切换账号标识.png"), ], confidence=0.95):
            break


def traverse_from_start_infinite_world(areaPattern, start):
    n = len(areaPattern)
    for i in range(n):
        # 计算当前索引
        current_index = (start + i) % n
        areaId = areaPattern[current_index]
        # IArea = 0
        # for i in range(start, start + n):
        # while 1:
        while 1:
            # print(areaPattern[(start + IArea) % n])
            # # i += 1
            # areaId = areaPattern[(start + IArea) % n]
            # areaId = areaPattern[i % n]
            print("区服：", areaId, "寻找选服按钮")
            # res = Ocr.mlkitocr_v2(rect=[385, 330, 1194, 836], pattern='选服')
            res = Ocr.mlkitocr_v2(rect=[385, 284, 953, 655], pattern='选服')
            if res:
                print("点击", res[0].text, "，坐标", res[0].center_x, res[0].center_y)
                action.click(res[0].center_x, res[0].center_y, 20)
                break
        time.sleep(1)
        while 1:
            # 寻找区服
            # area = Ocr.mlkitocr_v2(rect=[191, 98, 1388, 768], pattern=areaId)
            area = Ocr.mlkitocr_v2(rect=[360, 142, 1082, 597], pattern=areaId)
            if area:
                print("找到区服", area[0].text)
                action.click(area[0].center_x, area[0].center_y + 50, 20)
                break
            else:
                print("下滑选区")

                action.Touch.down(469, 565, 20)
                action.Touch.move(459, 246, 3000)
                action.Touch.up(459, 246, 1000)

                # action.Touch.down(459,246, 20)
                # action.Touch.move(469,565, 3000)
                # action.Touch.up(469,565, 1000)
                time.sleep(2)
        # clickRole(1)
        # changeRole()
        # time.sleep(2)
        # clickRole(2)
        # changeRole()
        # clickRole(3)
        # changeRole()
        for j in range(1, 4):
            stop_event = threading.Event()
            stop_event_new_area = threading.Event()
            clickRole(j)
            # 启动关闭活动提示线程
            while 1:
                if FindImages.find([R.img("任务按钮.png"), ], rect=[4, 74, 280, 439],
                                   confidence=0.95) or FindImages.find([R.img("新服连登七天1080.png"), ],
                                                                       rect=[163, 361, 574, 659], confidence=0.95):
                    print("已进入主界面")
                    break
            activity_thread = threading.Thread(target=closeActivityTips, args=(stop_event,))
            close_new_area_tip_thread = threading.Thread(target=close_new_area_tip, args=(stop_event_new_area,))
            try:
                activity_thread.start()
                close_new_area_tip_thread.start()
            # thread2.start()
            except:
                print("Error: unable to start thread")
            # closeNewAreaTip()
            # 待定
            time.sleep(5)
            go3stWorldDemon()
            changeRole()
            stop_event.set()
            stop_event_new_area.set()
            if j == 3:
                while 1:
                    # backToMain = FindImages.find_template([R.img("角色界面返回按钮.png"), ], confidence=0.95)
                    backToMain = FindImages.find([R.img("角色界面返回按钮1080.png"), ], rect=[848, 0, 1277, 304],
                                                 confidence=0.95)
                    if backToMain:
                        print("回到主界面")
                        action.click(backToMain["center_x"], backToMain["center_y"], 20)
                        break
        # IArea += 1
        # 点击注销
        # log_off_function()


def choose_account(account):
    print("当前账号：", account)


# 开启自动刷巢一
# traverse_from_start_infinite(areaPattern, 1)
def traverse_from_start_infinite_world_account(account_pattern, account_no, areaPattern, start):
    while 1:
        n = len(account_pattern)
        index = account_no
        is_select = False
        while True:
            account = account_pattern[index]
            # for account in account_pattern:

            print("要登录的账号：", account)
            # 更新索引
            index = (index + 1) % n
            if is_select:
                is_select = False
                print("跳过注销")
            else:
                log_off_function()
            time.sleep(3)
            while 1:
                print("寻找切换账号标识")
                if FindImages.find_template([R.img("切换账号标识.png"), ], confidence=0.95):
                    print("已找到切换账号标识")
                    break
            while 1:
                print("开始切换账号")
                if Selector().text(account).parent().find():
                    node = Selector(1).id("com.m4399.gamecenter:id/iv_islogin").parent(1).brother().type(
                        "TextView").text(
                        account).find()

                    # for n in node:
                    #     print(n)
                    # node = Selector(1).id("com.m4399.gamecenter:id/rl_deleteview").brother().find()
                    # for n in node:
                    if node:
                        print("已选中当前账号，", node.text)
                        is_select = True
                        break
                    time.sleep(2)
                    while 1:
                        print("选择账号")
                        if Selector().text(account).parent().find():
                            Selector().text(account).parent().click().find()
                            time.sleep(2)
                            # break
                        if FindImages.find([R.img("确认登录界面.png"),],confidence= 0.95):
                            break
                    break
                    # time.sleep(1)
            if is_select:
                # is_select = False
                continue
            #
            # node = Selector(1).id("com.m4399.gamecenter:id/iv_islogin").parent(1).brother().type("TextView").text(account).find()
            #
            # # for n in node:
            # #     print(n)
            # # node = Selector(1).id("com.m4399.gamecenter:id/rl_deleteview").brother().find()
            # # for n in node:
            # if node:
            #     print("已选中当前账号，", node.text)
            #     is_select = True
            #     continue
            # time.sleep(1)
            # Selector().text(account).parent().click().find()
            # time.sleep(1)
            while 1:
                print("确认登录")
                if FindImages.find([R.img("确认登录界面.png"),],confidence= 0.95):
                    Selector().id("com.m4399.gamecenter:id/btn_oauth").click().find()
                    break
                # if FindImages.find([R.img("注销.png"), ], confidence=0.95):
                #     break
            # Selector().id("com.m4399.gamecenter:id/btn_oauth").click().find()
            time.sleep(2)
            while 1:
                if FindImages.find([R.img("注销.png"), ], confidence=0.95):
                    print("已进入登录主界面")
                    break
            # while not FindImages.find([R.img("注销.png"), ], confidence=0.95):
            #     print("已进入登录主界面")
            time.sleep(2)
            Selector().id("com.sy4399.jllfx:id/m4399_ope_id_base_dialog_iv_close").find()
            time.sleep(2)
            Selector().packageName("com.sy4399.jllfx").id("com.sy4399.jllfx:id/m4399_id_tv_positive").text(
                "已阅读并同意").find()
            time.sleep(2)
            Selector().id("com.sy4399.jllfx:id/m4399_ope_id_base_dialog_iv_close").click().find()
            # Selector().id("com.sy4399.jllfx:id/m4399_ope_id_base_dialog_iv_close").packageName(
            #     "com.sy4399.jllfx").click().find()
            traverse_from_start_infinite_world(areaPattern, start)
            is_select = False


# 自动创角角色
def traverse_from_start_infinite_creat_role(areaPattern, start, role_name):
    n = len(areaPattern)
    IArea = 0
    while 1:
        while 1:
            print(areaPattern[(start + IArea) % n])
            # i += 1
            areaId = areaPattern[(start + IArea) % n]
            print("寻找选服按钮")
            # res = Ocr.mlkitocr_v2(rect=[385, 330, 1194, 836], pattern='选服')
            res = Ocr.mlkitocr_v2(rect=[385, 284, 953, 655], pattern='选服')
            if res:
                print("点击", res[0].text, "，坐标", res[0].center_x, res[0].center_y)
                action.click(res[0].center_x, res[0].center_y, 20)
                break
        time.sleep(1)
        while 1:
            # 寻找区服
            # area = Ocr.mlkitocr_v2(rect=[191, 98, 1388, 768], pattern=areaId)
            area = Ocr.mlkitocr_v2(rect=[360, 142, 1082, 597], pattern=areaId)
            if area:
                print("找到区服", area[0].text)
                action.click(area[0].center_x, area[0].center_y + 50, 20)
                break
            else:
                print("下滑选区")

                action.Touch.down(469, 565, 20)
                action.Touch.move(459, 246, 3000)
                action.Touch.up(459, 246, 1000)
                time.sleep(2)
        while 1:
            time.sleep(1)
            empty_role = FindImages.find([R.img("左侧创角按钮1080.png"), ], confidence=0.95)
            empty_role_3 = FindImages.find([R.img("创角第三个1080.png"), ], confidence=0.95)
            time.sleep(1)
            if empty_role or empty_role_3:
                stop_event = threading.Event()
                # stop_event_new_area = threading.Event()
                creatRole(role_name)
                # 启动关闭活动提示线程
                activity_thread = threading.Thread(target=closeActivityTips, args=(stop_event,))
                close_new_area_tip_thread = threading.Thread(target=close_new_area_tip)
                try:
                    activity_thread.start()
                    close_new_area_tip_thread.start()
                # thread2.start()
                except:
                    print("Error: unable to start thread")
                # closeNewAreaTip()
                time.sleep(5)
                changeRole()
            else:
                # i == 3
                backToMain = FindImages.find([R.img("角色界面返回按钮1080.png"), ], rect=[848, 0, 1277, 304],
                                             confidence=0.95)
                if backToMain:
                    print("回到主界面")
                    action.click(backToMain["center_x"], backToMain["center_y"], 20)
                    break
        IArea += 1


def clickRoleOrCreateRole(rolenumber, role_name):
    time.sleep(1)
    # is_start = True
    while 1:
        print("寻找开始游戏按钮")
        # startGame = Ocr.mlkitocr_v2(rect=[415, 436, 1594, 897], pattern='开始游戏')
        # start_game = FindImages.find_template([R.img("选角界面开始游戏按钮.png"), ], confidence=0.95)
        start_game = FindImages.find([R.img("选角界面开始游戏按钮1080.png"), ], rect=[824, 445, 1277, 717],
                                     confidence=0.95)
        if start_game:
            if rolenumber == 1:
                print("点击第一个角色")
                action.click(103, 174, 20)
                action.click(103, 174, 20)
            if rolenumber == 2:
                action.click(105, 321, 20)
                action.click(105, 321, 20)
                is_blank_role = FindImages.find([R.img("左侧创角按钮1080.png"), ], rect=[28, 227, 193, 405],
                                                confidence=0.95)
                if is_blank_role:
                    # creatRole(role_name,2)
                    creatRole(role_name)
                    print("创建第二个角色")
                    break
                print("点击第二个角色")
            if rolenumber == 3:
                action.click(107, 472, 20)
                action.click(107, 472, 20)
                is_blank_role_3 = FindImages.find([R.img("创角第三个1080.png"), ], confidence=0.95)
                if is_blank_role_3:
                    # creatRole(role_name,3)
                    creatRole(role_name)
                    print("创建第三个角色")
                    break
                print("点击第三个角色")

            print("开始游戏")
            time.sleep(1.5)
            action.click(start_game["center_x"], start_game["center_y"], 20)
            # action.click(startGame[0].center_x, startGame[0].center_y, 20)
            time.sleep(1.5)
            action.click(start_game["center_x"], start_game["center_y"], 20)
            # action.click(startGame[0].center_x, startGame[0].center_y, 20)
            time.sleep(5)
            # 如果卡在了选角界面
            # while Ocr.mlkitocr_v2(rect=[415, 436, 1594, 897], pattern='开始游戏'):
            #     # 卡在了选角界面
            #     print("卡在了选角界面")
            #     time.sleep(0.5)
            #     action.click(start_game["center_x"], start_game["center_y"], 20)
            #     # action.click(startGame[0].center_x, startGame[0].center_y, 20)
            #     break
            if FindImages.find([R.img("选角界面开始游戏按钮1080.png"), ], rect=[824, 445, 1277, 717], confidence=0.95):
                clickRoleOrCreateRole(rolenumber, role_name)
            else:
                break

        # while is_start:
        #     if Ocr.mlkitocr_v2(rect=[824,445,1277,717], pattern='开始游戏'):
        #         continue
        #     else:
        #         is_start = False


def traverse_from_start_infinite_creat_role_upgrade(areaPattern, start, role_name, level):
    n = len(areaPattern)
    IArea = 0
    while 1:
        while 1:
            print(areaPattern[(start + IArea) % n])
            # i += 1
            areaId = areaPattern[(start + IArea) % n]
            print("寻找选服按钮")
            # res = Ocr.mlkitocr_v2(rect=[385, 330, 1194, 836], pattern='选服')
            res = Ocr.mlkitocr_v2(rect=[385, 284, 953, 655], pattern='选服')
            if res:
                print("点击", res[0].text, "，坐标", res[0].center_x, res[0].center_y)
                action.click(res[0].center_x, res[0].center_y, 20)
                break
        time.sleep(1)
        while 1:
            # 寻找区服
            # area = Ocr.mlkitocr_v2(rect=[191, 98, 1388, 768], pattern=areaId)
            area = Ocr.mlkitocr_v2(rect=[360, 142, 1082, 597], pattern=areaId)
            if area:
                print("找到区服", area[0].text)
                action.click(area[0].center_x, area[0].center_y + 50, 20)
                break
            else:
                print("下滑选区")
                action.Touch.down(469, 565, 20)
                action.Touch.move(459, 246, 3000)
                action.Touch.up(459, 246, 1000)
                time.sleep(2)
        for i in range(1, 4):
            stop_event = threading.Event()
            # stop_event_new_area = threading.Event()
            clickRoleOrCreateRole(i, role_name)
            # 启动关闭活动提示线程
            activity_thread = threading.Thread(target=closeActivityTips, args=(stop_event,))
            close_new_area_tip_thread = threading.Thread(target=close_new_area_tip)
            try:
                activity_thread.start()
                close_new_area_tip_thread.start()
            # thread2.start()
            except:
                print("Error: unable to start thread")
            # closeNewAreaTip()
            # 待定
            time.sleep(5)
            is_level_72_stop = autoUpgrade(level)
            print("is_level_72_stop:", is_level_72_stop, ",i", i)
            if is_level_72_stop == 0:
                i -= 1
                print("i", i)
                stop_event.set()
                continue
            stop_event.set()
            if i == 3:
                while 1:
                    # backToMain = FindImages.find_template([R.img("角色界面返回按钮.png"), ], confidence=0.95)
                    backToMain = FindImages.find([R.img("角色界面返回按钮1080.png"), ], rect=[848, 0, 1277, 304],
                                                 confidence=0.95)
                    if backToMain:
                        print("回到主界面")
                        action.click(backToMain["center_x"], backToMain["center_y"], 20)
                        break
        IArea += 1


# 输入角色名，如果角色名出错（敏感或者重复）则嵌套调用重新输入
def input_role_name(role_name):
    action.click(586, 651)
    time.sleep(2)
    # # 当前控件 输入文本
    node = Selector().type("EditText").packageName("com.sy4399.jllfx").find()
    if node:
        time.sleep(1)
        id = random.randint(0, 100)
        new_role_name = role_name + str(id)
        node.input(new_role_name)
        time.sleep(1)
        # confirm_button = Ocr.mlkitocr_v2(rect=[663, 332, 1275, 709], pattern='确定')
        # time.sleep(1)
        # action.click(confirm_button[0].center_x, confirm_button[0].center_y, 20)
        action.click(1204, 670)
        time.sleep(1)
        while 1:
            creat_role_button = FindImages.find([R.img("创角1080.png"), ], rect=[788, 397, 1267, 703], confidence=0.95)
            if creat_role_button:
                action.click(creat_role_button["center_x"], creat_role_button["center_y"], 20)
                time.sleep(2)
                while FindImages.find([R.img("创角1080.png"), ], rect=[788, 397, 1267, 703], confidence=0.95):
                    input_role_name(role_name)
                break


# 自动升级
def creatRole(role_name):
    # is_blank_role = FindImages.find([R.img("左侧创角按钮1080.png"), ], confidence=0.95)
    # is_blank_role_3 = FindImages.find([R.img("创角第三个1080.png"), ], confidence=0.95)
    # if is_blank_role or is_blank_role_3:
    #     time.sleep(1)
    #     if is_blank_role:
    #         action.click(is_blank_role["center_x"], is_blank_role["center_y"], 20)
    #     elif is_blank_role_3:
    #         action.click(is_blank_role_3["center_x"], is_blank_role_3["center_y"], 20)
    time.sleep(1)
    action.click(106, 177)
    action.click(106, 177)
    action.click(106, 177)

    time.sleep(2)
    input_role_name(role_name)
    # action.click(586,651)
    # time.sleep(2)
    # # # 当前控件 输入文本
    # node = Selector().type("EditText").packageName("com.sy4399.jllfx").find()
    # if node:
    #     time.sleep(1)
    #     id = random.randint(0,100)
    #     role_name = role_name+ str(id)
    #     node.input(role_name)
    #     time.sleep(1)
    #     # confirm_button = Ocr.mlkitocr_v2(rect=[663, 332, 1275, 709], pattern='确定')
    #     # time.sleep(1)
    #     # action.click(confirm_button[0].center_x, confirm_button[0].center_y, 20)
    #     action.click(1204,670)
    #     time.sleep(1)
    #     while 1:
    #         creat_role_button = FindImages.find([R.img("创角1080.png"), ], rect=[788, 397, 1267, 703], confidence=0.95)
    #         if creat_role_button:
    #             action.click(creat_role_button["center_x"], creat_role_button["center_y"], 20)
    #             time.sleep(2)
    #             while FindImages.find([R.img("创角1080.png"), ], rect=[788, 397, 1267, 703], confidence=0.95):
    #                 input_role_name()
    #             break


def autoUpgrade(level):
    # start_time = time.time()
    times_72 = 0
    if level == 110:
        i = 1
        is_level_62 = False
        while 1:

            # action.click(1383, 47, 20)
            action.click(1114, 40, 20)
            print("点击")
            level_110 = FindImages.find([R.img("110级1080.png"), ], rect=[0, 2, 137, 137], confidence=0.95)

            lv = Ocr.mlkitocr_v2(rect=[46, 6, 90, 104])
            if lv:
                # print(re.findall(r"\d+", lv[0].text)[0])
                # lv = int(re.findall(r"\d+", lv[0].text)[0])

                if bool(re.search(r'\d', lv)):
                    lv = int(re.findall(r"\d+", lv[0].text)[0])
                    print("当前等级：", lv)
                    if lv >= 110:
                        changeRole()
                        return 1
            if level_110:
                changeRole()
                return 1
            # time.sleep(0.5)
            if i == 1:
                # noviceVillageCopy = FindImages.find([R.img("新手村副本按钮.png"), ], confidence=0.95)
                noviceVillageCopy = FindImages.find([R.img("新手村副本按钮（新）.png"), ], confidence=0.95)
                if noviceVillageCopy:
                    # time.sleep(1)
                    print(1)
                    print("i=", i)
                    action.click(noviceVillageCopy["center_x"], noviceVillageCopy["center_y"], 20)
                    time.sleep(2)
                    # goNoviceVillageCopy = FindImages.find([R.img("新手村副本前往按钮.png"), ], confidence=0.95)
                    goNoviceVillageCopy = FindImages.find([R.img("新手村副本前往按钮（新）.png"), ], confidence=0.95)
                    if goNoviceVillageCopy:
                        action.click(goNoviceVillageCopy["center_x"], goNoviceVillageCopy["center_y"], 20)
                        i = 0
            # isLevel6x = False | FindImages.find_template([R.img("等级6开头.png"), ], confidence=0.95) | FindImages.find_template([R.img("等级7开头.png"), ], confidence=0.95) | FindImages.find_template([R.img("等级8开头.png"), ], confidence=0.95)
            # current_time = time.time()
            # immortalAllianceMission = FindImages.find([R.img("仙盟任务.png"), ], confidence=0.95)
            level_62 = Ocr.mlkitocr_v2(rect=[2, 6, 151, 145], pattern='62')
            # if level_62:
            #     is_level_62 = True
            # if is_level_62:
            immortalAllianceMission = FindImages.find(
                [R.img("新手村副本前往按钮（新）.png"), R.img("仙盟任务（新）.png"), ], confidence=0.95)
            # if isLevel6x:
            # if current_time
            skip = FindImages.find([R.img("调过引导.png"), ], rect=[743, 0, 1277, 250], confidence=0.95)
            if skip:
                action.click(skip["center_x"], skip["center_y"], 20)
            if immortalAllianceMission:
                action.click(immortalAllianceMission["center_x"], immortalAllianceMission["center_y"], 20)
                action.click(immortalAllianceMission["center_x"] - 40, immortalAllianceMission["center_y"], 20)
                time.sleep(1)
            level_72 = Ocr.mlkitocr_v2(rect=[2, 6, 151, 145], pattern='72')
            level_110 = FindImages.find([R.img("110级1080.png"), ], rect=[0, 2, 137, 137], confidence=0.95)

            lv = Ocr.mlkitocr_v2(rect=[46, 6, 90, 104])
            if lv:
                print(re.findall(r"\d+", lv[0].text)[0])
                lv = int(re.findall(r"\d+", lv[0].text)[0])
                if lv >= 110:
                    changeRole()
                    return 1
            if level_110:
                changeRole()
                return 1
            if level_72:
                times_72 += 1
                if times_72 > 10:
                    changeRole()
                    return 0
    if level == 200:
        while 1:
            lv = Ocr.mlkitocr_v2(rect=[46, 6, 90, 104])
            if lv:
                # print(re.findall(r"\d+", lv[0].text)[0])
                # lv = int(re.findall(r"\d+", lv[0].text)[0])
                if bool(re.search(r'\d', lv[0].text)):
                    lv = int(re.findall(r"\d+", lv[0].text)[0])
                    print("当前等级：", lv)
                    if lv >= 200 or Ocr.mlkitocr_v2(rect=[2, 6, 151, 145], pattern='200') or FindImages.find(
                            [R.img("LV200.png"), ], rect=[2, 0, 116, 125], confidence=0.95):
                        changeRole()
                        return 1
            elif Ocr.mlkitocr_v2(rect=[2, 6, 151, 145], pattern='200') or FindImages.find([R.img("LV200.png"), ],
                                                                                          rect=[2, 0, 116, 125],
                                                                                          confidence=0.95):
                changeRole()
                return 1
            skip = FindImages.find([R.img("调过引导.png"), ], rect=[743, 0, 1277, 250], confidence=0.95)
            if skip:
                action.click(skip["center_x"], skip["center_y"], 20)
            noviceVillageCopy = FindImages.find([R.img("新手村副本按钮（新）.png"), ], confidence=0.95)
            if noviceVillageCopy:
                # time.sleep(1)
                action.click(noviceVillageCopy["center_x"], noviceVillageCopy["center_y"], 20)
                time.sleep(2)
                # goNoviceVillageCopy = FindImages.find([R.img("新手村副本前往按钮.png"), ], confidence=0.95)
                goNoviceVillageCopy = FindImages.find([R.img("新手村副本前往按钮（新）.png"), ], confidence=0.95)
                if goNoviceVillageCopy:
                    action.click(goNoviceVillageCopy["center_x"], goNoviceVillageCopy["center_y"], 20)
            next = FindImages.find([R.img("下一关.png"), ], rect=[370, 469, 971, 709], confidence=0.95)
            if next:
                action.click(next["center_x"], next["center_y"], 20)
            click_exit = FindImages.find([R.img("点击退出界面.png"), ], rect=[411, 431, 923, 661], confidence=0.95)
            jyd = FindImages.find([R.img("战纹卷轴经验丹.png"), ], rect=[735, 201, 1017, 488], confidence=0.95)
            if jyd:
                action.click(875, 429)
            if click_exit:
                action.click(633, 615)
            if FindImages.find([R.img("低于推荐战力.png"), ], rect=[366, 484, 864, 683], confidence=0.95):
                action.click(518, 459)
                time.sleep(0.5)
                action.click(1136, 62)
                break
            if FindImages.find([R.img("战纹失败.png"), ], rect=[382, 205, 897, 506], confidence=0.95):
                # 点击取消
                action.click(521, 461)
                # 关闭
                time.sleep(0.5)
                action.click(1128, 64)
                break
                # break

        while 1:
            lv = Ocr.mlkitocr_v2(rect=[46, 6, 90, 104])
            if lv:
                print(re.findall(r"\d+", lv[0].text)[0])
                lv = int(re.findall(r"\d+", lv[0].text)[0])
                if lv >= 200 or Ocr.mlkitocr_v2(rect=[2, 6, 151, 145], pattern='200') or FindImages.find(
                        [R.img("LV200.png"), ], rect=[2, 0, 116, 125], confidence=0.95):
                    changeRole()
                    return 1
            elif Ocr.mlkitocr_v2(rect=[2, 6, 151, 145], pattern='200') or FindImages.find([R.img("LV200.png"), ],
                                                                                          rect=[2, 0, 116, 125],
                                                                                          confidence=0.95):
                changeRole()
                return 1

            action.click(1114, 40, 20)
            print("点击")
            time.sleep(0.5)
            skip_con = FindImages.find([R.img("跳过对话.png"), ], rect=[909, 4, 1277, 155], confidence=0.95)
            if skip_con:
                action.click(skip_con["center_x"], skip_con["center_y"], 20)
            auto_con = FindImages.find([R.img("自动继续.png"), ], rect=[987, 2, 1269, 713], confidence=0.95)
            mail = FindImages.find_all_template([R.img("邮件.png"), ], rect=[673, 437, 1013, 715], confidence=0.95)
            if mail:
                action.click(880, 675)
                time.sleep(0.5)
                action.click(570, 601)
                time.sleep(0.5)
                action.click(1026, 601)
                time.sleep(0.5)
                action.click(880, 675)
                time.sleep(0.5)
            if auto_con:
                action.click(auto_con["center_x"], auto_con["center_y"], 20)
            rw_110 = FindImages.find([R.img("110击杀世界魔王.png"), ], rect=[2, 133, 334, 453], confidence=0.95)
            if rw_110:
                action.click(rw_110["center_x"], rw_110["center_y"], 20)
                time.sleep(0.5)
                action.click(1066, 116)
                time.sleep(0.5)
                action.click(1003, 603)
                time.sleep(1.5)
            rw_110_2 = FindImages.find([R.img("110对话钱老爷.png"), ], rect=[2, 149, 310, 427], confidence=0.95)
            if rw_110_2:
                action.click(rw_110_2["center_x"], rw_110_2["center_y"], 20)
            rw_111 = FindImages.find([R.img("111对话护法龙女.png"), ], rect=[2, 129, 336, 471], confidence=0.95)
            if rw_111:
                action.click(rw_111["center_x"], rw_111["center_y"], 20)
            # 装备副本
            rw_112 = FindImages.find([R.img("112装备副本.png"), ], rect=[4, 133, 344, 443], confidence=0.95)
            if rw_112:
                time.sleep(1)
                action.click(rw_112["center_x"], rw_112["center_y"], 20)
                # action.click(173,242)
                time.sleep(0.5)
                action.click(1227, 118)
                time.sleep(0.5)
                action.click(1140, 231)
                time.sleep(0.5)
                action.click(862, 598)
                # time.sleep(50)
            # if FindImages.find([R.img("低于推荐战力.png"),],rect= [366,484,864,683] ,confidence= 0.95):
            if FindImages.find([R.img("战力低于推荐战力2.png"), ], rect=[380, 207, 901, 510], confidence=0.95):
                action.click(518, 459)
                time.sleep(0.5)
                action.click(1136, 62)
            rw_112_2 = FindImages.find([R.img("112护法龙女.png"), ], rect=[2, 133, 322, 435], confidence=0.95)
            if rw_112_2:
                action.click(rw_112_2["center_x"], rw_112_2["center_y"], 20)
            rw_120 = FindImages.find([R.img("120繁花锦.png"), ], rect=[6, 133, 352, 439], confidence=0.95)
            if rw_120:
                action.click(rw_120["center_x"], rw_120["center_y"], 20)
            rw_121 = FindImages.find([R.img("121击败诅咒之手.png"), ], rect=[2, 139, 322, 439], confidence=0.95)
            if rw_121:
                action.click(rw_121["center_x"], rw_121["center_y"], 20)
            rw_132 = FindImages.find([R.img("132骑宠副本.png"), ], rect=[2, 143, 328, 429], confidence=0.95)
            if rw_132:
                action.click(rw_132["center_x"], rw_132["center_y"], 20)
                time.sleep(0.5)
                action.click(1217, 110)
                time.sleep(0.5)
                action.click(1009, 601)
                time.sleep(20)
                action.click(1124, 62)
                time.sleep(20)
                if FindImages.find([R.img("骑宠副本标识.png"), ], rect=[173, 52, 624, 296], confidence=0.95):
                    action.click(1132, 66)
            rw_140_yizhuan = FindImages.find([R.img("一转.png"), ], rect=[2, 133, 334, 427], confidence=0.95)
            if rw_140_yizhuan:
                action.click(rw_140_yizhuan["center_x"], rw_140_yizhuan["center_y"], 20)
                while 1:
                    if FindImages.find([R.img("完成转生.png"), ], rect=[598, 272, 899, 504], confidence=0.95):
                        action.click(753, 390)
                        print("可完成转生")
                        break
                    else:
                        print("不可完成转生")
                    time.sleep(0.5)
                    while 1:
                        zwjz = FindImages.find([R.img("战纹卷轴完成.png"), ], rect=[516, 270, 1021, 530],
                                               confidence=0.95)
                        if zwjz:
                            print("战纹卷轴已完成")
                            if FindImages.find([R.img("战纹卷轴任务.png"), ], rect=[338, 92, 983, 441],
                                               confidence=0.95):
                                action.click(874, 172)
                            break
                        else:
                            print("战纹卷轴未完成")
                            action.click(950, 420)

                    # while not FindImages.find([R.img("战纹卷轴完成.png"),],rect= [516,270,1021,530] ,confidence= 0.95):
                    #     action.click(950,420)
                    time.sleep(0.5)
                    # cdzb = FindImages.find([R.img("穿戴装备完成.png"), ], rect=[461, 278, 1011, 530], confidence=0.95)
                    cdzb = FindImages.find([R.img("穿戴装备完成.png"), ], rect=[514, 361, 620, 496], confidence=0.95)
                    if cdzb:
                        print("穿戴装备已完成")
                        continue
                    else:
                        print("穿戴装备未完成")
                        action.click(555, 420)
                    time.sleep(0.5)

            rw_140_2 = FindImages.find([R.img("完成1转.png"), ], rect=[6, 149, 334, 445], confidence=0.95)
            if rw_140_2:
                action.click(rw_140_2["center_x"], rw_140_2["center_y"], 20)
            # 地阶经验丹
            djjyd = FindImages.find([R.img("低阶经验丹.png"), ], rect=[748, 216, 1025, 514], confidence=0.95)
            if djjyd:
                action.click(875, 426)
            if FindImages.find([R.img("150穿戴5阶装备.png"), ], rect=[0, 139, 332, 433], confidence=0.95):
                if FindImages.find([R.img("新手村副本按钮（新）.png"), ], confidence=0.95):
                    action.click(1225, 121)
                    time.sleep(0.5)
                    action.click(1134, 242)
                    time.sleep(0.5)
                    action.click(838, 598)
                    time.sleep(0.5)
                    action.click(755, 475)
                    time.sleep(5)
                    for i in range(1, 20):
                        action.click(643, 484)
                    time.sleep(1)
                    action.click(874, 191)
                    time.sleep(0.5)
                    action.click(824, 266)
                    time.sleep(0.5)
                    action.click(931, 118)
                    time.sleep(0.5)
                    # action.click(1142,421)

                    # fb = FindImages.find([R.img("副本按钮.png"), ], rect=[703, 6, 1275, 322], confidence=0.95)

                else:
                    # aboveChangeButton = FindImages.find_template([R.img("右上角切换按钮.png"), ], confidence=0.95)
                    aboveChangeButton = FindImages.find([R.img("右上角切换按钮1080.png"), ], rect=[890, 0, 1277, 284],
                                                        confidence=0.95)
                    if aboveChangeButton:
                        action.click(aboveChangeButton["center_x"], aboveChangeButton["center_y"], 20)

            rw_200 = FindImages.find([R.img("200前辈.png"), ], rect=[2, 106, 293, 462], confidence=0.95)
            if rw_200:
                # 点击副本按钮
                action.click(1233, 117)
                time.sleep(0.5)
                # 点击组队副本
                action.click(1129, 238)
                time.sleep(0.5)
                # 点击单人进入
                action.click(822, 596)
                time.sleep(0.5)
                action.click(764, 473)
            immortalAllianceMission = FindImages.find([R.img("仙盟任务（新）.png"), ], rect=[4, 137, 328, 306],
                                                      confidence=0.95)
            if immortalAllianceMission:
                action.click(immortalAllianceMission["center_x"], immortalAllianceMission["center_y"], 20)
                action.click(immortalAllianceMission["center_x"] - 60, immortalAllianceMission["center_y"], 20)
                time.sleep(1)
            if FindImages.find([R.img("百变门票礼盒.png"), ], rect=[713, 209, 1036, 492], confidence=0.95):
                action.click(972, 247)
            # 972,247
            if FindImages.find([R.img("属性丹.png"), ], rect=[753, 213, 1032, 512], confidence=0.95):
                action.click(972, 247)


def get_red_envelope(mode, sleep_time, revise_times, get_red_envelope_click_times):
    if mode == "model_simple":
        print("领红包简单模式")
        while 1:
            for i in range(0,get_red_envelope_click_times):
                action.click(345,386)
                time.sleep(sleep_time)
            for i in range(0,revise_times):
                action.click(128,428)
                time.sleep(sleep_time)
            for i in range(0,revise_times):
                action.click(125,351)
                time.sleep(sleep_time)
    if mode == "model_photo":
        print("领红包识图模式")
        while 1:
            while 1:
                red_envelope = FindImages.find_template([R.img("领红包.png"), ], rect=[23, 32, 476, 565], confidence=0.95)
                if red_envelope:
                    action.click(red_envelope["center_x"], red_envelope["center_y"], 20)
                    time.sleep(sleep_time)
                elif FindImages.find_template([R.img("红包已领完.png"),],rect= [23, 32, 476, 565] ,confidence= 0.95):
                    break
            for i in range(0,revise_times):
                action.click(128,428)
                time.sleep(sleep_time)
            for i in range(0,revise_times):
                action.click(125,351)
                time.sleep(sleep_time)

# 开启自动升级
# autoUpgrade()

# # 克隆GitHub仓库
# def clone_repo(repo_url, clone_dir):
#     Repo.clone_from(repo_url, clone_dir)
#
#
# # 拉取最新更新
# def pull_repo(repo_dir):
#     repo = Repo(repo_dir)
#     origin = repo.remotes.origin
#     origin.pull()

# 克隆GitHub仓库
def clone_repo(repo_url, clone_dir):
    subprocess.run(['git', 'clone', repo_url, clone_dir])

# 拉取最新更新
def pull_repo(repo_dir):
    subprocess.run(['git', '-C', repo_dir, 'pull'])




# 构建一个WebWindow 显示‘/ui/a.html’
def tunnel(k, v):
    print(k)

    # # 示例：克隆一个仓库
    # repo_url = 'https://github.com/WuRuoHui/auto_ganme.git'
    # clone_dir = '/storage/emulated/0/new'
    # clone_repo(repo_url, clone_dir)
    #
    # # 示例：拉取仓库最新更新
    # pull_repo(clone_dir)

    if k == "submit":
        res = json.loads(v)
        print(res['Function'])
        print(res['no_demon_king'])
        if res['Function'] == 'get_red_envelope':
            print("开始领红包")
            get_red_envelope(res['get_red_envelope'], float(res['get_red_envelope_sleep_time']), int(res['revise_times']), int(res['get_red_envelope_click_times']))
        from_anywhere_back_to_main()
        if res['Function'] == 'kill_the_nest_one_demon_king':
            print("启动自动刷巢一")
            traverse_from_start_infinite(areaPattern, int(res['no_demon_king']))
        if res['Function'] == 'kill_the_world_three_demon_king':
            # print(res['account'])
            # print(res['account_no'])
            traverse_from_start_infinite_world_account(res['account'].split(","), int(res['account_no']), areaPattern,
                                                       int(res['no_demon_king']))
        if res['Function'] == 'auto_upgrade':
            print("启动自动升级")
            # autoUpgrade()
            # traverse_from_start_infinite_creat_role(areaPattern,0,"中尉")
            print(res['role_name'])
            traverse_from_start_infinite_creat_role_upgrade(areaPattern, int(res['no_demon_king']), res['role_name'],
                                                            int(res['level']))
    if k == "cancel":
        print("cancel")
        # while 1:
        #     print("当前进程：", os.getpid())
        #     print("父进程：", os.getppid())
        # sys.exit()


w = WebWindow(R.ui('index.html'), tunnel)
w.show()
