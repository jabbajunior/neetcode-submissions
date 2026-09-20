class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Return early checks
            if strs is None:
                return [[""]]
            elif len(strs) == 1:
                return [[strs[0]]]

            # Conceptually 26 character array represents count of characters
            # 0 - a, 1 - b, etc.

            word_frequency = {}
            result = []

            group_index = 0
            for word in strs:

                # Generating frequency array on character count
                frequency = [0 for _ in range(26)]

                for char in word:
                    frequency[ord(char) - ord('a')] += 1


                frequency = tuple(frequency)

                # If new anagram, add it to new group
                if frequency not in word_frequency:
                    result.append([word])
                    word_frequency[tuple(frequency)] = group_index
                    group_index += 1

                # If existing anagram, append to existing group
                else:
                    result[word_frequency[frequency]].append(word)

            return result

           