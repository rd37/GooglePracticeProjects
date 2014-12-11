'''
Created on Dec 9, 2014

@author: ronaldjosephdesmarais
'''
#global obj_root_cp
obj_root_cp=None

class copy_visitor(object):
    prev_node = None
    
    def __init__(self,name):
        self.name=name
        
    def visit(self,obj_node):
        if hasattr(obj_node,'next_cp'):
            #print "check if next2 is none"
            if obj_node.next2 is not None:
                obj_node.next_cp.next2 = obj_node.next2.next_cp
            if obj_node.next is not None:
                obj_node.next.accept(self)
        else:
            #create node
            #set prev links, if any
            
            obj_cp = obj(obj_node.name)
            obj_node.next_cp = obj_cp
            if self.prev_node is None:
                self.prev_node = obj_node
                print "Setting root cp of new array"
                global obj_root_cp
                if obj_root_cp is None:
                    #global obj_root_cp
                    obj_root_cp  = obj_cp
            else:
                self.prev_node.next_cp.next=obj_cp
                self.prev_node = obj_node
            if obj_node.next is not None:
                obj_node.next.accept(self)
            
                
            

class visitor(object):
    def __init__(self,name):
        self.name=name
    
    def visit(self,obj_node):
        if obj_node.next2 is not None:
            print '%s->%s'%(obj_node.name,obj_node.next2.name)
        else:
            print '%s'%(obj_node.name)
        if obj_node.next is not None:
            obj_node.next.accept(self)
        
class obj(object):
    next=None
    next2=None
    def __init__(self,name):
        #self.name='id:%s'%(self.__hash__())
        self.name=name
        
    def accept(self,visitor):
        visitor.visit(self)
        
obj1 = obj('O1')
obj2 = obj('02')
obj3 = obj('03')
obj4 = obj('04')
obj5 = obj('05')

obj1.next=obj2
obj1.next2=obj5

obj2.next=obj3
obj2.next2=obj1

obj3.next=obj4
obj3.next2=obj3

obj4.next=obj5
obj4.next2=obj1

obj5.next2=obj3

root_obj=obj1

visitor1 = visitor('show list')
root_obj.accept(visitor1)

print "____create copy in O(n) time_____"
cv = copy_visitor('create copy')
root_obj.accept(cv)
root_obj.accept(cv)
obj_root_cp.accept(visitor1)

#cv2 = copy_visitor('create copy',1)
#root_obj.accept(cv2)
#obj_root_cp.accept(visitor1)
