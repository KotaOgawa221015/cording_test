from collections import defaultdict

# test_data = [
#     "1, 2, 8.54",
#     "2, 3, 3.11",
#     "3, 1, 2.19",
#     "3, 4, 4",
#     "4, 1, 1.4"
# ]

#グラフの構築(標準入力)
def build_graph():
    graph = defaultdict(list)
    while True:
        try:
            # 入力を行う
            line = input().strip()
            if not line:
                break
            start, end, distance = line.split(',')
            start, end, distance = int(start.strip()), int(end.strip()), float(distance.strip())
            graph[start].append((end, distance))
        except EOFError:
            break
    return graph

# # グラフの構築（テスト）
# def build_graph():
#     graph = defaultdict(list)
#     for line in test_data:  # ここで直接リストを使って入力データを指定
#         line = line.strip()
#         if not line:
#             continue
#         start, end, distance = line.split(',')
#         start, end, distance = int(start.strip()), int(end.strip()), float(distance.strip())
#         graph[start].append((end, distance))
#     return graph


# 深さ優先探索(DFS)による最長経路の探索
def dfs(graph, node, visited, path, path_length, best_path, best_length):
    visited[node] = True
    path.append(node)
    
    # 現在の経路の長さが最長経路よりも長ければ更新
    if path_length > best_length[0]:
        best_length[0] = path_length
        best_path[:] = path[:]
    
    # 次のノードを探索
    for neighbor, distance in graph[node]:
        if neighbor not in visited or not visited[neighbor]:
            dfs(graph, neighbor, visited, path, path_length + distance, best_path, best_length)
    
    visited[node] = False
    path.pop()

# 最長経路を求める関数
def find_longest_path():
    graph = build_graph()
    best_path = []
    best_length = [0]
    
    # グラフ内のすべての駅（ノード）を探索
    nodes = list(graph.keys())

    visited = {node: False for node in graph}

    for node in nodes:
        if not visited[node]:
            dfs(graph, node, visited, [], 0, best_path, best_length)
    
    # 最長経路を出力
    for station in best_path:
        print(station, end="\r\n")

# メイン関数
if __name__ == "__main__":
    find_longest_path()
