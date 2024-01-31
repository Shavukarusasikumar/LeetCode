class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temp[i] > temp[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index

            stack.append(i)

        return result