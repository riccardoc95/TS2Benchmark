# Benchmarking computational topology tools using interactive jobs

Frequently, we encounter multiple software implementations for tackling the same problem, prompting the need to identify the most efficient option. This scenario is evident in the computation of [persistent homology](https://en.wikipedia.org/wiki/Persistent_homology), a method for computing topological features of a space at different spatial resolutions. Numerous software solutions have emerged for this purpose. This study focuses on software designed to extract topological features from images, with a specific interest in zero-dimensional persistent homology achieved through [simplicial complex](https://en.wikipedia.org/wiki/Simplicial_complex) filtering. Two options for this task are [Ripser](https://github.com/scikit-tda/ripser.py/tree/master), renowned for its stability and versatility, and the newly developed [PixHomology](https://github.com/riccardoc95/PixHomology). To determine the most efficient solution in terms of execution time and memory usage, we propose a benchmarking approach on [Terastat2](https://www.dss.uniroma1.it/it/HPCTerastat2) utilizing [interactive jobs](https://engaging-web.mit.edu/eofe-wiki/slurm/srun/) for real-time results.

## 0. Connect to TS2
Accessing TS2 involves establishing a connection to the login node through the ssh text terminal. The command from the terminal is:
```bash
ssh -l user_name -p 2020 ts2.uniroma1.it
```
where `user_name` is the personal username assigned to you after the access request. For more details see [https://dss.uniroma1.it/it/HPCTeraStat2/Collegarsi](https://dss.uniroma1.it/it/HPCTeraStat2/Collegarsi).

## 1. Workspace Setup:
In this section, our objective is to establish a directory on the Terastat platform encompassing all essential files indispensable for comprehensively engaging with the tutorial.

### 1.1 Clone the GitHub repository
To *clone the GitHub repository* means to create a local copy of a repository hosted on GitHub on your machine. This allows you to access the files, commit changes, and collaborate with others. The necessary command to accomplish this is typically `git clone <repository_URL>`.
The repository URL for this tutorial is [https://github.com/example/repository.git](https://github.com/riccardoc95/TS2Benchmark), the command would be:

```bash
git clone https://github.com/riccardoc95/TS2Benchmark
```
This command will download all the files from the specified repository into a directory named after the repository on your local machine.

### 1.2 Change the working directory
Navigate to the working directory refers to changing the current directory in the command line interface to the directory where you want to perform actions or execute commands. This can be achieved using the `cd` command followed by the directory path. The working directory is named **TS2Benchmark**, the command is:
```bash
cd TS2Benchmark
```
This command would switch the current directory to TS2Benchmark within the home directory, allowing you to carry out tasks within that specific directory.

## 2. Setup Conda Environment
TS2 provides a set of products and software libraries of general interest. Among these, we find the conda package manager. To activate the module just execute the command:
```bash
module load anaconda
```
When executed, this command loads the Anaconda module, which is a distribution of the Python (and/or R) programming language along with additional packages and tools commonly used in scientific computing, data science, and machine learning. Loading the Anaconda module ensures that the Anaconda distribution and its associated tools are available for use within the current environment (including the **conda** command), enabling users to easily access Python and its associated libraries for their computational tasks.

After loading the form you will need to restart your session. You can terminate and rerun the `ssh` session or execute
```bash
source ~/.bashrc
```

### 2.1 Create a new Python environment:
Since the packages already present in the Conda distribution are not sufficient and we need to install others and since modifying the base environment is restricted in Conda/Anaconda, we opt to create a fresh environment. This can be achieved using the following command:
```bash
conda create -n ts2b python=3.11
```
This creates a new Conda environment named **ts2b** with Python version 3.11.

To use the new environment we must activate it with:
```bash
conda activate ts2b
```
When activated, this environment becomes the primary environment for executing commands and running Python scripts within the current terminal session.


## 3 Python packages
Now we can proceed with installing the packages. There are several methods to install Python packages, each with its own advantages and use cases. Here are the most common methods:

### 3.1 Using pip (Python Package Installer):
**pip** is the default package manager for Python. To install a package using **pip**, you can use `pip install package_name`. For example, we need to install the Ripser package. The command is:
```bash
pip install ripser
```
For installing multiple packages at once we can use a requirements file. The `requirements.txt` file typically contains a list of package names. To install using **pip**, you can use:
```bash
pip install -r requirements.txt 
```

**ATTENTION**: Also Conda is a package manager for Python. It is particularly useful for managing Python environments and installing packages with dependencies.
To install a package using Conda, you can use the following command `conda install package_name`. However, not all Python packages are managed by conda. 

### 3.2 From Source
Sometimes, you may want to install a package directly from its source code. This happens when a package is not present on pip or you need a different version than the one managed by pip.
This involves downloading the source code from the package's repository and running the setup script to install it.
For example, PixHomology package is not yet on pip. We can download its source code with:
```bash
git clone https://github.com/riccardoc95/PixHomology
cd PixHomology
```
As compiling the source code requires specific development tools, we rely on TS2 to provide these tools. However, to access them, we must load the necessary modules. Specifically, we require a C compiler and the CMake utility. This can be accomplished using the following commands:
```bash
module load gcc
module load cmake
```
The commands to install from source may vary depending on the package, but typically involve running:
```bash
pip install .
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
