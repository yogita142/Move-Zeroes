def moveZeroes(nums):
    count = nums.count(0)  # Count the number of zeros in the list
    nums[:] = [num for num in nums if num != 0]  # Remove all zeros from the list
    nums.extend([0] * count)  # Append the zeros at the end
    return nums
  
nums1 = [0, 1, 0, 3, 12]
print(moveZeroes(nums1))  # Output: [1, 3, 12, 0, 0]

nums2 = [0]
print(moveZeroes(nums2))  # Output: [0]
