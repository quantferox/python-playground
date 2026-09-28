# MTC SOBES TEST TASK (by MASHA for strong middle JAVA Developer)

# a = [1,2,3,4,5,6] - TRUE
# b = [6,5,4,3,2,1] - TRUE
# c = [4,1,2,5,6,3] - FALSE

a = [1, 2, 3, 4, 5, 6]
b = [6, 5, 4, 3, 2, 1]
c = [4, 1, 2, 5, 6, 3]

# variant 1
# def is_sorted(arr):
#     if arr == sorted(arr) or arr == sorted(arr,reverse=True):
#         return True
#     return False


# def is_sorted(arr):
#     ascending = True
#     descending = True
#     for x in range(len(arr) - 1):
#         if arr[x] > arr[x + 1]:
#             ascending = False
#         if arr[x] < arr[x + 1]:
#             descending = False
#     return ascending or descending


# def is_sorted(arr):
#     return all(arr[x] <= arr[x + 1] for x in range(len(arr) - 1)) or all(
#         arr[x] >= arr[x + 1] for x in range(len(arr) - 1)
#     )
