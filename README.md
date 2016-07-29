# QuTech Tuning

Qcodes is a Python-based framework developed by QuTech (TU Delft/TNO) for automated tuning of qubits.

Also see
- [QuTech](https://http://qutech.nl/)
- [TNO](https://tno.nl)

QTT is compatible with Python 3.4+.

## Structure

QTT depends on Qcodes. Other repositories are the user scripts and measurement setups.

## Installation

We recommend [Anaconda](https://www.continuum.io/downloads) as an easy way to get most of the dependencies out-of-the-box.

As the project is still private, install it directly from this repository:

- Install git: the [command-line toolset](https://git-scm.com/) is the most powerful but the [desktop GUI from github](https://desktop.github.com/) is also quite good

- Clone this repositories somewhere on your hard drive. If you're using command line git, open a terminal window in the directory where you'd like to put qcodes and type:
```
git clone https://github.com/qdev-dk/Qcodes.git
git clone https://github.com/VandersypenQutech/qtt.git
git clone https://github.com/VandersypenQutech/users.git
git clone https://github.com/VandersypenQutech/stations.git
```

- Install python dependencies. For windows with anaconda:
```
> conda install numpy scipy matplotlib pandas scikit-image
> conda install spyder pyqtgraph
> pip install pyvisa
```
For other systems
```
> pip install numpy scipy matplotlib pandas scikit-image
> pip install numpy spyder pyqtgraph
> pip install pyvisa
```
- Register the repositories it with Python. For each of the repositories run this from the root directory:
```
> conda develop ./  (for Anaconda)
> python setup.py develop --user  (for other systems)
```


### Updating QTT

If you registered Qcodes with Python via `setup.py develop`, all you need to do to get the latest code is open a terminal window pointing to anywhere inside the repository and run `git pull`

## Usage

See the [docs](docs) directory (to be constructed)

## Contributing

See [Contributing](CONTRIBUTING.md) for information about bug/issue reports, contributing code, style, and testing


## License

See [License](LICENSE.txt)
