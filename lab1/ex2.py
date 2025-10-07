import random
from multiprocessing import Process

def random_data(x):
    data = []
    for i in range(x):
        data.append(random.randint(-x,x))
    return data

def sort(data):
    sorted_data = sorted(data)
    return sorted_data

def parallel_sort(data):
    #Set number of parallel processes
    #p = Pool(4)
    #sorted_data = p.map(sort(data),len(data))
    p = Process(target=sort, args=data)
    p.start()
    p.join()
    
    #return sorted_data

if __name__ == '__main__':
    rand_data = random_data(100000)
    print("RANDOM ",rand_data)

    sorted_data = parallel_sort(rand_data)

    print("SORTED ",sorted_data)
    