import heapq

def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances

# Graph represented as adjacency list with weights
# Node 0 = Pizza shop, nodes 1-4 = customer locations
graph = {
    0: [(1, 10), (2, 15)],
    1: [(0, 10), (3, 12), (4, 15)],
    2: [(0, 15), (4, 10)],
    3: [(1, 12), (4, 2)],
    4: [(1, 15), (2, 10), (3, 2)]
}

distances = dijkstra(graph, 2)
print("Minimum time from pizza shop to each location:")
for node in range(len(distances)):
    print(f"Location {node}: {distances[node]} minutes")

# Sum or route planning to minimize total delivery time can be complex, 
# this example shows shortest paths from shop to each location.
