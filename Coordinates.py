from math import radians, degrees, cos, sin, tan, asin, atan, acos, sqrt, pi
start = [0.0010001, 0.001001]
center = [0, 0]#Put in the center coordinates

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

def getCoords(radius, dist, start, angle):#Angle in radians
    # Distance in metres
    # Derived using trigonometry
    disty = radius * (2 * asin( ( dist * (sin(angle)) ) / (2*radius) ) )#radians
    latRad = ( radius * cos( (radians(start[0] - (disty / radius) ) ) ) )
    distx = latRad * (2 * asin( ( dist * (cos(angle)) ) / (2*latRad) ) )
    dlat = distx/radius * 180/pi
    dlon = ( disty / ( radius * cos( (radians(start[0])) - (disty / radius) ) )) * 180/pi
    return [start[0]-dlat, start[1]-dlon]

coord = []
#Print the coordinates into arr coord
for i in range(0, 11):
    coord = (getCoords(6378100, 350, start, i*36))
    print(str(start[0])+","+str(start[1]))
    print(str(coord[0])+","+str(coord[1]))
