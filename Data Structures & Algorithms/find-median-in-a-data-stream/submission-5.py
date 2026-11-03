#Idea of keeping keaps approximately equal

class MedianFinder:

    def __init__(self):
        self.smallH = []
        self.largeH = []

        

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.smallH, num)


        if len(self.smallH) == len(self.largeH) or len(self.smallH) - len(self.largeH) == 1:
            if self.smallH and self.largeH and self.smallH[0] > self.largeH[0]:
                toL = heapq.heappop_max(self.smallH)
                toS = heapq.heappop(self.largeH)
                heapq.heappush_max(self.smallH, toS)
                heapq.heappush(self.largeH, toL)
        if len(self.smallH) - len(self.largeH) > 1:
            heapq.heappush(self.largeH, heapq.heappop_max(self.smallH))
        

    def findMedian(self) -> float:
        if len(self.smallH) == len(self.largeH):
            first = self.smallH[0]
            second = self.largeH[0]
            return (first+second)/2
        elif len(self.smallH) > len(self.largeH):
            return self.smallH[0]
        else:
            return self.largeH[0]

        
        