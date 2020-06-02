import sys
def compute_min_refills(distance, tank, stops):
    stops=[0]+stops
    stops.append(distance)
    fuel=tank
    steps=0
    dist_stop=[]
    for i in range(len(stops)-1):
        dist_stop.append(stops[i+1]-stops[i])
    for i in range(len(dist_stop)):
        if(dist_stop[i]>tank):
            return -1
        fuel-=dist_stop[i]
        if(fuel<=0):
            steps+=1
            i-=1 
            fuel=tank
    return steps

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
