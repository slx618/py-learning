
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    j = 0
    for i in range(0, len(nums) - 1):
        if nums[i] != nums[j]:
            nums[j] = nums[i]
            j += 1
            continue
    print(nums)

removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])