ShadowSocks-Client
==================

shadowsocks 是一个轻量级隧道代理，用来穿过防火墙。

第一个版本由clowwindy用Python编写、后续有很多其他的移植版本。[见这里](https://github.com/clowwindy/shadowsocks)

ShadowSocks Server端可以绑定多个端口、以减少一个端口流量太大带来的风险。但是ShadowSocks Client没有能够支持多服务器 

多端口的版本、而我又有这个需求、所以就在[ShadowSocks](https://github.com/clowwindy/shadowsocks)的基础上修改了一个ShadowSocks-Client版本。

使用
----

首先检查是Pytohn版本是否是2.6 or 2.7
 
    $ python --version
    Python 2.7.5
    
下载ShadowSocks-Client



在`ShadowSocks-Client`目录下建立一个`config.json`文件、内容如下：

    {
        "server":"my_server_ip",
        "server_port":10086,
        "local_port":1080,
        "password":"barfoo!",
        "timeout":600,
        "method":"table"
    }
    
    
多服务器IP、端口和密码的`config.json`格式如下：



    {   
        “server_password”:
        [
        ["my_server_ip1", 10086, "123456789cde"],
        ["my_server_ip2", 10087, "369852147zxc"],
        ["my_server_ip3", 10088, "qazwsxedcrfv"],
        ["my_server_ip4", 10089, "barfoo!abcde"]
        ]
        "local_port":1080,
        "timeout":600,
        "method":"aes-256-cfb"
    }

在`cmd`下切换到`config.json`目录、然后运行`ShadowSocks_local.py`

      ShadowSocks_local.py
      

然后把浏览器代理修改为如下即可：

        协议：socks5
        地址：127.0.0.1
        端口：1080、也就是刚才填写的local_port

建议`Firefox`使用`AutoProxy`、`Chrome`使用`Proxy SwitchSharp`.



