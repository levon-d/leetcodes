class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [arr[0]]
        for i in range(1, len(arr)):
            prefix.append(prefix[-1] ^ arr[i])

        result = []
        for query in queries:
            if query[0] == 0:
                result.append(prefix[query[1]])
            else:
                result.append(prefix[query[1]] ^ prefix[query[0] - 1])

        return result

