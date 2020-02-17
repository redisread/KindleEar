#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

from base import BaseFeedBook
import re, urllib
from lib.urlopener import URLOpener
from bs4 import BeautifulSoup
import json
from config import SHARE_FUCK_GFW_SRV

__author__ = 'victorhong'

def getBook():
    return MyWechat

class MyWechat(BaseFeedBook):
    title                 = u'微信公众号A'
    description           = u'微信订阅内容。。。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_xueqiu.gif"
    coverfile             = "cv_xueqiu.jpg"
    oldest_article        = 3   #距离几天的文章
    fulltext_by_readability = False # 取消自动处理网页
    fulltext_by_instapaper = True
    feeds = [ (u'英语', 'https://rsshub.app/wechat/ershicimi/23'),
              (u'程序员', 'https://rsshub.app/wechat/ershicimi/59'),]