##iOS深度学习----安装环境(安装six出错解决办法)

安装苹果的coremltools出现

`
pip install coremltools
`

`
OSError: [Errno 1] Operation not permitted: 
'/tmp/pip-eBLWSU-uninstall/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/six-1.4.1-py2.7.egg-info'
`

出现这个错误是Apple预安装的这个six库出于安全原因被设置为sudo也不可以执行操作，所以需要依赖于高版本的库就需要更新six，但是没有six的权限，所以就会报错。

解决方案：

`
sudo -H pip install awscli --upgrade --ignore-installed six
`

然后重新安装 coremltools

