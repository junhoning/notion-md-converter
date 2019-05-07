import os
from glob import glob

md_list = glob("*.md")

code_blank = '    '

for path in md_list:
    with open(path, 'r', encoding='utf-8') as f:
        conts = f.read().replace('\n\n    ', '\n\n```python\n\n    ').split('\n')
        for idx, cont in enumerate(conts):
            if cont == '' and conts[idx-1][:len(code_blank)] == code_blank:
                if conts[idx+1] != '' and conts[idx+1][:len(code_blank)] != code_blank:
                    conts[idx] = '\n\n```'

            if idx == len(conts) -1:
                if cont[:len(code_blank)] == code_blank:
                    conts.append('\n\n```')


        for idx, cont in enumerate(conts):
            if cont[:4] == '    ':
                conts[idx] = cont.replace('  ', '', 1)

    with open(path.replace('.md', '_edited.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(conts))