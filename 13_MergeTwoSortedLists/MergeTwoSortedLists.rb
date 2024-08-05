#An attemp at Ruby. I'm going to do an actual online course before diving into it becasue the syntax is wierd.



# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} list1
# @param {ListNode} list2
# @return {ListNode}
def merge_two_lists(list1, list2)
    #Start - enstablish the head 
    if list1.val < list2.val
        rlist = list1
        list1 = list1.next
    end
    else
        rlist = list2
        list2 = list2.next
    end
    #Loop - populate the body
    while true
        if list1.val < list2.val
            rlist.next = list1
            list1 = list1.next
        end

            if list1 == nil
                rlist.next = list2
                return rlist
            end
        else
            rlist.next = list2
            list2 = list2.next

            if rlist2 == nil
                rlist.next = list1
                return rlist
            end
        end
end