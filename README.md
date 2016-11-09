==========
VKMSGStats
==========

About
=====

Simple python class that allows to get VK messages statistics messages from any user or dialogue.

**License**: GNU GPL version 3.

**Requirements**: Python 2 or 3 with requests and installed [vk_api](https://github.com/python273/vk_api)


Installation
============

* Install requests if you dont have this library: `pip install requests`
* Install [vk_api](https://github.com/python273/vk_api): `pip install vk_api`
* Import [VKMSGStats](./src/VKMSGStats/VKMSGStats.py)


Usage
=====

**VKMSGStats(login, password)**
    To create the object o the class

**getUserStats(userID)**
    For calculating statistics of messages in a conversation with one interlocutor

**getChatStats(filed)**
    For calculating statistics of messages in the group conversation

**printStats()**
    For beautiful output