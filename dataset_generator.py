import os
import random


# This code generates the txt files in /dataset
def generate_graph(num_vertices, num_edges):
    vertices = list(range(0, num_vertices))
    edges = set()

    # Ensure non-directed edges without duplicates and no loops
    while len(edges) < num_edges:
        v1, v2 = random.sample(vertices, 2)
        
        # Check if v1 is equal to v2 (loop), skip this iteration if true
        if v1 == v2:
            continue

        edge = (min(v1, v2), max(v1, v2))
        edges.add(edge)

    return vertices, list(edges)

def write_graph_to_file(vertices, edges, filename):
    file_path = os.path.join("dataset", filename)
    with open(file_path, 'w') as file:
        file.write(f"{len(vertices)} {len(edges)}\n")
        for edge in edges:
            file.write(f"{edge[0]} {edge[1]}\n")

def generate_type(num_vertices, num_edges, type, dataset_number):
    vertices, edges = generate_graph(num_vertices, num_edges)
    if type == "besar":
        write_graph_to_file(vertices, edges, f'dataset_besar{dataset_number}.txt')
    elif type == "sedang":
        write_graph_to_file(vertices, edges, f'dataset_sedang{dataset_number}.txt')
    elif type == "kecil":
        write_graph_to_file(vertices, edges, f'dataset_kecil{dataset_number}.txt')


def generate():
    generate_type(20, 120, "besar", 1)
    generate_type(18, 120, "sedang", 1)
    generate_type(16, 120, "kecil", 1)
    generate_type(20, 100, "besar", 2)
    generate_type(18, 100, "sedang", 2)
    generate_type(16, 100, "kecil", 2)
    generate_type(20, 80, "besar", 3)
    generate_type(18, 80, "sedang", 3)
    generate_type(16, 80, "kecil", 3)


if __name__ == "__main__":
    generate()
    