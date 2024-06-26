import heapq

def dijkstra(graph, start):
    # 優先度付きキューの初期化
    queue = []
    heapq.heappush(queue, (0, start))

    # 各ノードの最短距離を無限大に初期化
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 既に見つけた最短距離よりも長い距離のノードは無視
        if current_distance > distances[current_node]:
            continue

    # 隣接ノードの距離を計算
    for neighbor, weight in graph[current_node].items():
        distance = current_distance + weight

        # 新しい最短距離が見つかった場合、更新して優先度付きキューに追加
        if distance < distances[neighbor]:
            distances[neighbor] = distance
            heapq.heappush(queue, (distance, neighbor))

    return distances

# 架空の路線図の定義（隣接リスト形式）
graph = {
'A': {'B': 1, 'C': 4},
'B': {'A': 1, 'C': 2, 'D': 5},
'C': {'A': 4, 'B': 2, 'D': 1},
'D': {'B': 5, 'C': 1}
}

# 始点ノード
start_node = 'A'

# ダイクストラ法を実行して最短距離を求める
shortest_distances = dijkstra(graph, start_node)

# 結果を表示
print(f"Starting from node {start_node}, the shortest distances to each node are:")
for node, distance in shortest_distances.items():
    print(f"Distance to {node}: {distance}")