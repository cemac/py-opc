[![DOI](https://zenodo.org/badge/30832320.svg)](https://zenodo.org/badge/latestdoi/30832320)

# py-opc
A Fork of the R1 pull request from the py-opc library

## Dependencies

One of the following, depending on whether you use GPIO pins or a SPI-USB adapter:
  1. [`py-spidev`](https://github.com/doceme/py-spidev) - for those using GPIO pins
  1. [`pyusbiss`](https://github.com/dancingquanta/pyusbiss) - for those using a SPI-USB adapter (python3+ only)


## Installation
To install a version of the library which self updates on changes, use:
`pip setup.py develop`


### USB
    `pip3 install pyusbiss`

### GPIO
    `pip install git+https://github.com/doceme/py-spidev.git`


## License

  This library is licensed under the MIT license. The full text of the license can be found in this repository at LICENSE.txt.

## Documentation

  Full documentation can be found [here](http://py-opc.readthedocs.org/en/latest/).
