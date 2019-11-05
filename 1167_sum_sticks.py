from datetime import datetime

class Sticks:
    def connectSticks(self, sticks):
        sum = 0
        while(len(sticks) > 1):
            sticks.sort()
            new_stick = sticks[0] + sticks[1]
            sum += new_stick
            sticks.pop(0)
            sticks.pop(0)
            sticks.append(new_stick)
        return sum
    def connectSticks2(self, sticks):
        sum = 0
        while(len(sticks) > 1):
            new_stick = 0
            first = min(sticks)
            new_stick += first
            sticks.remove(first)
            second = min(sticks)
            new_stick += second
            sticks.remove(second)
            sum += new_stick
            sticks.append(new_stick)
        return sum
    
if __name__ == "__main__":
    obj = Sticks()

    start1 = datetime.now()
    output1 = obj.connectSticks([1,8,3,5])
    time1 = datetime.now() - start1

    start2 = datetime.now()
    output2 = obj.connectSticks2([1,8,3,5])
    time2 = datetime.now() - start2
    
    print(output1, time1)
    print(output2, time2)
