# 最快解
# 思路清晰，第一遍遍历，给栈添加新元素，每个元素都会进栈j，剩余在栈中的元素就是必须要在第二轮找到的，甚至找不到的
# 第二遍遍历，只更新栈中的元素的值，不再添加新元素到栈中，此时剩下的元素就是绝对找不到的

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
        
        return res
      
 # 我的解不太好写

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = [(nums[0], 0)]
        tail = 1 % len(nums)
        poped = 0
        while True:
            while stack and (tail != stack[0][1] or nums[tail] != stack[-1][0]) and stack[-1][0] < nums[tail]:
                val, pos = stack.pop()
                res[pos] = nums[tail]
                poped += 1
                if poped == len(nums):
                    return res
            if stack and tail == stack[0][-1]:
                return res
            if res[tail] == -1:
                stack.append((nums[tail], tail))
            tail = (tail + 1) % len(nums)
            
