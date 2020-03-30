'''
# 辞書型で無向グラフを表現
# https://yottagin.com/?p=1822

graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.print_graph()
>> {1: [2], 2: [1, 3], 3: [2]}
'''
class Graph():
    def __init__(self):
        """ ノードのつながりを辞書型で表現する """
        self.adjacency_dict = {}
    
    def add_vertex(self, v):
        """ ノードを追加する """
        self.adjacency_dict[v] = []
    def add_edge(self, v1, v2):
        """ ノード同士をつなぐ。"""
        # 無向グラフの場合は双方向。もし有向グラフなら片側のみ。
        self.adjacency_dict[v1].append(v2)
        self.adjacency_dict[v2].append(v1)
    def remove_edge(self, v1, v2):
        """ ノード同士のつながりを削除する。"""
        self.adjacency_dict[v1].remove(v2)
        self.adjacency_dict[v2].remove(v1)
    def remove_vertex(self,v):
        """ ノードを削除する。"""
        while self.adjacency_dict[v] != []:
            adjacent_vertex = self.adjacency_dict[v][-1]
            self.remove_edge(v, adjacent_vertex)
        del self.adjacency_dict[v]
    
    def print_graph(self):
        print(self.adjacency_dict)
    
    def dfs_stack(self, start, visited=None):
        """ 深さ優先探索 Depth First Search スタックバージョン"""
        # ノードを格納するスタック
        stack = [start]
        # 訪れた順番を格納
        visited = []
        
        while stack != []:
            current_vertex = stack.pop()
            visited.append(current_vertex)
            for v in self.adjacency_dict[current_vertex]:
                if v not in visited and v not in stack:
                    stack.append(v)
        print(visited)
            
    def bfs(self, start, visited=None):
        # ノードを格納するキュー
        queue = collections.deque([start])
        # 訪れた順番を格納
        visited = []
        while list(queue) != []:
            current_vertex = queue.popleft()
            visited.append(current_vertex)
            for v in self.adjacency_dict[current_vertex]:
                if v not in visited and v not in queue:
                    queue.append(v)
        print(visited)