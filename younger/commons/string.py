#!/usr/bin/env python3
# -*- encoding=utf8 -*-

########################################################################
# Created time: 2024-12-27 16:41:20
# Author: Jason Young (杨郑鑫).
# E-Mail: AI.Jason.Young@outlook.com
# Last Modified by: Jason Young (杨郑鑫)
# Last Modified time: 2024-12-27 16:46:45
# Copyright (c) 2024 Yangs.AI
# 
# This source code is licensed under the Apache License 2.0 found in the
# LICENSE file in the root directory of this source tree.
########################################################################


import re


README_TABLE_Pattern = r'(\|?(?:[^\r\n\|]*\|)+(?:[^\r\n]*\|?))\r?\n(\|?(?:(?:\s*:?-+:?\s*)\|)+(?:(?:\s*:?-+:?\s*)\|?))\r?\n((?:\|?(?:(?:[^\r\n\|]*)\|)+(?:(?:(?:[^\r\n\|]*)\|?))\r?\n)+)'
README_DIGIT_Pattern = r'(?:[+-]?(?:(?:\d+(?:\.\d+)?)|(?:\.\d+))%?)\s+|\s+(?:[+-]?(?:(?:\d+(?:\.\d+)?)|(?:\.\d+))%?)'
README_DATE_Pattern = r'(?:(?:\d{4})(?:-|\/)(?:\d{1,2})(?:-|\/)\d{1,2})|(?:(?:\d{1,2})(?:-|\/)(?:\d{1,2})(?:-|\/)\d{4})|(?:(?:\d{4})(?:-|\/)(?:\d{1,2}))|(?:(?:\d{1,2})(?:-|\/)(?:\d{4}))|(?:\d{1,2}(?:-|\/)\d{1,2})'
README_DATETIME_Pattern = r'\b\d{4}-(?!(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b)\d{1,2}-(?!([12]\d|3[01])\b)\d{1,2} \d{1,2}:\d{2}(:\d{2})?\b|\b\d{1,2}:\d{2}(:\d{2})?(?:\s*[apAP]\.?[mM]\.?)?\b|\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b'


def extract_possible_tables_from_readme_string(readme: str) -> list[dict[str, list[str]]]:

    def extract_cells(row: str) -> list[str]:
        cell_str = row.strip()
        cell_str = cell_str[ 1:  ] if len(cell_str) and cell_str[ 0] == '|' else cell_str
        cell_str = cell_str[  :-1] if len(cell_str) and cell_str[-1] == '|' else cell_str
        cells = [cell.strip() for cell in cell_str.split('|')]
        return cells

    readme = readme.strip() + '\n'
    possible_tables = list()
    for match_result in re.finditer(README_TABLE_Pattern, readme, re.MULTILINE):
        headers = match_result.group(1)
        headers = extract_cells(headers)
        rows = list()
        for row in match_result.group(3).strip().split('\n'):
            rows.append(extract_cells(row))
        possible_tables.append(
            dict(
                headers=headers,
                rows=rows
            )
        )

    return possible_tables


def extract_possible_digits_from_readme_string(readme: str) -> list[str]:

    def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
        intervals = sorted(intervals)
        new_intervals = list()
        start, end = (-1, -1)
        for interval in intervals:
            if end < interval[0]:
                new_interval = (start, end)
                new_intervals.append(new_interval)
                start, end = interval

            else:
                if end < interval[1]:
                    end = interval[1]

        new_intervals.append((start, end))
        return new_intervals[1:]

    intervals = list()
    for match_result in re.finditer(README_DIGIT_Pattern, readme, re.MULTILINE):
        start = match_result.start() - 32
        end = match_result.end() + 32
        intervals.append((start, end))

    intervals = merge_intervals(intervals)
    possible_digit = list()
    for start, end in intervals:
        digit_context = ' '.join(readme[start:end].split())
        possible_digit.append(digit_context)

    return possible_digit


def remove_yaml_front_matter_from_readme_string(readme: str) -> str:
    readme_lines = readme.split('\n')
    split_pattern = '---'
    if len(readme_lines) <= 2:
        return '\n'.join(readme_lines)
    if readme_lines[0].strip() == split_pattern:
        for index, readme_line in enumerate(readme_lines[1:], start=1):
            if readme_line.strip() == split_pattern:
                break
        return '\n'.join(readme_lines[index+1:])
    return '\n'.join(readme_lines)
