import json
file_path = "C:/Users/user/gpt_4o_mini_GPTScore_1500_0.json"

with open(file_path, "r") as fp:
    data = json.load(fp)

result = dict()

for key, value in data.items():
    add = 0
    count = 0
    print(f"key: {key}, value: {value}")
    for key2, value2 in value.items():
        add = add + value2
        count = count + 1

        if count == 10:
            break

    result[key] = add

#print(result)

file_path = "C:/Users/user/PycharmProjects/Json_test/package.json"
with open(file_path, "w", encoding="UTF-8") as fp:
    json.dump(result, fp)
