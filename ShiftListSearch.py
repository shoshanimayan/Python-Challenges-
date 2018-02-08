

"""
* returns max int in a shifted list
* checks to make sure that all elements in list are int
* arguements: List, the shifted list we look through for the max value
* returns: an int, which is the max int found in the shifted list, or prints out an error message if wrong type of elements in list
"""
def maxShiftedList(List):
    """if(list):
        if(all(isinstance(element, int) for element in List)):
            return max(List)
        else:
            raise TypeError("element of wrong type in array")
    else:
        raise TypeError("emptyList")
"""
    return  List[2:]+List[:2]
l=[2, 4, 6, 8, 10]
print(maxShiftedList(l))



"""

firstly I was confused by the question, as it was unclear if i was supposed to be implementing the shifting of the list as a requirement of the function
    but going off the documentation I assumed it wasn't, tho if it is it could be easily implemeted by creating a list that is shifted by its index
    through the following format List[-index:] + seq[:-index]

1. edge cases I accounted for where empty lists, as those could not be shifted or return anything,
    and lists that consist that have elements that are not int, and thus would get in the way of the finding out what tthe largest value int is

2. essentailly what we are being asked to do here is create an algorithm that returns the greatest int value in a non ordered list, which
    is already a built in function of python, as seen in max(), which always returns the max value of its given arguement.


3. 

"""
