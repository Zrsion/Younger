#!/usr/bin/env python3
# -*- encoding=utf8 -*-

########################################################################
# Created time: 2024-08-27 18:03:44
# Author: Jason Young (杨郑鑫).
# E-Mail: AI.Jason.Young@outlook.com
# Last Modified by: Jason Young (杨郑鑫)
# Last Modified time: 2025-01-05 20:59:42
# Copyright (c) 2024 Yangs.AI
# 
# This source code is licensed under the Apache License 2.0 found in the
# LICENSE file in the root directory of this source tree.
########################################################################


import os
import pathlib

from younger.commons.constants import YoungerHandle


CACHE_ROOT: pathlib.Path = pathlib.Path.home().joinpath(f'.cache/{YoungerHandle.MainName}')


def set_cache_root(dirpath: pathlib.Path) -> None:
    assert isinstance(dirpath, pathlib.Path)
    global CACHE_ROOT
    CACHE_ROOT = dirpath
    return


def get_cache_root() -> pathlib.Path:
    return CACHE_ROOT
