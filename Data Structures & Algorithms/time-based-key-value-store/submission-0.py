class TimeMap:

    def __init__(self):
        self.key_store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.key_store.get(key, [])
        # values will be sorted
        # use binary search to filter the value

        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1


        return res

        
