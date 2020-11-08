import json
from matplotlib import pyplot

with open("data.json","r") as f:
	data = f.read()

data = json.loads(data)
res = {}
for i in range(0,24):
	res[i] = 0

cnt = 0
total = 0
for i in data:
	total += 1
	if i["last_match_time"] is not None:
		t = int(i["last_match_time"].split(":")[0][-2:])
		res[t] += 1
		cnt += 1
	
print(total,cnt)
print(res)

res_num = list(res.values())

pyplot.bar(range(24), res_num)
pyplot.show()
