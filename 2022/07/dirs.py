"""SUPER hacky day 7"""
with open('input.txt', 'r') as f:
    cmds = f.read().splitlines()

dirs = {'/': {'_s': 0}}
curr_dir = dirs
for cmd in cmds:
    if '$ cd' == cmd[:4]:
        new_dir = cmd.split(' ')[-1]
        curr_dir = curr_dir[new_dir]
        continue
    
    if '$ ls' == cmd[:4]: 
        continue
    
    if 'dir' == cmd[:3]:
        new_dir = cmd.split(' ')[-1]
        curr_dir[new_dir] = {'..': curr_dir, '_s': 0}
        continue
    
    fsize = int(cmd.split(' ')[0])
    curr_dir['_s'] += fsize


total = 0
del_total = 0
def find_totals(d: dict) -> dict:
    global total
    global del_total
    d['_t'] = d['_s']

    sub_dirs = set(d.keys()) - {'..', '_s'}
    if sub_dirs:
        for k in sub_dirs:
            if isinstance(d[k], dict):
                find_totals(d[k])
                sub_total = d[k]['_t']
                d['_t'] += sub_total

                if sub_total <= 100000:
                    total += sub_total
                
                if sub_total >= 358913:
                    if not del_total:
                        del_total = sub_total
                    elif sub_total < del_total:
                        del_total = sub_total

find_totals(dirs['/'])
print(total)
print(del_total)
print(30000000 - (70000000 - dirs['/']['_t']))
