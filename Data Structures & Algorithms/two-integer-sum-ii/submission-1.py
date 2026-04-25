class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range (len(numbers)):
        #     for j in range (i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1,j+1]
        # return []


         left, right = 0, len(numbers) - 1  
        # Two pointers: start and end
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  
                # Return 1-based indices
            
            elif current_sum < target:
                left += 1  
                # Need bigger sum → move left forward
            
            else:
                right -= 1  
                # Need smaller sum → move right backward
