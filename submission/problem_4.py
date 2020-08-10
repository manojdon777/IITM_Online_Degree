v,e=map(int, input().split())
graph = {}
key = graph.keys()
for i in range(e):
	u,v=map(str,input().split())
	if i in key:
		graph[u].append(v)
		graph[v].append(u)
print (graph)