# Bubble Sort
# def bubble_sort(arr):
#     n = len(arr)
#     for x in range(n):
#         for y in range(0, n - x - 1):
#             if arr[y] > arr[y + 1]:
#                 arr[y], arr[y + 1] = arr[y + 1], arr[y]
#     return arr

# my_list1 = [34, 3, 25, 17, 29, 70, 12]
# sorted_array1 = bubble_sort(my_list1)

# print(sorted_array1)

# Merge Sort
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1
#     return arr

# my_list2 = [23, 45, 2, 50, 87, 34]
# sorted_array2 = merge_sort(my_list2)

# print(sorted_array2)


# Quick Sort
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[len(arr) // 2]
#         left = [x for x in arr if x < pivot]
#         middle = [x for x in arr if x == pivot]
#         right = [x for x in arr if x > pivot]
#         return quick_sort(left) + middle + quick_sort(right)
    

# temperatures = [25, 30, 28, 27, 26, 29, 31]

# sorted_temperatures = quick_sort(temperatures)

# print(sorted_temperatures)




# # Linear Search
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# # Binary Search 
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# # Task: Search for "Msanii" in a list of student names
# student_names = ["Alice", "Brian", "Chloe", "David", "Msanii", "Eve", "Frank"]
# target_name = "Msanii"

# # Linear Search
# linear_search_result = linear_search(student_names, target_name)
# print(f"Linear Search: '{target_name}' found at index {linear_search_result}" if linear_search_result != -1 else f"'{target_name}' not found")

# # Binary Search (List must be sorted)
# sorted_student_names = sorted(student_names)
# binary_search_result = binary_search(sorted_student_names, target_name)
# print(f"Binary Search: '{target_name}' found at index {binary_search_result} in the sorted list" if binary_search_result != -1 else f"'{target_name}' not found")





def create_graph():
    graph = {
        "Nairobi": {"Mombasa": 500, "Kisumu": 300, "Eldoret": 280, "Kitui": 150},
        "Mombasa": {"Nairobi": 500, "Kisumu": 800, "Kitui": 300},
        "Kisumu": {"Nairobi": 300, "Mombasa": 800},
        "Eldoret": {"Nairobi": 280, "Kitui": 200},
        "Kitui": {"Nairobi": 150, "Mombasa": 300, "Eldoret": 200}
    }
    return graph

def display_graph(graph):
    for city, neighbors in graph.items():
        print(f"{city}: {neighbors}")


# graph = create_graph()
# display_graph(graph)


import heapq

def dijkstra(graph, start, end):
    pq = [(0, start)]
    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    previous = {city: None for city in graph}

    while pq:
        current_distance, current_city = heapq.heappop(pq)
        if current_distance > distances[current_city]:
            continue

        for neighbor, weight in graph[current_city].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_city
                heapq.heappush(pq, (distance, neighbor))

    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous[current]

    return path, distances[end]

graph = create_graph()

start_city = "Eldoret"
end_city = "Mombasa"
shortest_path, shortest_distance = dijkstra(graph, start_city, end_city)

print(f"Shortest path from {start_city} to {end_city}: {shortest_path}")
print(f"Shortest distance: {shortest_distance}")



# class InventorySystem:
#     def __init__(self):
#         self.inventory = {}  # Dictionary to store items and their quantities

#     def add_item(self, item, quantity):
#         if item in self.inventory:
#             self.inventory[item] += quantity
#         else:
#             self.inventory[item] = quantity
#         print(f"Added {quantity} of {item}. Current stock: {self.inventory[item]}")

#     def remove_item(self, item, quantity):
#         if item in self.inventory and self.inventory[item] >= quantity:
#             self.inventory[item] -= quantity
#             print(f"Removed {quantity} of {item}. Current stock: {self.inventory[item]}")
#             if self.inventory[item] == 0:
#                 del self.inventory[item]
#         else:
#             print(f"Cannot remove {quantity} of {item}. Not enough stock or item does not exist.")

#     def search_item(self, item):
#         if item in self.inventory:
#             return f"{item} is available. Quantity: {self.inventory[item]}"
#         else:
#             return f"{item} is not available in the inventory."

# # Example Usage
# inventory = InventorySystem()

# # Adding items
# inventory.add_item("Laptop", 10)
# inventory.add_item("Smartphone", 15)

# # Removing items
# inventory.remove_item("Laptop", 5)

# # Searching for items
# print(inventory.search_item("Laptop"))
# print(inventory.search_item("Tablet"))



