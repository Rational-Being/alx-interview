#!/usr/bin/python3
"""

"""

import sys

statcd = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

count = 0
final = 0

try:
    for _ in sys.stdin:
        new = _.split(" ")
        if len(new) > 4:
            stats = new[-2]
            size = int(new[-1])
        
        if stats in statcd.keys():
            statcd[stats] += 1
        
        fin += size
        count += 1

    if count == 10:
        count = 0
        print (f"File size: {fin}")

        for k, v in sorted(statcd.items()):
            if v != 0:
                print(f"{key}: {value}")
except Exception as e:
    pass

finally:
    print(f"File size: {fin}")
    for k, v in sorted(statcd.items()):
        if value != 0:
            print(f"{key}: {value}")