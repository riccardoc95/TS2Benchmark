import numpy as np
from memory_profiler import memory_usage
import tqdm
import os

dataset = input('the name of the dataset to test: ')
method  = input('the name of the method to test: ')

if dataset:
    dataset_dir = f'./data/{dataset}'
    files = list(os.listdir(dataset_dir))
else:
    dataset_dir = './data/MNIST'
    files = list(os.listdir(dataset_dir))
    
if method:
    if method == 'ripser':
        from ripser import lower_star_img
        function = lambda x: lower_star_img(x)
    elif method == 'pixh':
        import pixhomology as px
        function = lambda x: -1 * px.computePH(-1 * x)
    else:
        function = lambda x: x
else:
    function = lambda x: x

def benchmark_function(file): 
    input = np.load(os.path.join(dataset_dir, file))
    dgm = function(input)

if __name__ == "__main__":
    all_times = []
    all_mems = []
    for file in tqdm.tqdm(files):
        mem_usage = max(memory_usage((benchmark_function, ), interval=.01))
        time = len(mem_usage)/10
        output = [f'Method: {method}, File: {file}\nExecution time: {str(round(max(time),1))} sec, Peak of memory: {str(round(max(mem_usage), 1))} Mbyte\n']
        print(output)
        print()
        all_times.append(time)
        all_mems.append(mem_usage)

    all_times = np.array(all_times)
    all_mems = np.array(all_mems)
    output = f"Memory\nmin:{np.min(all_mems)}, mean:{np.mean(all_mems)}, max:{np.max(all_mems)}\n\nTime\nmin:{np.min(all_times)}, mean:{np.mean(all_times)}, max:{np.max(all_times)}"
    with open(f"benchmark_{dataset}_{method}.txt", 'w') as f:
        f.writelines(output)
    np.save(f"benchmark_{dataset}_{method}_time.npy", all_times)
    np.save(f"benchmark_{dataset}_{method}_mem.npy", all_mems)
