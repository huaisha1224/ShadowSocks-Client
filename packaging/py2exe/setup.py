from distutils.core import setup
# NOTICE!!
# This setup.py is written for py2exe
# Don't make a python package using this file!

try:
    import py2exe
except ImportError:
    pass

setup(name='ShadowSocks-Client',
        version='0.5',
        description='The ShadowSocks client is a support multiple server port and password',
        author='huaisha1224',
        author_email='sam.hxq@gmail.com',
        url='https://github.com/huaisha1224/ShadowSocks-Client',
        options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
        windows = [{"script":"ShadowSocks_local.py", "dest_base": "shadowsocks_local",}],
        zipfile = None)
