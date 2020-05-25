# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    data={}
    # write your code here
    for i in range(len(values)):
        data[values[i]/weights[i]]=[values[i],weights[i]]
    access=list(reversed(sorted(data.keys())))
    for i in access:
        if(capacity>0):
            if(capacity-data[i][1]>=0):
                value+=data[i][0]
                capacity-=data[i][1]
            else:
                r=data[i][1]/capacity
                value+=data[i][0]/r 
                capacity-=data[i][1]/r
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
