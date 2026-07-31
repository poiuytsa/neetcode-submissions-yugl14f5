class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res=[]

        #empty intervals
        if not intervals:
            return [newInterval]

        #at beginning
        if newInterval[1]<intervals[0][0]:
            return [newInterval]+intervals

        #at ending
        if newInterval[0]>intervals[-1][1]:
            return intervals+[newInterval]

        for i in range(len(intervals)):

            #in b/w 2 intervals
            if (i+1<len(intervals) and intervals[i][1]<newInterval[0]
            and newInterval[1]<intervals[i+1][0]):
                res.append(intervals[i])
                res.append(newInterval)
                res.extend(intervals[i+1:])
                return res

            #overlap
            if newInterval[0]<=intervals[i][1] and newInterval[1]>=intervals[i][0]:
                start=min(newInterval[0],intervals[i][0])
                end=max(newInterval[1],intervals[i][1])

                #check if it spans multiple intervals
                j=i+1
                while j<len(intervals) and intervals[j][0]<=end:
                    end=max(end,intervals[j][1])
                    j+=1

                res.append([start,end])
                res.extend(intervals[j:])
                return res

            res.append(intervals[i])

        return res