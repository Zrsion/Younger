#!/usr/bin/env python3
# -*- encoding=utf8 -*-

########################################################################
# Created time: 2025-01-06 19:27:28
# Author: Jason Young (杨郑鑫).
# E-Mail: AI.Jason.Young@outlook.com
# Last Modified by: Jason Young (杨郑鑫)
# Last Modified time: 2025-01-06 19:50:37
# Copyright (c) 2025 Yangs.AI
# 
# This source code is licensed under the Apache License 2.0 found in the
# LICENSE file in the root directory of this source tree.
########################################################################


import pathlib

from younger.commons.cache import CachedGenerator


itr = CachedGenerator(pathlib.Path('./Test/itr'), range(100000), 1000)


print(len(itr))
print(all([index == i for index, i in enumerate(itr)]))

# for index, i in enumerate(itr):
#     print(index, i)