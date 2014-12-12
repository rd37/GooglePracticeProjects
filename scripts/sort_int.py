'''
Created on Dec 10, 2014

@author: ronaldjosephdesmarais
only works for small integer values due to dict hash function
'''
ints = [5,8,1,7,4,13,12,4,8,62,63,33,42,51]

print "------use python sorted------"
print sorted(ints)

print "------use dictionary   ------"
srt_dict = {}
srt_arr = []

for i in ints:
    if i not in srt_dict:
        srt_dict[i]=1
    else:
        srt_dict[i]=srt_dict[i]+1

for i_key in srt_dict:
    for i in range(0,srt_dict[i_key]):
        srt_arr.append(i_key)

print srt_arr