# CCEE Whitepaper Extreme Heat Analysis Template User Guide

## Description

This the Jupyter Notebook for analyzing datasets for extreme heat in California, along with utility functions and datasets required for execution.

## Prerequisites

Before running the Jupyter notebook, ensure that you have the following installed:

- **Python**: Version 3.6 or higher is recommended. You can download it from the [official Python website](https://www.python.org/downloads/).
- **Jupyter Notebook**: This can be installed via pip if it is not already included in your Python installation.

## Installation Steps
1. **Downloading the Project**
    1. Go to the repository page on GitHub.
    2. Click the green **Code** button.
    3. Select **Download ZIP**.
    4. Extract the ZIP file on your local machine.

2. **Install Required Libraries**:
   Open your command line interface (Command Prompt, Terminal, etc.) and run:
   ```bash
   pip install -r requirements.txt
   ```

## Setting Up Your Environment
1. **Start Jupyter Notebook**:
   In the command line, type:
   ```bash
   jupyter notebook
   ```
   This will start the Jupyter server and open the Jupyter Notebook interface in your web browser.

2. **Open Your Notebook**:
   In the Jupyter interface, navigate to your notebook (i.e.`high_heat.ipynb`) and click to open it.

## Running the Notebook

1. **Execute Cells**:
   Click on a cell and press **Shift + Enter** to execute it. You can also use the **Run** button in the toolbar.


## Troubleshooting Common Issues

- **Import Errors**: If you encounter an error saying a module cannot be found, make sure it’s installed in your environment and correctly imported in your notebook.
- **File Not Found**: If the notebook cannot find your datasets, ensure the file paths are correct. They should be relative to where your notebook is located.

## Closing Jupyter Notebook

1. **Shut Down the Notebook**: Close the tab in your web browser when you’re done.
2. **Stop the Jupyter Server**: Go back to your command line and press **Ctrl + C** to stop the server. Confirm with **Y** when prompted.
