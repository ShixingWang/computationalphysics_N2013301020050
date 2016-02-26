# 在Fedora 23 系统下安装Python 2.7.11
*for genuine novices about Linux and Python* <br>
*写这种教程的人是不是很傻* *_(:з」∠)_*
## 下载Python 2.7.11
没有用命令行那么高端的办法，直接在浏览器中输入下面的网址:
[https://www.python.org/downloads/release/python-2711/](https://www.python.org/downloads/release/python-2711/)
点击前两个链接之一（我只试过第二个），等待下载完成，默认路径应该是/home/$用户名/download
## 解压缩及安装
- 打开terminal（方法1：鼠标指向左上角“活动”，在屏幕中间搜索栏中输入'terminal'；方法2：鼠标指向左上角“活动”，点击左边栏最下“显示所有程序”-“工具”-“终端”）
- 依次输入
`cd /home/$用户名/download`<br>
`ls -al`<br>
这是为了查看压缩包的文件名，我的是“Python-2.7.11.gtz”
- 输入`tar –zxvf Python-2.7.11.gtz`，等待命令行 <del> _抽疯 </del> 反应
- 依次输入下面的命令进行安装： <br>
`./configure` <br>
`make` <br>
`make install`

注意“/configure“前面有英文句号，否则报错。
## "no acceptable C compiler found in $PATH"错误
在上一步make环节可能会卡住，终端提示"no acceptable C compiler found in $PATH"，出现这一错误是因为电脑未安装C编译器，解决方法如下：

- 输入`yum install gcc`，若有确认环节输入`y`，直到提示GCC成功安装
- 重复刚才卡住之前及其后续命令
- 如出现权限问题报错输入`su`，根据提示输入管理员密码，重复之前报错的步骤

## 安装成功
在终端输入`python`，若出现以下字样
>Python 2.7.11 (default, Feb 25 2016, 15:39:54) <br>
[GCC 5.3.1 20151207 (Red Hat 5.3.1-2)] on linux2 <br>
Type "help", "copyright", "credits" or "license" for more information.

则说明安装成功






## Reference
1. “如何在linux系统中安装python?”-百度知道 
	[http://zhidao.baidu.com/link?url=f8BF3Cah5RBhKd-EqoQsUbe-3MMRbyVFq2My39o5Dx6G5K8XfdbOTee6BXNtOpBmGyLuwUXvyQo6rF_MjoliFK](http://zhidao.baidu.com/link?url=f8BF3Cah5RBhKd-EqoQsUbe-3MMRbyVFq2My39o5Dx6G5K8XfdbOTee6BXNtOpBmGyLuwUXvyQo6rF_MjoliFK)
2. "no acceptable C compiler found in $PATH'解决手记'" -上学吧 
  [http://www.shangxueba.com/jingyan/121655.html](http://www.shangxueba.com/jingyan/121655.html)
