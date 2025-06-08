def partition_equal_subset_aux(nums, target, i):
    if i == len(nums):
        return False

    if target == 0:
        return True

    ok = False

    if nums[i] > target:
        ok = ok or partition_equal_subset_aux(nums, target - nums[i], i + 1)

    pass


def partition_equal_subset(nums):
    total = sum(nums)

    if total % 2 != 0:
        return False

    target = total // 2

    return partition_equal_subset_aux(nums, target, 0)
