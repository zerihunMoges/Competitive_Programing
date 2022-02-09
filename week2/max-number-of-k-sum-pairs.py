operations = 0
        nums.sort(key = lambda x: k-x)

        j = -1
        i =0 
        while len(nums) + j >= i:
            if nums[i] + nums[j] == k and abs(j) != (len(nums) -i):
                operations += 1
            elif nums[i] + nums[j] < k:
                i-=1
            elif nums[i] + nums[j] > k:
                j+=1
            j-=1
            i+=1

        return operations
