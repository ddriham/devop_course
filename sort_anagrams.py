!#/usr/bin/env python3
# the input is list of anagrams the out put will be list for each anagram,
# sorted alphabet.
# extreamly hard exercise!!!! (more then 10 hours :) )


list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']

def sort_anagrams(words):
    anagram_groups = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]

    result = []
    for word in words:
        sorted_word = ''.join(sorted(word))
        group = anagram_groups.get(sorted_word)
        if group and word == group[0]:
            result.append(group)

    def group_index(group):
        return words.index(group[0])

    result.sort(key=group_index)
    return result

print (sort_anagrams(list_of_words))
