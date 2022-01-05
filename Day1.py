class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list3 = []
        
        l1 = []
        l2 = []
        least = 1000
        res = 1
        final = []
        
        for element in list1:
            if element in list2:
                list3.append(element)
        
        for i in list3:
            l1.append(list1.index(i))            
            l2.append(list2.index(i))
  

        for i in range(len(l1)):
            if l1[i] + l2[i] < least:
                least = l1[i] + l2[i]
                res = min(l1[i], l2[i])
                
        for i in range(len(l1)):
            if l1[i] + l2[i] == least:
                final.append(list3[i])
                
        return final
