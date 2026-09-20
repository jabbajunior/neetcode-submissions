class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
           # Return early checks
        if strs is None:
            return [[""]]
        elif len(strs) == 1:
            return [[strs[0]]]

        '''Sort each string alhpabetically and then use that instead of a frequency dict'''

        sorted_strs = [''.join(sorted(s)) for s in strs]
        index_dict = {}
        result = []

        i = 0
        for signature in sorted_strs:
            if signature not in index_dict:
                index_dict[signature] = len(result)
                result.append([strs[i]])
            else:
                result[index_dict[signature]].append(strs[i])
                pass

            i += 1

        return result