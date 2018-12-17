# Gary tracks his hikes meticulously. During his last hike he took n steps.
# For every step he took, he noted if it was an uphill, U,
# or a downhill, D step.
# Gary's hikes start and end at sea level and each step up or down represents
# a 1 unit change in altitude.
# A mountain is a sequence of consecutive steps above sea level,
# starting with a step up from sea level and end with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level,
# starting with a step down from sea level and end with a step up to sea level.


def counting_valleys(num, seq):
    up = down = valley = 0
    trek = []
    for item in list(seq):
        if item == "D":
            down += 1
            trek.append(item)
        else:
            up += 1
            trek.append(item)
        if down == up and trek[0] == "Down":
            valley += 1
            down = up = 0
            trek = []
        elif down == up and trek[0] == "U":
            down = up = 0
            trek = []
    print("Valley: {}".format(valley))


if __name__ == '__main__':
    counting_valleys(8, "UDDDUDUU")
