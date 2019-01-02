#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : check-docs.py
# Date  : 2018-12-26
import os
import re


# 获取符合的文件列表
def dir_list(path, match='', nomatch='ssssssss'):
    allfiles_list = []
    allfiles = os.listdir(path)
    for f in allfiles:
        # if match.find(f):
        if re.search(match, f):
            if re.search(nomatch, f):
                pass
            else:
                filepath = os.path.join(path, f)
                allfiles_list.append(filepath)
    return allfiles_list
# all_list = dir_list("/Users/jh/git/deployment/xiaomi-config/conf/hdfs/", "prc", "xiaomi")


def namenode_list(*args, **kwargs):
    for fil in dir_list(*args, **kwargs):
        with open(fil, 'r') as f:
            fil_con = f.readlines()
            reads = ''
            for read_lines in fil_con:
                reads = reads + read_lines.strip()

            # print reads
            result_list = re.findall('namenode(.*?)execute', reads)
            # print result_list
            for results in result_list:
                # print results
                result = re.sub(':ports:base:.*hosts:- |federation_count:.*|/.*? |-? ', ' ', results)
                namenode = result.split()
                print namenode


a = namenode_list("/Users/jh/git/deployment/xiaomi-config/conf/hdfs/", "prc", "xiaomi")
print a





