#!/usr/bin/python
# -*- coding: utf-8 -*-
#filename:utils.py

import os
import logging
import json
import random


def find_config():
    config_path = 'config.json'
    if os.path.exists(config_path):
        return config_path
    config_path = os.path.join(os.path.dirname(__file__), '../', 'config.json')
    if os.path.exists(config_path):
        return config_path
    return None

def check_config(config):
    if config.get('server', '') in ['127.0.0.1', 'localhost']:
        logging.warn('Server is set to "%s", maybe it\'s not correct' % config['server'])
        logging.warn('Notice server will listen at %s:%s' % (config['server'], config['server_port']))
    if (config.get('method', '') or '').lower() == 'rc4':
        logging.warn('RC4 is not safe; please use a safer cipher, like AES-256-CFB')



if __name__ == "__main__":
    config_path = find_config()
    if config_path:
        logging.info('Loading Config From %s' % config_path)
        with open(config_path, 'rb') as f:
            config = json.load(f)

            #print config
            if config.has_key("server_password") == True:
                number =  len(config["server_password"]) #判断有server_password的长度、也就是有几条服务器/端口/密码

                #通过random取一个随机数、来随机分配用哪一条服务器端口密码
                i = random.randint(0,number)
                #然后写入到一个字典中
                server_dict = {}
                server_dict[u"server"]= config["server_password"][i][0]
                server_dict[u"server_port"] = config["server_password"][i][1]
                server_dict[u"password"] = config["server_password"][i][2]
                server_dict[u"local_port"] = config["local_port"]
                server_dict[u"method"] = config["method"]
                server_dict[u"timeout"] = config["timeout"]
                print server_dict

                # for i in range (0,number):
                #     #print i
                #     server_dict = {}
                #     server_dict["server"]= config["server_password"][i][0]
                #     server_dict["server_port"] = config["server_password"][i][1]
                #     server_dict["password"] = config["server_password"][i][2]
                #     server_dict["local_port"] = config["local_port"]
                #     server_dict["method"] = config["method"]
                #     server_dict["timeout"] = config["timeout"]
                #     print server_dict
            else:
                print config


        # for i in config['server_password']:
        #     print i
        
