#!/usr/bin/env bash

hour=$(date +%H)
min=$(date +%M)

if [ $hour -ge 1 ] && [ $hour -le 6 ];
then
  echo "啊啦…… 是凌晨呢！你看现在都已经 $hour:$min 啦！快去睡觉！！"

elif [ $hour -gt 6 ] && [ $hour -lt 12 ];
then
  echo "早上好！现在是 $hour:$min~ 是元气满满的一天呢！"

elif [ $hour -eq 12 ];
then
  echo "中午啦！已经 $hour:$min 惹！不要忘记吃中饭哦~"

elif [ $hour -gt 12 ] && [ $hour -le 17 ];
then
  echo "下午好哦~ 现在是 $hour:$min，可以弄点小鱼干吃哦 ww"


elif [ $hour -gt 17 ] && [ $hour -le 21 ];
then
  echo "已经晚上了呢~ 唔喵…… 是 $hour:$min…… 脑袋有点不清楚了呢~"

else
  echo "$hour:$min 惹~ 夜深了呢~ 快去陪着 Apple 酱睡觉吧！"
fi
