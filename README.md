# braille_switch

## 実行方法
```
$ cd ~/catkin_ws/src/
$ git clone https://github.com/asakawafuko/braille_switch.git
$ cd ..
$ catkin_make
$ cd /src/braille_switch/driver/RaspberryPiMouse/utils
$ ./build_install.bash
$ roslaunch braille_switch switch.launch
```
## License

このリポジトリはGPLv3ライセンスで公開されています。詳細は[COPYING](./COPYING)を確認してください。

### Includings

このリポジトリは以下に示すリポジトリのコードを一部含みます。

* [ラズパイマウス用デバイスドライバ](https://github.com/rt-net/RaspberryPiMouse)
  * GPL v3 License
