

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def calc_geometric_series_sum():
    a = float(input())
    r = float(input())
    n = int(input())
    geo_sum = 0
    for i in range(n):
        geo_sum = geo_sum + a*(r**i)
    return geo_sum


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
print("{:.4f}".format(calc_geometric_series_sum()), end="")

