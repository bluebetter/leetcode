#coding=utf-8

def find_inflection_port(arr):
    if len(arr) <= 2:
        return []
    ret = []
    for i in range(1, len(arr)-1):
        if ((arr[i] - arr[i-1]) * (arr[i+1] - arr[i])) < 0:
            ret.append(arr[i])
    return ret
