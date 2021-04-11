import time

def get_anagrams(word):
    result = 0
    anagram_dict = dict()

    # get all possible substrings
    for i in range(1, len(word)):
        for j in range(0, len(word) - i + 1):
            tmp = "".join(sorted(word[j:j+i]))   # sorting each word, would make it easier to compare with the anagram word, as both will be same after sorting
            anagram_dict[tmp] = anagram_dict.get(tmp, 0) + 1
            
    summary = {k:v for k,v in anagram_dict.items() if v>1}
    print(f"summary: {summary}")

    for v in summary.values():
        result += sum(range(v))
    # result = len(summary)
    return result

if __name__ == "__main__":

    word = "abba"

    start = time.time()
    result = get_anagrams(word)
    end = time.time()

    print(f"No of Anagrams possible: {result}")
    print(f"Total time taken: {end-start}")