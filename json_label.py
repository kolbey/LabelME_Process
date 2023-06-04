#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import os.path as osp

path = "./jsons/"
files = os.listdir(path)

for i in files:
    full_name = osp.join(path, i)
    if full_name.endswith(".json"):
        os.system("D:/Anaconda3/envs/tensorflow/Scripts/labelme_json_to_dataset.exe %s" % full_name)

print ("转换完成.")
