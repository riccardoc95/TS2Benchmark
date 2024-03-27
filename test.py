import argparse
import numpy as np
from memory_profiler import memory_usage
import tqdm
import os


parser = argparse.ArgumentParser()
parser.add_argument('--dataset', help='the name of the dataset to test')
parser.add_argument('--method', help='the name of the method to test')

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
        function = lambda x: - px.computePH(-x)
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

    print(f'{args.method}')
    print('----------')
    print(f'Execution time: ', round(max(time),1), 'sec')
    print(f'Peak of memory: ', round(max(mem_usage), 1), 'Mbyte')
