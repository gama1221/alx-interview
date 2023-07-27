#!/usr/bin/python3
<<<<<<< HEAD
"""
log parsing
"""

import sys
import re


def output(log: dict) -> None:
    """
    helper function to display stats
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    regex = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')  # nopep8

    line_count = 0
    log = {}
    log["file_size"] = 0
    log["code_frequency"] = {
        str(code): 0 for code in [
            200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if (match):
                line_count += 1
                code = match.group(1)
                file_size = int(match.group(2))

                # File size
                log["file_size"] += file_size

                # status code
                if (code.isdecimal()):
                    log["code_frequency"][code] += 1

                if (line_count % 10 == 0):
                    output(log)
    finally:
        output(log)
=======
"""reads stdin line by line and computes metrics"""

import sys

total_size = 0
counter = 0
codes = ['200', '301', '400', '401', '403', '404', '405', '500']
dict_counter = {'200': 0, '301': 0,
                '400': 0, '401': 0,
                '403': 0, '404': 0,
                '405': 0, '500': 0}

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 2:
            code = line_list[-2]
            size = line_list[-1]
            if code in codes:
                dict_counter[code] += 1
            total_size += int(size)
            counter += 1

        if counter == 10:
            print("File size: {:d}".format(total_size))
            for k, v in sorted(dict_counter.items()):
                if v != 0:
                    print("{}: {:d}".format(k, v))
            counter = 0

except Exception:
    pass
finally:
    print("File size: {}".format(total_size))
    for k, v in sorted(dict_counter.items()):
        if v != 0:
            print("{}: {}".format(k, v))
>>>>>>> 36931085e09056bd6df40d053aeb24c309ed5c32
