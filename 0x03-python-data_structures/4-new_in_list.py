#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ahtyat = my_list[:]
    if 0 <= idx < len(my_list):
        ahtyat[idx] = element
        return(ahtyat)
    return(my_list)
