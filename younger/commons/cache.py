#!/usr/bin/env python3
# -*- encoding=utf8 -*-

########################################################################
# Created time: 2024-08-27 18:03:44
# Author: Jason Young (杨郑鑫).
# E-Mail: AI.Jason.Young@outlook.com
# Last Modified by: Jason Young (杨郑鑫)
# Last Modified time: 2024-11-27 15:25:45
# Copyright (c) 2024 Yangs.AI
# 
# This source code is licensed under the Apache License 2.0 found in the
# LICENSE file in the root directory of this source tree.
########################################################################


import os
import pathlib

from younger.commons.constants import YoungerHandle


cache_root: pathlib.Path = pathlib.Path(os.getcwd()).joinpath(f'{YoungerHandle.MainName}/{YoungerHandle.LogicsName}')


def set_cache_root(dirpath: pathlib.Path) -> None:
    assert isinstance(dirpath, pathlib.Path)
    global cache_root
    cache_root = dirpath
    return


def get_cache_root() -> pathlib.Path:
    return cache_root
