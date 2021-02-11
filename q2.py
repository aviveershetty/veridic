packageData = [["1",  "y", "700.0"], ["2",  "m",  "51.0"], ["3", "bw",  "45.0"], ["4",  "q", "150.0"], ["5", "bw",  "40.0"]]

def perToNumber(per): 
    switcher = { 
        "y": 1, 
        "m": 12, 
        "q": 4,
        "bw": 24 
    } 
    return switcher.get(per) 

import heapq
def compute(packageData):
    maxHeap = []
    for id, per, price in packageData:
        multiplier = perToNumber(per)
        priceAnnum = multiplier * float(price)
        # maxHeap.append(priceAnnum)
        # maxHeap.sort()
        heapq.heappush(maxHeap, (-1 * priceAnnum, id))
    print(maxHeap)
    
compute(packageData)