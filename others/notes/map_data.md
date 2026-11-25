# Map data notes (Week 1)

Owner: Abdullah Al Galib

## Places

18 well-known places, spread across the city and linked by main roads (including Bashundhara R/A, where NSU is):

Uttara, Airport, Bashundhara R/A, Banani, Gulshan 1, Badda, Mohakhali, Mirpur 10, Agargaon, Farmgate, Kawran Bazar, Mohammadpur, Dhanmondi 27, Shahbag, New Market, Rampura, Malibagh, Motijheel.

Coordinates are approximate (3 decimals, about 100 m), read from Google Maps by placing a pin on a central landmark of each area. They are stored in `data/places.csv`.

## File formats

- `data/places.csv`: `name, lat, lon`
- `data/roads.csv`: `from, to, distance_km, time_min` (one row per road; roads are two-way)

Names must be spelled exactly the same in both files (for example always `Dhanmondi 27`, never `Dhanmondi`).

## Draft road list (about 30 roads)

Main corridors we connect:

- Airport Road: Uttara - Airport - Banani
- Pragati Sarani: Airport - Bashundhara R/A - Badda - Rampura
- Hatirjheel: Gulshan 1 - Kawran Bazar, Rampura - Kawran Bazar
- Bijoy Sarani / Rokeya Sarani: Mohakhali - Farmgate, Mirpur 10 - Agargaon - Farmgate
- Mirpur Road: Mohammadpur - Dhanmondi 27 - New Market
- Old Dhaka side: Kawran Bazar - Shahbag - Motijheel, Malibagh - Motijheel

## How costs are estimated

- **Distance**: the driving distance along the road, which is always longer than the straight line between the two places.
- **Time**: typical off-peak driving time. Wide roads (Airport Road, Pragati Sarani, Hatirjheel) are faster per km than busy roads (Farmgate, Malibagh, New Market), which is why the fastest route is not always the shortest.

All values are approximate and should be checked against Google Maps.

## Checks the loader must run

1. Every road has positive distance and time (UCS needs non-negative costs).
2. No road is shorter than the straight line between its ends (keeps the A* heuristic admissible).
3. Every place can be reached from every other place.
4. Every name in `roads.csv` exists in `places.csv`.
