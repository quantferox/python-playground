# def sum_numbers(s):
#     if s == "":
#         return 0
#     parts = s.split(",")
#     total = 0
#     for part in parts:
#         part = part.strip()
#         if part == "":
#             continue
#         if part.isdigit():
#             total += int(part)
#         else:
#             raise ValueError("Input contains non-digit characters")
#     return total


# ==============================================================================
def sum_numbers(s):
    return 0 if not s else sum(int(x) for x in s.split(",") if x.isdigit())
