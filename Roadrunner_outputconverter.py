import pickle
import sys
import RoadGraph
import utm

roadgraph = pickle.load(open(sys.argv[1],"rb"))

file1 = open('roadrunner_vertices.txt', 'a+')
file2 = open('roadrunner_edges.txt', 'a+')
vertices = []
edge_iterator = 1

for edge in roadgraph.edges.values():
	n1, n2 = edge[0], edge[1]
	if roadgraph.nodes[n1] not in vertices:
		vertices.append(roadgraph.nodes[n1])
		file1.write(str(vertices.index(roadgraph.nodes[n1])+1)+","+str(utm.from_latlon(roadgraph.nodes[n1][0],roadgraph.nodes[n1][1])[0])+","+str(utm.from_latlon(roadgraph.nodes[n1][0],roadgraph.nodes[n1][1])[1])+"\n")
	if roadgraph.nodes[n2] not in vertices:
		vertices.append(roadgraph.nodes[n2])
		file1.write(str(vertices.index(roadgraph.nodes[n2])+1)+","+str(utm.from_latlon(roadgraph.nodes[n2][0],roadgraph.nodes[n2][1])[0])+","+str(utm.from_latlon(roadgraph.nodes[n2][0],roadgraph.nodes[n2][1])[1])+"\n")
	file2.write(str(edge_iterator)+","+str(vertices.index(roadgraph.nodes[n1])+1)+","+str(vertices.index(roadgraph.nodes[n2])+1)+"\n")
	edge_iterator += 1

file1.close()
file2.close()

