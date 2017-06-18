def solution(list_of_nums):
    """Enter Code Here"""
    count1=0
    count2=0
    for index in list_of_nums:
        if index%2 == 0:
            count1 += 1
        else:
            count2 += 1


    return {"ODD": count2 ,"EVEN": count1}
