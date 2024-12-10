import re

'''
if a do comes before mul capture it
if a dont comes before mul dont capture it

dont = 0
do = 1

if dont, everything is nulled until we hit another one, at which point we resume multiplcation
there's a note, only the most recent  do() or dont() applies

its just on big text file
'''

lines = open("puzzle.txt","r")
#also unclude mull
capture_pattern = r"(mul\((\d+),(\d+)\))"
#do pattern
do_pattern = r"(do\(()\))"
#dont pattern
dont_pattern = r"(don't\(()\))"

#combine them
combined = r"(mul\((\d+),(\d+)\))|(do\(()\))|(don't\(()\))"

new_lines = ""
for l in lines:
    new_lines += l.strip('\n')


prod = 0
l = re.findall(combined,new_lines)
print(l)
is_enabled = True
for match in l:
    if 'do()' in match or "don\'t()" in match:
        if 'do()' in match:
            is_enabled = True
        else:
            is_enabled = False
    if is_enabled:
        if 'do()' in match:
            continue
        first,second = int(match[1]),int(match[2])
        prod += first*second
        continue
'''
new_line = []
for entry in l:
    if entry[0].startswith("mul"):
        new_line.append(int(entry[1])*int(entry[2]))
    elif 'do()' in entry:
        new_line.append('do')
    elif 'don\'t()' in entry:
        new_line.append('dont')
#calculate line product
print(new_line)

i = 0
n = len(new_line)
do_mult = True
for num in new_line:
    if num == 0:
        do_mult = False
    elif num == 1:
        do_mult = True
    elif do_mult == True:
        prod += num
'''

print(prod)
print(107991598)
