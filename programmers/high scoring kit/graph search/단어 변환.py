
from collections import deque


def solution(begin, target, words):
    minToWord = { begin:0 } # minimum step to this word
    wordQ = deque([begin])  # queue of the word
    visited = set([begin])  # set of visited words; chose bc search is O(1)

    # perform bfs
    while wordQ :
        currWord = wordQ.popleft()

        for word in words :
            if word not in visited and canChange(currWord, word) :  # must be not visited and only have a single letter difference
                wordQ.append(word)
                visited.add(word)
                minToWord[word] = minToWord[currWord] + 1           # if not visited yet, in bfs the first to reach this word means it was the shortest distance

    
    return minToWord.get(target, 0)

def canChange(word, target) :
    return sum([ word[i] == target[i] for i in range(len(word))]) == len(word) - 1


assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 4
assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0