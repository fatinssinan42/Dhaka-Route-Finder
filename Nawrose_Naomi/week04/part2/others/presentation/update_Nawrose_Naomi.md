# Update presentation (class 12): Nawrose's part

Slide 6, "BFS, UCS and A* side by side" (about 40 seconds)

- One map per algorithm, same start and goal: Gulshan 1 to Dhanmondi 27, shortest route.
- Red is the route, the green square is the start, the blue triangle is the goal. The box in the corner gives the cost and the number of places expanded.
- BFS takes only 2 roads but the route is 8.6 km. UCS and A* both find the 7.7 km route through Mohakhali and Farmgate.
- Anyone can draw this again: `python main.py --start "Gulshan 1" --goal "Dhanmondi 27" --plot`. The program also prints step-by-step directions for the route.

Likely questions

- *Why does BFS give a longer route?* It counts roads, not kilometres, so the first route it reaches uses the fewest roads.
- *How are the figures made?* visualize.py draws the places at their real latitude and longitude with networkx and matplotlib.
- *What comes next for the results?* An experiment runner that runs every algorithm on all 306 start-goal pairs and saves the results to a CSV file.

Timekeeping

- I keep time for the 5-minute slot: about 30 s title, 50 s per main slide, 20 s for next steps.
