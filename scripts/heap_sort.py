'''
Created on Dec 10, 2014

@author: ronaldjosephdesmarais
'''
data = [3,7,16,8,10,12,1,5,11,13,2,4,15,14,9]
d_len = len(data)

def HEAP_SORT(i):
    i_val = data[i]
    if d_len > 2*i+1:
        l_val = data[2*i+1]
    else:
        l_val = None
    if d_len > 2*i+2:
        r_val = data[2*i+2]
    else:
        r_val = None
    
    if (l_val is None or i_val >= l_val) and (r_val is None or i_val >= r_val):
        return
    elif l_val > r_val:
        data[2*i+1] = i_val
        data[i] = l_val
        return HEAP_SORT(2*i+1)
    else:
        data[2*i+2] = i_val
        data[i] = r_val
        return HEAP_SORT(2*i+2)

print "------Create Heap------"
for i in range(0,d_len/2):
    HEAP_SORT(d_len/2-1-i)
print data

print "------Now Sortit ------"
for i in range(0,d_len-1):
    d_root=data[0]
    data[0]=data[d_len-1]
    data[d_len-1] = d_root
    d_len=d_len-1
    HEAP_SORT(0)

print data
    
