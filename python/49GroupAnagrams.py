# from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram_groups = defaultdict(list)
        anagram_groups = {}

        for elem in strs:
            key = ''.join(sorted(elem))

            anagram_groups.setdefault(key, [])
            anagram_groups[key].append(elem)

        groups = list(anagram_groups.values())
        return groups
