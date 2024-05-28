# Import Libraries
import numpy as np
import tqdm
import os
from memory_profiler import memory_usage


# 1. Ask the user what dataset they want to use and which program to test
dataset = 
method  = 

# 2. Set dataset_dir as the dataset directory path. 
# If the inserted dataset is not known, use the MNIST path.
if dataset:
    dataset_dir = 
else:
    dataset_dir = 

files = list(os.listdir(dataset_dir))
   
# Load software
if method == 'ripser':
    from ripser import lower_star_img
    function = lambda x: lower_star_img(x)
elif method == 'pixh':
    import pixhomology as px
    function = lambda x: -1 * px.computePH(-1 * x)
else:
    function = lambda x: x

# 3. Define the benchmark function
# For each file in the files list, we need to load the file into 
# memory (Hint use np.load(). function) and apply the function
def benchmark_function():
    for file in tqdm.tqdm(files):
       # ...
      
if __name__ == "__main__":
    mem_usage = memory_usage((benchmark_function, ), interval=.01)
    time = np.arange(0, len(mem_usage)/10, 0.1)

    # 4. Print mem_usage and time for the program and write this information into a log file (txt file)
    # ...
    # ...
    with open(f"benchmark_{dataset}_{method}.txt", 'w') as f:
        f.writelines(output)
