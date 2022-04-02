import ast
import copy
import time
import numpy as np
import queue

# Jika menginginkan ukuran puzzle lebih besar
N=4
def getBlankIndex(matrix):
    for i in range(N):
        for j in range(N):
            if(matrix[i][j]==16):
                return [i,j]
def kurang(matrix):
    index=getBlankIndex(matrix)
    mat1 = []
    # ubah jadi 1d
    for a in matrix:
        for b in a:
            mat1.append(b)
    matrix = mat1
    kurang=[]
    pos=0
    sigma_kurang=0
    for i in range(N*N):
        tmp=matrix[i]
        count_kurang=0
        for j in range(i+1,16):
            if(tmp > matrix[j] and tmp!=0):
                sigma_kurang+=1
    if((index[0]+index[1])%2==0):
        sigma_kurang=sigma_kurang+0
    else :
        sigma_kurang=sigma_kurang+1
    return (sigma_kurang)
def display_kurang(matrix):
    index=getBlankIndex(matrix)
    mat1 = []
    # ubah jadi 1d
    for a in matrix:
        for b in a:
            mat1.append(b)
    matrix = mat1
    kurang=[]
    pos=0
    for i in range(N*N):
        tmp=matrix[i]
        count_kurang=0
        for j in range(i+1,16):
            if(tmp > matrix[j] and tmp!=0):
                count_kurang += 1
        kurang+=[[tmp,count_kurang]]        
    kurang.sort() #sort fungsi kurang ke-i
    for k in range(N*N):
        print("Nilai dari fungsi Kurang(" + str(kurang[k][0])+"):" ,kurang[k][1])
def cost(matrix): #tingkat start dari 1
    count = 0
    for i in range(N):
        for j in range(N):
            if((matrix[i][j] != final[i][j]) and matrix[i][j] != 16):
                count += 1
    return (count)
def punyasolusi(matrix):
    if(kurang(matrix)%2==0):
        return True
    else:
        return False
# queue
class Node:
    def __init__(self, parent, matrix, cost, blank, level):
        #parent
        self.parent = parent
        #matrix
        self.matrix = matrix
        # fungsi cost
        self.cost = cost
        # posisi block kosong
        self.blank = blank
        # level nodenya
        self.level = level
    #priority queue
    def __lt__(self, other): # prioritas cost lalu level
        if self.cost == other.cost:
            return self.level < other.level 
        return self.cost < other.cost
def isOnMatrix(blank):
    return 0 <= blank[0] < N and 0 <= blank[1] < N
def display(matrix):
    print('\n'.join(['\t'.join([str(cell) for cell in j]) for j in matrix]))
def print_path(root):
    if root is None:
        return
    print_path(root.parent)
    print("Level : ", root.level)
    display(root.matrix)
    print()
def solve(matrix,blank):
    #up, right, down, left
    #pergerakan blank space
    # untuk row -1 berarti geser keatas,1 geser kebawah,0 diam
    # untuk col -1 berarti geser kekiri,1 geser kekanan,0 diam
    #[[up],[right],[down],[left]]-> dengan susunan [row,col]
    move=[[-1,0],[0,1],[1,0],[0,-1]]
    visited = set()
    start = time.time()
    nodes = queue.PriorityQueue()
    visited.add(tuple(np.reshape(matrix,16)))
    # create root node
    rootcost = cost(matrix) # root cost
    root = Node(None,matrix, rootcost, blank, 0)
    nodes.put(root)
    if(punyasolusi(matrix)):
        print("Susunan Matrix Awal: ")
        display(matrix)
        print("")
        print("-----------------")
        print("Nilai dari fungsi Kurang (i) + X pada posisi awal :",kurang(matrix))
        display_kurang(matrix)
        print("Puzzle Dapat Diselesaikan")
        start = time.time()
        while not nodes.empty() :
            current = nodes.get()
            #Jika ingin mengetahui current state
            #display(current.matrix)
            #print("Gambar Ke:"+str(j+1)+", FUNGSI COST : " + str(current.cost+current.level) + ", LEVEL : " + str(current.level))
            #Jika ingin melihat state ke berapa tambahkan di while and j>=0 dan deklarasi j=0 diatas while
            # j+=1
            if (current.matrix) == final:
                stop = time.time()
                print("Susunan Akhir Puzzle")
                print("Terdapat "+ str(current.level)+" Langkah Untuk Menyelesaikan Puzzle dari Posisi Awal")
                print("")
                print("Berikut Langkah Menyelesaikan : ")
                print_path(current)
                #return current.level, stop - start, len(visited)
                print("level: ",current.level)
                print("waktu: ",stop - start)
                print("Jumlah Simpul:", len(visited))
                break
            for i in range(0,4): #Ada 4 move
                #posisi 16(blank) berdasarkan array arah gerak row dan col
                child_blank = [current.blank[0] +move[i][0],current.blank[1] + move[i][1]]
                if isOnMatrix(child_blank):
                    mat = copy.deepcopy(current.matrix)
                    #swap element 16(blank) dengan elemen yang berada pada kiri atau kanan atau atas atau bawah(sesuai arah gerak)
                    temp = mat[child_blank[0]][child_blank[1]]
                    mat[child_blank[0]][child_blank[1]] = 16
                    mat[current.blank[0]][current.blank[1]] = temp
                    while tuple(np.reshape(mat,16)) not in visited:
                        visited.add(tuple(np.reshape(mat,16)))
                        child_cost = cost(mat)+(current.level+1)
                        child = Node(current, mat, child_cost, child_blank, current.level + 1)
                        nodes.put(child)
    else:
        print("Nilai dari fungsi Kurang (i) +X pada posisi awal :",kurang(matrix))
        display_kurang(matrix)
        print("Puzzle Tidak Dapat Diselesaikan")

def bacaFile(namaFile):
    with open(namaFile+ str(".txt"), 'r') as f:
        matrix = [[int(i) for i in line.split(' ')] for line in f]
    return matrix
final = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print("Cara Memasukkan Puzzle: ")
print("1.From File")
print("2. Input Manual")
cara=int(input("Pilihlah cara memasukkan puzzle :"))
matrix=[[0 for i in range(N)] for i in range (N)]
if(cara==1):
    matrix=bacaFile(str(input("Masukkan Nama File (tanpa format (.txt)) : ")))
if(cara==2):
    for i in range (N) :
        for j in range(N):
            elemen=int(input("Elemen Matriks Baris ke- "+str(i+1)+" Kolom ke-" + str(j+1)+ " :" ))
            matrix[i][j]=elemen
blank=getBlankIndex(matrix)
solve(matrix,blank)
lanjut=str(input("Apakah ingin menyelesaikan puzzle lainnya?: Y/N" ))
