import random
from multiprocessing import Pool, cpu_count
import heapq

def get_random_data(x):
    data = []
    for i in range(x):
        data.append(random.randint(-x,x))
    return data

def sort_single(data):
    return sorted(data)

def parallel_sort(data):
    #Establish the number of parallel processes
    processes_count = cpu_count()
    chunk_size = len(data) // processes_count #divide with int precision

    #Divide dataset into smaller chunks, with chunk_size step
    chunks = []
    for i in range(0, len(data), chunk_size):
        chunks.append(data[i : i+chunk_size])
    
    #Parallel sorting
    with Pool(processes_count) as p:
        sorted_chunks = p.map(sort_single,chunks)

    #Merge sorted data
    #merged = sorted(sum(sorted_chunks, []))
    merged = list(heapq.merge(*sorted_chunks))

    return merged


if __name__ == '__main__':
    rand_data = get_random_data(100000)
    print("RANDOM ",rand_data)

    sorted_data = parallel_sort(rand_data)

    print("SORTED ",sorted_data)
    