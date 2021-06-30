result = ""

jammed = []

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        jammed.append(line)

l = len(jammed[0])

freqs = [{} for _ in range(l)]

for s in jammed:
    for (i,c) in enumerate(s):
        freqs[i][c] = freqs[i].get(c, 0) + 1

for i in range(l):
    maxc = max(freqs[i], key=lambda x: freqs[i][x])
    result += maxc
        


with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))

