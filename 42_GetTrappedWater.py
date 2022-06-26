from audioop import maxpp


def getTrappedRainwater(height):
    maxR = 0
    maxL = 0
    total = 0
    for index, elem in enumerate(height):
        if height[index:] == []:
            maxR = 0
        else:
            maxR = max(height[index:])
        if height[:index] == []:
            maxL = 0
        else:
            maxL = max(height[:index])
        currentWater = min(maxL, maxR) - elem
        if currentWater < 0: currentWater=0
        total += currentWater
    return total

# bar = [0,1,0,2,1,0,3,1,0,1,2]
# print(getTrappedRainwater(height=bar))

# better way

def getTrappedRainwater2(height):
    total = 0
    pl = 0
    pr = len(height)-1
    maxR = height[pr]
    maxL = height[pl]
    while pl < pr:
        if height[pl] > maxL:
            maxL = height[pl]
        if height[pr] > maxR:
            maxR = height[pr] 
        if maxL <= maxR:
            currentwater=maxL - height[pl]
            if currentwater < 0 : currentwater=0
            pl+=1
        else:
            currentwater=maxR - height[pr]
            if currentwater < 0 : currentwater=0
            pr-=1
        total += currentwater
    return total

bar = [0,1,0,2,1,0,3,1,0,1,2]
print(getTrappedRainwater2(height=bar))