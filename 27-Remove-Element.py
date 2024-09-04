class Solution(object):
    def removeElement(self, nums, val):

        k = 0

        for i in range(len(nums)):
           #index per number in list 
           
            if nums[i] != val:
                #if not equal to val 
                nums[k] = nums[i]

                #nums k being the current postiion, nums i the current number to be in said postion k 
                k += 1

                #k as a counter of numbers not equal to val 


        return k
        #return val



        #longer solution

    #class Solution(object):
    #def removeElement(self, nums, val):
#   k = 0

 #       for i in range(len(nums)):
           #index per number in list 
           
  #          if nums[i] != val:
                #if not equal to val 
   #             nums[i] = nums[i]
    #            k += 1
    #.      else 
    #           nums.remove(i)


    #    return k


        
        

