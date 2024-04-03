# Pair of gloves
# Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.

# Given an array describing the color of each glove, return the number of pairs you can constitute, assuming that only gloves of the same color can form pairs.

# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# result = 2 (1 red pair + 1 blue pair)

# input = ["red", "red", "red", "red", "red", "red"]
# result = 3 (3 red pairs)

def solution(gloves):
    pairs = {}
    glove_count = 0
    for glove in gloves:
        if glove not in pairs:
            pairs[glove] = 1
        else:
            pairs[glove] += 1
    for val in pairs.values():
        count = val // 2
        glove_count += count 
    return glove_count


# def solution(arr):
#     gloves = {}
#     glove_count = 0
#     for color in arr:
#         if color not in gloves:
#             gloves[color] = 1
#         else:
#             gloves[color] += 1
#     for val in gloves.values():
#         x = val // 2
#         glove_count += x
#     return glove_count

print(solution(["red", "red", "red", "red", "red", "red"]))



