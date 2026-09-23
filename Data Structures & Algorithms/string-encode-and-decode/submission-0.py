class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += str(len(s)) + "-"
        code += "E"
        for s in strs:
            code += s
        return code

    def decode(self, s: str) -> List[str]:
        decode_int = []
        length = ""
        is_word = False
        for i in range(len(s)):
            l = s[i]
            if l == "E":
                s = s[i + 1:]
                break
            elif l == "-":
                decode_int.append(int(length))
                length = ""
            else:
                length += l
        decode = []
        for length in decode_int:
            decode.append(s[:length])
            s = s[length:]
        return decode

