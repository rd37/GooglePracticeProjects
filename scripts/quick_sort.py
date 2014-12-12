'''
Created on Dec 11, 2014

@author: ronaldjosephdesmarais
'''
data=[13,11,23,45,22,10,20,56,33,22,1,77,8,9,33,2,5,4,1,8,9,876,33,45,21,78,65,4,3,11]
#data=[3,1]
print "use python sorted to compare"
print sorted(data)

print "use quick-sort"

def sort_it(swp_idx,cmp_idx):
    ptr_idx=swp_idx
    
    while ptr_idx<cmp_idx:
        if data[ptr_idx]<=data[cmp_idx]:
            tmp=data[swp_idx]
            data[swp_idx]=data[ptr_idx]
            data[ptr_idx]=tmp
            swp_idx+=1
        ptr_idx+=1
    tmp = data[swp_idx]
    data[swp_idx]=data[cmp_idx]
    data[cmp_idx]=tmp
    return swp_idx

def Quick_Sort(str_idx,end_idx):
    pvt_idx = sort_it(str_idx,end_idx)
    if pvt_idx-str_idx > 1:
        Quick_Sort(str_idx,pvt_idx-1)
    if end_idx-pvt_idx > 1:
        Quick_Sort(pvt_idx+1,end_idx)
    
print data
print "Now Lets Quick Sort"

Quick_Sort(0,len(data)-1)
print data
