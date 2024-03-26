#!/usr/bin/env python3
""" script that reads stdin line by line and computes metrics"""


import sys


def print_stats(total_size, status_codes):
    """def for stats"""
    print("File size:", total_size)
    for code, count in sorted(status_codes.items()):
        print(code + ":", count)

def main():
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 9:
                status = parts[-2]
                file_size = parts[-1]
                if status in status_codes:
                    status_codes[status] += 1
                total_size += int(file_size)
                line_count += 1

            if line_count == 10:
                print_stats(total_size, status_codes)
                line_count = 0

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()

