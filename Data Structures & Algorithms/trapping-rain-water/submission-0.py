class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        leftMax = [0] * n
        rightMax = [0] * n

        for i in range(n):
            leftMax[i] = max(height[:i+1])

        for i in range(n):
            rightMax[i] = max(height[i:])

        water = 0
        for i in range(n):
            water += min(leftMax[i], rightMax[i]) - height[i]

        return water