class TimeMap:
    def __init__(self):
        #nested dictionary 
        self.storage={}
        #{key1:{time1:value1
        #       time2:value2} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key]={} 
            self.storage[key]={timestamp:value}
        else:
            self.storage[key][timestamp]=value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        t_v=self.storage[key]

        currMax=0
        for t,v in t_v.items():
            if t<=timestamp:
                currMax=max(currMax,t)
        if currMax in t_v:
            return t_v[currMax]
        else:
            return ""
        