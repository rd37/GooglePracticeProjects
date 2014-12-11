'''
Created on Dec 9, 2014

@author: ronaldjosephdesmarais
'''
str_to_srt = 'thisisthestringtosort'
str_alph = {'t':0,'h':1,'i':2,'s':3,'e':4,'r':5,'n':6,'g':7,'o':8}

srted_dict = {}
srted_cnt = {}

for c in str_to_srt:
    idx = str_alph[c]
    
    if idx in srted_dict:
        srted_cnt[idx] += 1
    else:
        srted_dict[idx] = c
        srted_cnt[idx] = 1
        
out_str = ''

for key in srted_dict:
    c = srted_dict[key]
    cnt = srted_cnt[key]
    
    out_str = "%s%s"%(out_str,c*cnt)

print out_str