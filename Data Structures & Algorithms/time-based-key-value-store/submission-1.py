class TimeMap:

    def __init__(self):
        self.my_dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.my_dict:
            self.my_dict[key] = []
        self.my_dict[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        res = ""

        if key not in self.my_dict:
            return ""

        values = self.my_dict.get(key, [])

        l, r = 0, len(values) - 1

        while l <= r:

            mid = (l + r) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res

        
