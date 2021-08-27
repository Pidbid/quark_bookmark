# quark_bookmark

将手机夸克浏览器书签提取，并生成一个通用的bookmark.html文件

## 使用教程

* 手机Root
* 复制手机文件 /data/data/com.quark.browser/databases/bookmark.db 至此文件夹下
* 打开终端运行

> python main.py [-path]  

* path 为可选值，如果不填写，则在主文件夹下寻找名为bookmark.db的文件  

## 其他

* 为什么不通过ADB获取文件？  
    - 这要分为两种情况，在手机无Root权限的情况下无论是通过ABD或者是其他方法是无法获取手机data分区下的文件的。在手机有Root权限的情况下，部分手机依然无法使用adb pull命令获取手机data分区下的文件，z综上并不推荐使用ADB获取文件。  
* 那应该怎么获得bookmark.db文件呢？  
    - 0，手机Root，手机不Root的话一切都白搭
    - 1，使用手机文件管理类软件，如ES浏览器等，将/data/data/com.quark.browser/databases/bookmark.db复制到手机可访问的内存中，再将其复制到电脑即可。  
    - 2，在Root的情况下链接USB使用ADB命令（虽不推荐，但是这种方法是可行的）。连接之后输入以下命令进行复制：
    > adb shell  
    > su #手机上点击允许shell获取最高权限  
    > cp /data/data/com.quark.browser/databases/bookmark.db /storage/emulated/0  

    - 然后将手机存储中的bookmark.db复制到电脑进行操作  

## 关于

[Pidbid blog](https://www.wicos.me)  
Email: wicos#wicos.cn
