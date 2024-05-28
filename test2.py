import argparse
import numpy as np
from memory_profiler import memory_usage
import tqdm
import os


parser = argparse.ArgumentParser()
# 1. Write a python parser to get dataset and method variable
# Hint: use function add_argument define in parser object
# https://docs.python.org/3/library/argparse.html




args = parser.parse_args()

if args.dataset:
    dataset_dir = f'./data/{args.dataset}'
    files = list(os.listdir(dataset_dir))
else:
    dataset_dir = './data/MNIST'
    files = list(os.listdir(dataset_dir))
    
if args.method:
    if args.method == 'ripser':
        from ripser import lower_star_img
        function = lambda x: lower_star_img(x)
    elif args.method == 'pixh':
        import pixhomology as px
        function = lambda x: -1 * px.computePH(-1 * x)
    else:
        function = lambda x: x
else:
    function = lambda x: x

def benchmark_function():
    for file in tqdm.tqdm(files):
        input = np.load(os.path.join(dataset_dir, file))
        dgm = function(input)

if __name__ == "__main__":
    mem_usage = memory_usage((benchmark_function, ), interval=.01)
    time = np.arange(0, len(mem_usage)/10, 0.1)

    output = [f'{args.method}\n', 
             '----------\n',
             f'Execution time: ', str(round(max(time),1)), 'sec\n',
             f'Peak of memory: ', str(round(max(mem_usage), 1)), 'Mbyte\n']
    with open(f"benchmark_{args.dataset}_{args.method}.txt", 'w') as f:
        f.writelines(output)
