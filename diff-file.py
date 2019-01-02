#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import sys


def cha(x, y):
    a = []
    b = []
    c = []
    with open(x, 'r') as f1:
        aa = f1.readlines()
        for i in aa:
            a.append(i.strip())

    with open(y, 'r') as f2:
        bb = f2.readlines()
        for i in bb:
            b.append(i.strip())

    for i in a:
        if i not in b:
            c.append(i)
    for i in b:
        if i not in a:
            c.append(i)
    for h in sorted(c):
        print h


def jiao(x, y):
    a = []
    b = []
    c = []
    with open(x, 'r') as f1:
        aa = f1.readlines()
        for i in aa:
            a.append(i.strip())

    with open(y, 'r') as f2:
        bb = f2.readlines()
        for i in bb:
            b.append(i.strip())

    for i in a:
        if i in b:
            c.append(i)
    for h in sorted(c):
        print h


def bin(x, y):
    a = []
    b = []
    c = []
    with open(x, 'r') as f1:
        aa = f1.readlines()
        for i in aa:
            a.append(i.strip())

    with open(y, 'r') as f2:
        bb = f2.readlines()
        for i in bb:
            b.append(i.strip())

    d = copy.deepcopy(b)

    for i in a:
        for h in b:
            if i != h:
                b.append(i)
                break
    for i in a:
        if i in d:
            c.append(i)

    e = copy.deepcopy(b)
    for x in c:
        if x in b:
            e.remove(x)
    for h in sorted(e):
        print h


method = sys.argv[1]

file1 = sys.argv[2]

file2 = sys.argv[3]

if method == "bin":
    bin(file1, file2)

elif method == "jiao":
    jiao(file1, file2)

elif method == "cha":
    cha(file1, file2)
