class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ""

        encoded_string = []

        for s in strs:
            temp = ""
            temp += str(len(s)) + "#" + s
            encoded_string.append(temp)

        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:

        if not s:
            return []

        res = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            i = j + 1
            j = i + length

            res.append(s[i:j])

            i = j

        return res




