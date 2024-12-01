import os

with open("day-1-input.txt", "r", encoding="utf-8") as f:
    input = f.read()
input.rstrip()
pair_list = input.split("\n")
left_list = []
right_list = []

for i in pair_list.copy():
    if i == "":
        continue
    else:
        split_item = i.split()
        left_list.append(int(split_item[0]))
        right_list.append(int(split_item[1]))

left_list.sort()
right_list.sort()

dif_list = []

for i in range(len(left_list)):
    dif = abs(left_list[i] - right_list[i])
    dif_list.append(dif)

similarity_score = 0

for l in left_list:
    sim = 0
    for r in right_list:
        if l == r:
            sim += 1
    similarity_score += l * sim


answer = sum(dif_list)

# print(left_list)
# print(right_list)
# print(dif_list)
print("Answer: {}".format(str(answer)))
print("Similarity Score: {}".format(str(similarity_score)))
