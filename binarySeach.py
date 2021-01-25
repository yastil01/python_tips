        def binarySearch(target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2
                if target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            return left
            
      1. if the array has duplicates, this will return 1st occurance of the target
         [9,9,9,9] -> ans will be 0
      2. if target > nums[-1], it will return last index
      3. if target < nums[0], it will return 0
      4. if you find a match, left==right==mid
      5. if you don't find a match, it will return insert location
