def groupAnagrams(words):
    anagrams = []
    if not words:
        return anagrams
    A = [''.join(sorted(word)) for word in words]
    dict = {}
    for i, e in enumerate(A):
        dict.setdefault(e, []).append(i)

    for index in dict.values():
        collection = tuple(words[i] for i in index)
        if len(collection) > 1:
            anagrams.append(collection)
 
    return anagrams
if __name__ == '__main__':
    
    words = ['CARS', 'REPAID', 'DUES', 'NOSE', 'SIGNED', 'LANE', 'PAIRED', 'ARCS',
             'GRAB', 'USED', 'ONES', 'BRAG', 'SUED', 'LEAN', 'helo','abcd','oleh']
 
    anagrams = groupAnagrams(words)
    for anagram in anagrams:
        print(anagram)
