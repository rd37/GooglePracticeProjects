'''
Created on Dec 9, 2014

@author: ronaldjosephdesmarais
'''
str='thisisthestring sort ok very well ok ABC is not the CBA ok'
count_array={}
value_array={}
print "Sort this %s"%str

print "___the easy way using sorted_____"
str_arr = sorted(str)
print ''.join(str_arr)
print "___the hard way using dict_____"

for i in str:
    h_code = ord(i)
   
    if h_code in value_array:
        count_array[h_code] += 1
    else:
        value_array[h_code] = i
        count_array[h_code] = 1

print "___show sorted array___"

sorted_str=''

for key in value_array:
    char = value_array[key]
    cnt = count_array[key]
    #print "%s:%s"%(char,cnt)
    for i in range(0,cnt):
        sorted_str = "%s%s"%(sorted_str,char)
        
print sorted_str
    