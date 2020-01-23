# braille_switch

## 実行方法
```
$ cd ~/catkin_ws/src/
$ git clone https://github.com/asakawafuko/braille_switch.git
$ cd ..
$ catkin_make
$ cd /src/braille_switch/driver/RaspberryPiMouse/src/driver
$ make
$ sudo insmod rtmouse.ko
$ sudo chmod 666 /dev/rtswitch*
$ roslaunch braille_switch switch.launch
```
