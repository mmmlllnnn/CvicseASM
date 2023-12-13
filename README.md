# CvicseASM
## 作用
- 中创软件ASM小助手上网认证绕过，无需认证直接上网
- 电脑限制解除(比如不能安装Navicat、Xshell等)


## 环境
```
python3.7+
```

## 使用方式

直接运行test.py文件即可
```
python test.py
```
然后会提示输入要上网的设备号，这个在网页认证界面可以抓到，是一个很明显的5位数字。

## 备注
也写了一个js版本的（test.js），不需要忽略即可

## 释放权限
公司限制了Navicat和Xshell全家桶的使用，一运行就会被小助手把进程杀掉，遂写了一个.reg修改其注册表，来解除限制，双击代码中的reg文件运行即可。<br>
除此之外也修改了心跳包时长、双网卡限制、各种日志上报等等。

## 截图

![](https://cdn.jsdelivr.net/gh/mmmlllnnn/CvicseASM/cvicse.jpg)
## 声明
使用者请对自己行为负责，因此仓库产生的后果与作者无关。

## exe版见release
