num = 0
files = {}
with open('1.txt',encoding='utf-8') as f:
    for line in f:
        num+=1
files["1.txt"] = num
num=0
with open('2.txt',encoding='utf-8') as f:
    for line in f:
        num+=1
files["2.txt"] = num
num=0
with open('3.txt',encoding='utf-8') as f:
    for line in f:
        num+=1
files["3.txt"] = num

sorted_dict = dict(sorted(files.items(), key=lambda x: x[1]))

for i in sorted_dict:
    print(i)
    print(sorted_dict[i])
    with open(i,encoding='utf-8') as f:
        text = f.read()
    print(text)
    
