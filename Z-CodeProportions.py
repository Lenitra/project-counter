import os

# loop all files and subfiles in the directory


toret = {"py": 0
         , "js": 0
         , "html": 0
         , "css": 0
         , "yaml": 0}

for root, dirs, files in os.walk("."):
    for f in files:
        try:
            with open(os.path.join(root, f), 'r') as infile:
                lines = infile.readlines()
                for k,v in toret.items():
                    if f.endswith(k):
                        toret[k] += len(lines)
        except:
            pass

total = 0
for k,v in toret.items():
    total += v


percent = {}
for k,v in toret.items():
    percent[k] = round(v / total * 100, 2)



print()
print()
print()
print("Total lines of code: " + str(total))
print(toret)
print(percent)
print()
print()
print()