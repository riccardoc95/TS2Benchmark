# Benchmarking computational topology tools using interactive jobs

Frequently, we encounter multiple software implementations for tackling the same problem, prompting the need to identify the most efficient option. This scenario is evident in the computation of [persistent homology](https://en.wikipedia.org/wiki/Persistent_homology), a method for computing topological features of a space at different spatial resolutions. Numerous software solutions have emerged for this purpose. This study focuses on software designed to extract topological features from images, with a specific interest in zero-dimensional persistent homology achieved through [simplicial complex](https://en.wikipedia.org/wiki/Simplicial_complex) filtering. Two options for this task are [Ripser](https://github.com/scikit-tda/ripser.py/tree/master), renowned for its stability and versatility, and the newly developed [PixHomology](https://github.com/riccardoc95/PixHomology). To determine the most efficient solution in terms of execution time and memory usage, we propose a benchmarking approach on [Terastat2](https://www.dss.uniroma1.it/it/HPCTerastat2) utilizing [interactive jobs](https://engaging-web.mit.edu/eofe-wiki/slurm/srun/) for real-time results.

## 1. Creare lo spazio di lavoro:

### 1.1 Clonare la repository di GitHub
```bash
git clone https://github.com/riccardoc95/TS2Benchmark
```

### 1.2 Entrare nella workdir
```bash
cd TS2Benchmark
```

## 2. Set Conda Environmnet
In questo step viene inizializzato un nuovo environmnet utilizzando il gestore di pacchetti conda presente in TS2.

### 2.1 Attivare il modulo:
```bash
module load anaconda
```
### 2.2 Creare un nuovo environment python:
```bash
conda create -n ts2b python=3.11
```

### 2.3 Attivare l'environment ts2b:
```bash
conda activate ts2b
```

## 3 Installazione dei pacchetti python
### 3.1 Utilizzare il comando python pip
```bash
pip install ripser
```

### 3.2 Compilare il codice da una repository
```bash
git clone https://github.com/riccardoc95/PixHomology
cd PixHomology
```

```bash
module load gcc
```

```bash
module load cmake
```

```bash
pip install .
```

### 3.3 Installazione ricorsiva da file
```bash
pip install -r requirements.txt 
```

## 4. Download data
In questo step andremo a scaricare i dati necessari per il benchmark dei software
```bash
wget link_data
```

## 5. Esecuzione del job su una shell interattiva
```bash
srun
```
