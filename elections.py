in_data = open('input.txt', encoding='utf8')
out_data = open('output.txt', 'w', encoding='utf8')
candidate_dict = {}
votes_count = int()
for line in in_data:
    candidate_list = line.strip().split('/n')
    for candidate in candidate_list:
        candidate_dict[candidate] = candidate_dict.get(candidate, 0) + 1
        votes_count += 1
sort_votes = sorted(candidate_dict.items(), key=lambda x: x[1], reverse=True)
for item in sort_votes:
    percent = int(item[1]) / votes_count * 100
    if percent > 50:
        print(item[0], file=out_data)
        break
    else:
        for name, _ in sort_votes[:2]:
            print(name, file=out_data)
        break
