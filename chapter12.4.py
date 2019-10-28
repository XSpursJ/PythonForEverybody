import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://www.pocket-lint.com/phones/buyers-guides/huawei/146745-huawei-p30-vs-p30-pro-comparison')

for line in fhand:
    print(line.decode().strip())

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
