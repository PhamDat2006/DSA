#Big-O notation: cách mô tả thời gian chạy (hoặc bộ nhớ) của thuật toán khi input rất lớn.
"""
O(1): hằng số (cực nhanh, không phụ thuộc input).
O(log n): logarit (tìm kiếm nhị phân). # n / (2^k) = 1  ⟹  2^k = n  ⟹  k = log₂(n)
O(n): tuyến tính (duyệt hết mảng).
O(n log n): hiệu quả (Merge Sort, Quick Sort).
O(n²): chậm dần (dùng 2 vòng lặp lồng nhau).
O(2ⁿ): rất chậm (Backtracking, đệ quy brute force).
"""
# O(1) - hằng số
def constant_example(arr):
    return arr[0]  # luôn chỉ chạy 1 bước

# O(n) - tuyến tính
def linear_example(arr):
    for x in arr:
        print(x)

# O(n^2) - bậc 2
def quadratic_example(arr):
    for i in arr:
        for j in arr:
            print(i, j)

# Test
arr = [1, 2, 3, 4, 5]
constant_example(arr)
linear_example(arr)
quadratic_example(arr)

#Viết một hàm tính tổng các phần tử mảng
def total(arr):
    return sum(arr)

# ass
