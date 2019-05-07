#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from glob import glob
import shutil
import re


# In[2]:


md_list = []
md_list_tmp = glob("*/*.md")
for path in md_list_tmp:
    if path[-len('_edited.md'):] != '_edited.md':
        md_list.append(path)


# In[3]:


for path in md_list:
    with open(path, 'r', encoding='utf-8') as f:
        conts = f.read().split('\n')

    code_close = True
    code_blank = '    '
    code_name = '```python'

    for idx, cont in enumerate(conts):
        if cont[:len(code_blank)] == code_blank and len(cont) > len(code_blank):
            first_letter = cont[len(code_blank)]
            p = re.compile('[a-zA-Z]')
            m = p.match(first_letter)
            exists = m is not None or first_letter == '#' or first_letter == "'" or first_letter == '"' 

            if code_close and exists:
                code_close = False
                conts[idx] = code_name + '\n\n' + cont

        if code_close == False and cont != '' and cont[:len(code_blank)] != code_blank:
            code_close = True
            conts[idx] = '\n' + '```' + '\n' + cont

    final_conts = '\n'.join(conts)
    final_conts.split('\n')
    
    with open(path.replace('.md', '_edited.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(conts))


# In[4]:


if not os.path.exists('md_files'):
    os.makedirs('md_files')


# In[5]:


for path in glob("ch.*/*"):
    new_dir = 'md_files'
    file_name = os.path.basename(path)
    new_path = os.path.join(new_dir, file_name)
    shutil.copy(path, new_dir)


# In[6]:


edited_mds = []
for path in glob('*/*_edited.md'):
    edited_mds.append(os.path.basename(path))


# In[7]:


md_names = ' '.join(edited_mds)


# In[8]:


pandoc_cmd = 'pandoc -o ../output.epub --highlight-style tango --epub-cover-image ./sources/KakaoTalk_20190413_153131931.png ./sources/titlepage_eng.txt'

print(pandoc_cmd, md_names)


# In[ ]:




