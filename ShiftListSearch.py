

"""
  maxShiftedList()
* returns max int in a shifted list of int
* checks to make sure that all elements in list are int, and list is not empty
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
    but going off the documentation I assumed it wasn't, though if it is, shifting could be easily implemeted by creating a list that is shifted by an index arguement
    through the following format: List[index:] + List[:index], which would return the list shifted by its that index. I believe this would not add to the complexity of the function

1. Edge cases I accounted for were empty lists, as those could not be shifted or return anything,
    and lists that have elements that are not int (double, string, ect), and thus would get in the way of the finding out what the largest int value is as specified in the question.
    Hitting these edge cases will raise an error, I chose to do this instead of just printing a message because I believe a more professional function would raise an error and stop the entire
    process instead of letting it continue running incorrectly, although I see the appeal of just printing for debugging purposes.

2. Essentailly what we are being asked to do here is create an algorithm that returns the greatest int value in a non ordered list, which
    is already a built in function of python, as seen in max(), which always returns the max value of its given arguement. according the python documentation
    max() has a complexity class of O(n). Additionally the other consuming part of the my algorithm, the foreloop for checking if all the elements in the given
    list are int instances "all(isinstance(element, int) for element in List)):", is actually made of the all() function and a for loop, and is effectivley
    a nested loop with complexity O(n^2). before any of that we check that the list is not empty which has a complexity of O(1). Therefore, at worst this the
    complexity of the is function grows quadraticly with the size of the given list, with complexity class of O(n^2)+ O(n) = O(n^2), and at best it has a complexity of O(1) when the list is empty.

3. One way to simplify this problem would be to guarentee that all the elements inside the list are int, meaning we dont have have to check for that edge
    case of seeing if any of the elements are not int, which is the most most consuming part of the algorithm at O(n^2), getting rid of checking for this
    edge case would reduce the algorithms complexity to O(n), and have the problem grow linearly instead of quadraticly. I would recommend implementing
    this change by recreating this problem in another language such as java or c++, while Python is incredibly easy to use and is very
    practical for getting a lot of work done quickly, it is that same practicality that can sometimes make python inefficent in terms of complexity. In
    this case the fact that Python is dynamically typed, meaning types are only checked at run time, and you can't declare types for variables or
    parameters like you do in Java or C++ can make things easier but more consuming because you can always just make assumptions about typing.
    Additionally, if given more time I would look to see if any library existed for python that would allow python to simulate static typing so that we would
    not need to check typing within the function itself.

"""
