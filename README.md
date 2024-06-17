# Algorithms

This is a collection of algos written in python, detailed with time and space complexity

## Usage
To run any algorithm simply,

Clone the repo:
```sh
git clone git@github.com:Puddi1/Algorithms.git ./algos
cd algos
```

Create a python3 environment for the project:
```sh
python3 -m venv .myvenv
```

Activate it:
```sh
source .myvenv/bin/activate
```

Install needed packages:
```sh
pip install -r requirements.txt
```

Finally, run an algorithm from top level directory as a module:
```sh
python3 -m src.algos.<script name>
```

Or a data strcture:
```sh
python3 -m src.data_structures.<script name>
```

Running files from top level directory as a module is needed as there are both algorithms and data structures, which are two submodules, that import each others.

To exit the environment:
```sh
deactivate
```


## Todo
The repo really needs some cleaning