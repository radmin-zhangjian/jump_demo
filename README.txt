#Wed Apr 19 11:19:51 MSK 2017
Pkg.Revision=26 rc1

Android Debug Bridge version 1.0.39
Revision 5943271ace17-android



使用adb devices命令发现开发板始终处于offline状态。

网上提供的解决方法是：

adb kill-server

adb start-server

adb remount

按顺序输入这些命令就可以解决，可我试了好多次都不成功。

用adb version查看版本后发现是1.0.29——较低的版本，现在的设备已经不支持了。

后来我把adb的版本更新到了1.0.36，成功解决了问题。