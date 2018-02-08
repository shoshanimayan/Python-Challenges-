

"""
  maxShiftedList()
* returns max int in a shifted list
* checks to make sure that all elements in list are int
* arguements: List, the shifted list we look through for the max value
* returns: an int, which is the max int found in the shifted list, or prints out an error message if wrong type of elements in list
"""
def maxShiftedList(List):
    #check that list is not empty, list returns false if its empty
    if(list):
        # checks all elements in list are int
        if(all(isinstance(element, int) for element in List)):
            # returns the maximum element in the list
            return max(List) 
        else:
            raise TypeError("element of wrong type in array")
    else:
        raise TypeError("empty list, nothing to return")

  




"""

Firstly I was confused by the requirements of the question, as it was unclear if i was supposed to be implementing the shifting of the list as a requirement of the function
    but going off the documentation I assumed it wasn't, tho if it is, shifting could be easily implemeted by creating a list that is shifted by and index arguement
    through the following format: List[index:] + seq[:index], which would return the list shifted by its that index. Additionall this would not add to the complexity of the function

1. Edge cases I accounted for were empty lists, as those could not be shifted or return anything,
    and lists that consist that have elements that are not int (double, string, ect), and thus would get in the way of the finding out what the largest int value is as specified in the question.
    Hitting these edge cases will raise an error, I choose to do this instead of just printing a message because I believe a more professional function
    would raise an error and stop the entire process instead of letting it continue running incorrectly, although I see the appeal of just printing for debugging
    purposes.

2. Essentailly what we are being asked to do here is create an algorithm that returns the greatest int value in a non ordered list, which
    is already a built in function of python, as seen in max(), which always returns the max value of its given arguement. according the python documentation
    max() has a complexity class of O(n). Additionally the other consuming part of the my algorithm, the foreloop for checking if all the elements in the given
    list are int instances "all(isinstance(element, int) for element in List)):", is actually made of the all() function and a for loop, and is effectivley
    a nested loop with complexity O(n^2). Therefore, as a whole this the complexity of the is function grows quadraticly with the size of the given list,
    with a total complexity class of O(n^2)+ O(n) = O(n^2).

3. 

"""
