matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
final=[[2,3,15,4],[1,5,8,16],[13,7,6,14],[10,9,12,11]]
tes=[[2,3,15,4],[1,5,8,16],[13,7,6,14],[10,9,12,11],[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(tuple(tes)[1])
visited=[]
matrix=tuple(matrix)
final=tuple(final)

'''
visited.append(matrix)
visited.append(final)
print(visited)
print(visited[0])
if(visited[0]!=visited[1]):
    print('a')
'''
if(final==matrix):
    print("bener")
if(final[1]!=matrix[1]):
    print('salah')