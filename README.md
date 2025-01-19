# EEPE Simulation and Financial Modeling

## Overview
This repository contains a Python project that simulates Expected Exposures (EE) over time and calculates the Expected Effective Positive Exposure (EEPE) for financial models. The project is designed to help model and assess the credit risk of financial portfolios, particularly in the context of exposure calculations over time, providing insights into the risk levels over a defined period.

## Key Features
- **Exposure Simulation**: Simulates the expected exposures (EE) at each time step, modeling potential credit risk.
- **EEPE Calculation**: Computes the Expected Effective Positive Exposure (EEPE), a key metric used in financial institutions for assessing risk exposure.
- **Visualization**: Provides a graphical representation of simulated exposures over time and the calculated EEPE.

## Prerequisites
Before running the code, ensure you have the following Python libraries installed:

- `numpy`: For numerical operations and random number generation.
- `matplotlib`: For plotting graphs and visualizing results.

You can install them using pip:

```bash
pip install numpy matplotlib
```

Installation
To get started, clone the repository to your local machine:

```bash
git clone https://github.com/TKoskas/EEPE_Simulation.git
```

Navigate to the project folder:

```bash
cd EEPE_Simulation
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage
To simulate the expected exposures and calculate the EEPE, run the following Python script:

```bash
python eepe_simulation.py
```

## Example Output:
The program will output a list of simulated exposures, display the EEPE value, and show a plot representing the expected exposure over time, with a horizontal line indicating the EEPE.

Simulated Exposures (EE) over time:

[ 5.06142335 39.11097881 90.02433036 96.30470842 18.34439422 62.15211757 12.49852848 80.5098807  30.48223002 93.37377766 77.1716297  66.26950765]

Expected Effective Positive Exposure (EEPE): 55.94 million

How it works:

Simulated Exposures (EE): The program generates random exposure values over a specified number of time steps (e.g., 12 months). Each exposure represents the potential exposure at that time.

EEPE Calculation: The EEPE is calculated as the average of all positive exposures over the given time period.

Visualization: A plot is generated showing the variation of exposure over time, with a red dashed line representing the calculated EEPE.

This model can be extended to assess the credit risk of various financial products by adjusting the simulation parameters.

## License
This project is licensed under the MIT License
