class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if not strs:
           return []

        my_dict = defaultdict(list)

        for s in strs:
            my_list = [0] * 26
            for c in s:
                my_list[ord(c) - ord('a')] += 1
            my_dict[tuple(my_list)].append(s)

        return list(my_dict.values())
        