"""Geometry helpers for the map.

The straight-line distance between two places is the basis of the A*
heuristic: no road can be shorter than the straight line, so it never
overestimates the real road distance.
"""

import math

EARTH_RADIUS_KM = 6371.0


def haversine_km(a, b):
    """Great-circle distance in km between two (lat, lon) points given in degrees."""
    lat1, lon1 = map(math.radians, a)
    lat2, lon2 = map(math.radians, b)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    h = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * EARTH_RADIUS_KM * math.asin(math.sqrt(h))
