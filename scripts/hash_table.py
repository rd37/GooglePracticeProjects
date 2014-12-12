'''
Created on Dec 11, 2014

@author: ronaldjosephdesmarais
'''
#define input
#obj1=object()
objects_defn=['hello',100,-1.1,'boomra',22,22,22,22]


#create hash buckets and hashable range
bucket_size=20
buckets=[]

for i in range(0,bucket_size):
    buckets.append([])
    
#create hash function use built in for now
def hash_this(obj):
    #replace this with your own
    return obj.__hash__()%bucket_size

def bucket_insert(bucket,value):
    bucket.append(value)

def bucket_remove(bucket,value):
    for obj in bucket:
        if obj == value:
            bucket.remove(value)
            return
    else:
        print "Error unable to find %s"%value
            
def double_up():
    global bucket_size
    bucket_size=bucket_size*2
    global buckets
    
    buckets_tmp=[]
    for i in range(0,bucket_size):
        buckets_tmp.append([])
    for bucket in buckets:
        while len(bucket)>0:
            item = bucket.pop()
            bucket_insert(buckets_tmp[hash_this(item)], item)
    buckets=buckets_tmp

def double_down():
    global bucket_size
    bucket_size=bucket_size/2
    global buckets
    
    buckets_tmp=[]
    for i in range(0,bucket_size):
        buckets_tmp.append([])
    for bucket in buckets:
        while len(bucket)>0:
            item = bucket.pop()
            bucket_insert(buckets_tmp[hash_this(item)], item)
    buckets=buckets_tmp

print "Insert Items into HashMap using Insert"
for entry in objects_defn:
    buck_idx = hash_this(entry)
    bucket_insert(buckets[buck_idx],entry)

print buckets

print "Test Remove <object>"
bucket_remove(buckets[hash_this(objects_defn[3])],objects_defn[3])

print buckets
print "Try to double up"
double_up()
print buckets
print "Try to double down"
double_down()
print buckets




