#!/usr/bin/python3
"""
log parsing
"""import sys
from collections import defaultdict

total_size = 0
status_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) != 7:
            continue
        ip_address, _, _, path, status_code, file_size, _ = parts
        if path != '/projects/260':
            continue
        try:
            file_size = int(file_size)
            status_code = int(status_code)
        except ValueError:
            continue
        total_size += file_size
        status_counts[status_code] += 1
        if line_count % 10 == 0:
            print(f'Total file size: {total_size}')
            for code in sorted(status_counts):
                print(f'{code}: {status_counts[code]}')
            print()
except KeyboardInterrupt:
    print('Interrupted')
    print(f'Total file size: {total_size}')
    for code in sorted(status_counts):
        print(f'{code}: {status_counts[code]}')