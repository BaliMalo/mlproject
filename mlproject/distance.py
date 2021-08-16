from math import radians, cos, sin, asin, sqrt
import argparse

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r

if __name__ == "__main__":
    # Le Wagon location
    lat1, lon1 = 48.865070, 2.380009
    description = 'stkrgcp_description'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--coords',
                        nargs='+',
                        help='list of coordinates',
                        required=False)
    args = parser.parse_args()
    lon2, lat2 = args.coords
    distance = haversine(float(lon1), float(lat1), float(lon2), float(lat2))
    print(distance)