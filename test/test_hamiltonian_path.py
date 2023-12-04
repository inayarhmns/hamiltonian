import os
import time
import tracemalloc
import sys
from statistics import mean

# Get the current directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Navigate to the parent directory and add it to sys.path
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

import hamiltonian_path as hp



def make_adj_matrix(filename):
    with open(filename, 'r') as file:
        # Read the first line to get the number of vertices and edges
        num_vertices, num_edges = map(int, file.readline().split())

        # Initialize the adjacency matrix with zeros
        adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        # Read the remaining lines to get the edges
        for line in file:
            v1, v2 = map(int, line.split())
            
            # Update the adjacency matrix for an undirected graph
            adjacency_matrix[v1][v2] = 1
            adjacency_matrix[v2][v1] = 1

    return adjacency_matrix

def get_num_vertices(filename):
    with open(filename, 'r') as file:
        num_of_vertices = int(file.readline().split()[0])
    return num_of_vertices


def elapsed_since(start):
    elapsed_time = (time.time() - start) * 1000  # Convert to ms
    return elapsed_time


def test(dataset_file):
    adj_matrix = make_adj_matrix(dataset_file)
    num_vertices = get_num_vertices(dataset_file)

    tracemalloc.start()
    start = time.time()
    
    # start testing
    N = len(adj_matrix)
    print(hp.Hamiltonian_path(adj_matrix, N))


    elapsed_time = elapsed_since(start)
    memory_peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return elapsed_time, memory_peak
    


def testall():
    folder_path = "dataset"
    mem_besar = []; mem_sedang = []; mem_kecil = []
    time_besar = []; time_sedang = []; time_kecil = []
    with open("test/result/hamiltonian_path_result.txt", 'w') as file:
        for filename in os.listdir(folder_path):
                filepath = os.path.join(folder_path, filename)
            
                # Check if the path is a regular file (not a directory)
                if os.path.isfile(filepath):
                    
                    elapsed_time, memory_peak = test(filepath)
                    file.write(f"Dataset {filepath}. Time: {str(elapsed_time)} ms. Memory peak: {memory_peak} B.\n")
                    
                    if filepath.startswith("dataset\dataset_besar"):
                        mem_besar.append(int(memory_peak))
                        time_besar.append(float(elapsed_time))
                    elif filepath.startswith("dataset\dataset_sedang"):
                        mem_sedang.append(int(memory_peak))
                        time_sedang.append(float(elapsed_time))
                    elif filepath.startswith("dataset\dataset_kecil"):
                        mem_kecil.append(int(memory_peak))
                        time_kecil.append(float(elapsed_time))
        
        file.write(f"Average dataset besar: Memory = {str(mean(mem_besar))} B. Time = {str(mean(time_besar))} ms. \n")
        file.write(f"Average dataset sedang: Memory = {str(mean(mem_sedang))} B. Time = {str(mean(time_sedang))} ms. \n")
        file.write(f"Average dataset kecil: Memory = {str(mean(mem_kecil))} B. Time = {str(mean(time_kecil))}  ms. \n")
    
if __name__ == "__main__":
    testall()
    


