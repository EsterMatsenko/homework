def difference(*args):
    if len(args) == 0:
        return 0
    elif len(args) == 1:
        return args[0]
    else:
        max_value = max(args)
        min_value = min(args)
        return round(max_value - min_value, 2)
print(difference(1.25,2,3.21,4.33,5,6,7.169,8,9.2,10.3,11,12,13,14,15.7528))