import tkinter as tk
import heapq

stops = {
    'Central Station': {'Market Square': 5, 'City Park': 8, 'University': 10, 'Library': 7, 'Shopping Mall': 14},
    'Market Square': {'Central Station': 5, 'City Park': 6, 'Library': 7, 'Shopping Mall': 9},
    'City Park': {'Central Station': 8, 'Market Square': 6, 'Library': 11, 'Shopping Mall': 3, 'Hospital': 12},
    'Library': {'Central Station': 7, 'Market Square': 7, 'City Park': 11, 'Shopping Mall': 4, 'Hospital': 11},
    'Shopping Mall': {'Central Station': 14, 'Market Square': 9, 'City Park': 3, 'Library': 4, 'Hospital': 8},
    'University': {'Central Station': 10, 'City Park': 14},
    'Hospital': {'City Park': 12, 'Library': 11, 'Shopping Mall': 8}
}


class BusRouteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Find best bus route")

       
        self.start_label = tk.Label(root, text="Enter starting bus stop:")
        self.start_label.pack()
        self.start_entry = tk.Entry(root)
        self.start_entry.pack()

        self.end_label = tk.Label(root, text="Enter ending bus stop:")
        self.end_label.pack()
        self.end_entry = tk.Entry(root)
        self.end_entry.pack()

        self.stops_label = tk.Label(root, text="Enter additional stop:")
        self.stops_label.pack()
        self.stops_entry = tk.Entry(root)
        self.stops_entry.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        
        self.find_button = tk.Button(root, text="Find Route", command=self.find_route)
        self.find_button.pack()

    def findShortestRoute(self, start, end):
        distances = {node: float('inf') for node in stops}
        distances[start] = 0
        priority_queue = [(0, start)]
        previous_nodes = {}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node == end:
                path = []
                while current_node:
                    path.insert(0, current_node)
                    current_node = previous_nodes.get(current_node)
                return distances[end], path

            for neighbor, weight in stops[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        print("No valid route found.")
        return None

    def find_route(self):
        start_stop = self.start_entry.get().title()
        end_stop = self.end_entry.get().title()
        intermediate_stop = self.stops_entry.get().strip().title()

        if start_stop not in stops or end_stop not in stops:
            self.result_label.config(text="Invalid bus stops. Please try again.")
        elif intermediate_stop and intermediate_stop not in stops:
            self.result_label.config(text="Invalid stop stop. Please try again.")
        else:
            if intermediate_stop:
                # vahepeatusega
                result = self.findShortestRoute(start_stop, intermediate_stop)
                intermediate_distance, intermediate_path = result
                result = self.findShortestRoute(intermediate_stop, end_stop)
                end_distance, end_path = result
                full_path = intermediate_path + end_path[1:]  
                shortest_distance = intermediate_distance + end_distance
            else:
                # ilma vahepeatuseta
                result = self.findShortestRoute(start_stop, end_stop)
                shortest_distance, full_path = result

            route_description = f"Shortest distance from {start_stop} to {end_stop}: {shortest_distance} km\nRoute: {' -> '.join(full_path)}"
            self.result_label.config(text=route_description)


root = tk.Tk()
app = BusRouteApp(root)
root.mainloop()

