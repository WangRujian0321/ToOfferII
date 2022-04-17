class Solution:
    def groupAnagrams(self, strs):
        mp = {}
        for st in strs:
            key = "".join(sorted(st))
            if key not in mp:
                mp[key] = [st]
            else:
                mp[key].append(st)
        return list(mp.values())