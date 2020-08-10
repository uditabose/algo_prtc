
import sys
sys.path.append('./ds/')

from linked_list import linked_list

def kth_to_last(link_list, kth):
   '''
    2.2 find k-th element from last, O(N)
   '''
   curr_node = link_list
   count = 0 
   while count < kth:
      curr_node = curr_node.get_next()
      count += 1
    
   kth_node = link_list
   while curr_node != None:
      kth_node = kth_node.get_next()
      curr_node = curr_node.get_next()

   return kth_node

def run():
   base_list = ['m', 'q', 'g', 'z', 'o', 'a', 'u', 'e', 'a', 'm', 's']
   link_list = linked_list()
   link_list.build(base_list)
   print(link_list)
   
   for x in range(0, len(base_list)+2):
       kth = x
       kth_node = kth_to_last(link_list, kth)
       if kth_node != None:
          print("node[%d] = %s" % (kth, kth_node.get_data()))
       else:
          print("node[%d] = %s" % (kth, 'None'))
       

if __name__ == '__main__':
    run()

