class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strs:
            rep = ''.join(sorted(word))
            group[rep].append(word)
        return [g for g in group.values()]