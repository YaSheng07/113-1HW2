def missingNumber(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2  # 計算 0 到 n 的總和
    actual_sum = sum(nums)  # 計算數組的總和
    return total_sum - actual_sum  # 找出缺失的數字

# 測試範例
print(missingNumber([3, 0, 1]))  # 輸出: 2
print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 輸出: