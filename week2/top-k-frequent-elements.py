class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arry = [0]
        frequency_list = []
        minm = 0
        maxm = nums[0]
        minFrequency = 0
        
        for i in range(len(nums)):
            if nums[i] > maxm:
                maxm = nums[i]
            elif nums[i] < minm:
                minm = nums[i]

        arry = [0]*(maxm + 1 - minm)
        
        for i in range(len(nums)):
            arry[nums[i]] += 1
            
        for i in range(len(arry)):
            if len(frequency_list) < k and arry[i] != 0:
                j = i-len(arry) if i > maxm else i
                frequency_list.append(j)
            elif arry[i] != 0 :
                if minFrequency == 0:
                    for j in range(len(frequency_list)):
                        minFrequency = j if arry[frequency_list[j]] < arry[frequency_list[minFrequency]] else minFrequency
                if arry[i] > arry[frequency_list[minFrequency]]:
                    j = i-len(arry) if i > maxm else i
                    frequency_list[minFrequency] = j
                    minFrequency = 0
                    
        return frequency_list
