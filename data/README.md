# data

Map data for the route finder.

| File | Columns | Description |
|---|---|---|
| `places.csv` | `name, lat, lon` | One row per place, with approximate coordinates |
| `roads.csv` | `from, to, distance_km, time_min` | One row per road; roads are two-way |

Place names must be spelled exactly the same in both files.
