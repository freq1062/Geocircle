from math import radians, degrees, cos, sin, tan, asin, atan, acos, sqrt, pi
#start = [43.5018428 + degrees( 2 * (asin(1000/(6378100*2))) ), -79.6668495]
#start = [42.852566, 117.848660]
start = [0.0010001, 0.001001]
center = [43.5032268, -79.6669038]

def haversine(c1, c2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    lat1 = c1[0]
    lon1 = c1[1]
    lat2 = c2[0]
    lon2 = c2[1]
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371*1000 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    #I changed it to metres with the times 1000
    return c * r

def getCoords(radius, dist, start, angle):
    # Distance in metres
    #6371*1000
    disty = radius * (2 * asin( ( dist * (sin(angle)) ) / (2*radius) ) )#radians
    latRad = ( radius * cos( (radians(start[0] - (disty / radius) ) ) ) )
    distx = latRad * (2 * asin( ( dist * (cos(angle)) ) / (2*latRad) ) )
    #print(distx,disty)
    dlat = distx/radius * 180/pi
    #dlon = disty/radius * 180/pi
    #dlat = ( distx / ( radius * cos( (radians(start[0])) - (distx / radius) ) )) * 180/pi
    dlon = ( disty / ( radius * cos( (radians(start[0])) - (disty / radius) ) )) * 180/pi
    #dlon = disty/latRad * 180/pi
    #print(dlat, dlon)
    return [start[0]-dlat, start[1]-dlon]

coord = []
#print(start)
for i in range(0, 11):
    coord = (getCoords(6378100, 6378100/2, start, i*36))
    print(str(start[0])+","+str(start[1]))
    print(str(coord[0])+","+str(coord[1]))
#for i in range(100, 200):
    #print(haversine(start, [start[0], start[1]+ 0.0000001 * i]), i)
    #print(haversine([0, 0], [0, 0.0000001 * i]), i)
#coords.append(getCoords(145/1000, 2.9/1000, start))
#for i in range(0, 3):
#    coords.append(getCoords(145, 2.9/1000, coords[len(coords)-1]))
#    #haversine(start, target), target)
#print(coords)
