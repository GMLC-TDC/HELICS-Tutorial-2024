# HELICS-Tutorial-2024 [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GMLC-TDC/HELICS-Tutorial-2024/main)

Click the following link to get started.
[https://mybinder.org/v2/gh/GMLC-TDC/HELICS-Tutorial-2024/main](https://mybinder.org/v2/gh/GMLC-TDC/HELICS-Tutorial-2024/main)

This is a online remote demonstration. So there's no installation required.

The tutorial has 3 parts:

1. Running the minimum API calls you will need to know in `demo.py`.
2. A simple value exchange that sends pi (i.e. 3.14...) back and forth between two federates. To run it start both the notebooks in that folder simultaneously and go back and forth.
3. An example transmission-distribution exchange between PyPower and OpenDSS via OpenDSSdirect. Similar to piexchange, this requires starting two notebooks simultaneously that each setup a federate and then interact via HELICS.

Notes:
*   In these examples the HELICS broker is setup by one of the federates programatically. It is also possible (and perhaps more common for large co-simulations) to start the broker directly using the executable provided by HELICS and then have federates attach.
*   Similarly these examples illustrate configuring the federates and their data exchange programatically. It is also possible to put this configuration information in a file and have HELICS read it in, which can make it easy to use the same federate code to be re-used as multiple different federates.  
*   For larger co-simulations, the helics-cli helps manage the process of configuring and starting a large number of federates.

If you are interested in running this demonstration on your computer, you can follow the installation steps below.

## Tutorial Installation (optional)

-   Install [Miniconda3](https://docs.conda.io/en/latest/miniconda.html)
-   Run the following

```
git clone https://github.com/GMLC-TDC/HELICS-Tutorial-2024
cd HELICS-Tutorial-2024
conda env create --name helics-environment --file=environments.yml
jupyter lab
```

You can check if everything has been installed correctly by running the following to start Python:

```
conda activate helics-environment
python
```

When Python has started you can run the following:

```
>>> import helics as h
>>> h.helicsGetVersion()
```


## Release
HELICS-Tutorial-2024 is distributed under the terms of the BSD-3 clause license. All new
contributions must be made under this license. [LICENSE](LICENSE)

SPDX-License-Identifier: BSD-3-Clause
