
dictionary = {}

def graph_list(input_list):
    # graph a list of tuples
    for i in input_list:
        # if the 2nd index is not in the dictionary
        if i[1] not in dictionary:
            # set the key to the 2nd index and the value to a set
            dictionary[i[1]] = set()
            # add the 1st index to the set
            dictionary[i[1]].add(i[0])
        # otherwise
        else:
            # just add the 1st index to the set
            dictionary[i[1]].add(i[0])

    return dictionary

def get_ancestors(person):
    if person in dictionary:
        return dictionary[person]

def earliest_ancestor(ancestors, starting_node):
    # graph the ancestors
    people = graph_list(ancestors)
    # create a Stack
    stack = []
    # push the starting node onto the stack in a list
    stack.append([starting_node])
    # keep track of visited children in a set
    visited = set()
    # keep track of longest path
    longest_path = []

    # so long as the stack is not empty,
    while len(stack) > 0:
        # get the current PATH
        current_path = stack.pop()
        # get the current person
        current_person = current_path[-1]

        # if the person has no parents, return -1
        if starting_node not in people:
            return -1
        
        # if we haven't seen this child before,
        if current_person not in visited:

            # if longest path is empty:
            if len(longest_path) == 0:
                # add current path to longest path list
                longest_path.append(current_path)
            # if the current PATH is longer than the longest PATH
            elif len(current_path) > len(longest_path[0]):
                # replace the longest PATH with the current PATH
                longest_path[0] = current_path
            # else if the current PATH and the longest PATH are the same length,
            elif len(current_path) == len(longest_path[0]):
                # make the longest PATH whichever one has the lowest value
                if current_path[-1] < longest_path[0][-1]:
                    longest_path[0] = current_path

            # add current person to the visited set
            visited.add(current_person)
            
            ancestors = get_ancestors(current_person)

            # the child has parents
            if ancestors is not None:
                # loop through all the ancestors of the current person
                for a in ancestors:
                    # copy the current path
                    new_path = list(current_path)
                    # add the ancestor to the new path
                    new_path.append(a)
                    # add the new path to the stack
                    stack.append(new_path)

    return longest_path[-1][-1]
