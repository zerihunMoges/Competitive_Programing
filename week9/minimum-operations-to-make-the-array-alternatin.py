class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odd = defaultdict(int)
        even =  defaultdict(int)
        activee = set()
        activee
        print(len(nums))
        maxxd = [[0,None],[0,None]]
        maxxe = [[0,None],[0,None]]
        for i in range(len(nums)):
            if i%2 == 0:
                even[nums[i]] += 1
                if even[nums[i]] > maxxe[0][0]:
                    if maxxe[0][1] != nums[i]:
                        maxxe[1] =maxxe[0]
                    maxxe[0] = [even[nums[i]], nums[i]]
                
                elif even[nums[i]] > maxxe[1][0]: 
                    maxxe[1] = [even[nums[i]], nums[i]]
                         
            else:
                odd[nums[i]] += 1
                if odd[nums[i]] > maxxd[0][0]:
                    if maxxd[0][1] != nums[i]:
                        maxxd[1] =maxxd[0]
                    
                    maxxd[0] = [odd[nums[i]], nums[i]]
                
                elif odd[nums[i]] > maxxd[1][0]: 
                    maxxd[1] = [odd[nums[i]], nums[i]]
    
        if maxxe[0][1] == maxxd[0][1]:
            return min((len(nums)//2 - maxxe[0][0] +(1 if len(nums)%2 ==1 else 0) + 
                        len(nums)//2-maxxd[1][0]), (len(nums)//2 - maxxe[1][0] +
                        (1 if len(nums)%2 ==1 else 0) + len(nums)//2-maxxd[0][0]) )
        else:
            return (len(nums)//2 - maxxe[0][0] + (1 if len(nums)%2 == 1 else 0) + 
                        len(nums)//2-maxxd[0][0])
