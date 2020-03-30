'''
ダイクストラ法
'''
import heapq

# N -> ノードの数
# M -> ノードをつなぐ枝の数
N, M = map(int,input().split())
nodes = [list(map(int,input().split())) for _ in range(M)]
#ノードの確定状態
node_comfirmed = [0] * N

# どのノードとどのノードが繋がっているか
dic_nodes_connection = {}
for i in range(M):
    dic_nodes_connection.setdefault(nodes[i][0], []).append(nodes[i][1])
    dic_nodes_connection.setdefault(nodes[i][1], []).append(nodes[i][0])

# ノード間の重さ
values_between_nodes = [[0 for _ in range(N)] for _ in range(N)]
for i in range(M):
    values_between_nodes[nodes[i][0]][nodes[i][1]] = nodes[i][2]
    values_between_nodes[nodes[i][1]][nodes[i][0]] = nodes[i][2]

# 各ノードまでの値を保持
ans = [float('inf')] * N

# 1. 始点に0を書き込む
ans[0] = 0
heapq_list = []
# リストを優先度付きキューへ
# 配列で渡した場合，インデックス0によって並び替えが行われる
# インデックス0に重さが入る
heapq.heapify(heapq_list)
heapq.heappush(heapq_list, [0, 0])

while heapq_list != []:
    # 2. ノードの中でもっとも小さい物を選び確定させる
    # 　 もしpopしたものがすでに確定されていたらcontinue
    
    current_node = heapq.heappop(heapq_list)
    node_value = current_node[0]
    node_number = current_node[1]

    if node_comfirmed[node_number] == 0:
        node_comfirmed[node_number] = 1
        ans[node_number] = node_value
    else:
        continue

    # 3. 確定したノードとつながっているノードを見て値を更新する
    for node_connection_number in dic_nodes_connection[node_number]:
        if node_comfirmed[node_connection_number] == 0:
            if ans[node_connection_number] > node_value + values_between_nodes[node_number][node_connection_number]:
                ans[node_connection_number] = node_value + values_between_nodes[node_number][node_connection_number]
            # 次の検索候補に追加
            heapq.heappush(heapq_list,[ans[node_connection_number], node_connection_number])

    # 4. 全ての地点が確定(= heapqが空)していれば終了

print(ans)
'''
# Input
7 10
0 1 2
0 2 5
1 2 4
2 3 2
1 3 6
1 4 10
3 5 1
4 5 3
4 6 5
5 6 9

# Output
[0, 2, 5, 7, 11, 8, 16]
'''