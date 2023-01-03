#!/bin/env python3

import time

now_time = time.localtime()

int_hour = now_time.tm_hour

min = str(now_time.tm_min) if len(str(now_time.tm_min)) != 1 else f"0{now_time.tm_min}"

hour = str(now_time.tm_hour) if len(str(now_time.tm_hour)) != 1 else f"0{now_time.tm_hour}"

if 1 <= int_hour <= 6:
    greeting = f"啊啦…… 是凌晨呢！你看现在都已经 {hour}:{min} 啦！快去睡觉！！"
elif int_hour <= 11:
    greeting = f"早上好！现在是 {hour}:{min}~ 是元气满满的一天呢！"
elif int_hour == 12:
    greeting = f"中午啦！已经 {hour}:{min} 惹！不要忘记吃中饭哦~"
elif int_hour <= 17:
    greeting = f"下午好哦~ 现在是 {hour}:{min}，可以弄点小鱼干吃哦 ww"
elif int_hour <= 21:
    greeting = f"已经晚上了呢~ 唔喵…… 是 {hour}:{min}…… 脑袋有点不清楚了呢~"
else:
    greeting = f"{hour}:{min} 惹~ 夜深了呢~ 快去陪着 Apple 酱睡觉吧！"
    
print(greeting)

