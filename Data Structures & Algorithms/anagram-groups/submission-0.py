class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            rep = ''.join(sorted(word))
            if group.get(rep, None) is None:
                group[rep] = [word]
            else:
                group[rep].append(word)
        return [g for g in group.values()]