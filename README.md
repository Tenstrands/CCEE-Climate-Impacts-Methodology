# CCEE Whitepaper Extreme Heat Analysis Template User Guide

## Description
This is the Jupyter Notebook for analyzing datasets for extreme heat in California, along with utility functions and datasets required for execution.

## Installation Steps

### Option 1: Google Colab Setup

#### Prerequisites
Ensure you have a Google account to use Google Colab.

#### Setting Up Your Environment
1. **Download the Project**:
    - Go to the repository page on GitHub.
    - Click the green **Code** button.
    - Select **Download ZIP**.
    - Extract the ZIP file on your local machine.

2. **Upload to Google Drive**:
    - Upload the extracted folder to your Google Drive.

3. **Open Google Colab**:
    - Open the template that you want to explore in the templates folder. The default option should open the template in Google Colab.

4. **Mount Google Drive**:
    - From the left sidebar, click `Files`.
    - Under where it says Files, click the **Mount Drive** button. Colab should automatically insert a cell to run.
    - Run the cell and follow the prompts. Select **Allow All** when Google Drive asks for access.
    - Wait a few seconds until you see `Mounted at /content/drive`. A `drive` folder should appear above `sample_data` on the left.

5. **Set Working Directory**:
    - Hover below the cell you ran in step 4. There should be an option to `+ Code` or `+ Text`. Select `+ Code`.
    - Copy the following code into the new cell you created. This sets the working directory to the templates directory.
    ```python
    import os
    os.chdir('paste-path-here')
    ```
    - Locate the `templates` folder inside `CCEE-Climate-Impacts-Methodology`. Click the three dots next to that folder and select **Copy path**.
    - In the code cell where it says `paste-path-here`, delete it and paste in the path you just copied. Do not remove the single quotation marks.
    - Run the cell.
    - To confirm you are in the right directory. Add a new code cell like before and run:
    ```python
    !pwd
    ```
    - You should see something ending in `../CCEE-Climate-Impacts-Methology/templates`.


6. **Run the Notebook**:
    - Run template as you wish.

7. **Exploring Other Templates**:
    - Repeat steps 3-5 for the new template.

### Option 2: Local Setup

#### Prerequisites
Before running the Jupyter notebook, ensure that you have the following installed:

- **Python**: Version 3.6 or higher is recommended. You can download it from the official Python website.
- **Jupyter Notebook**: This can be installed via pip if it is not already included in your Python installation.

#### Downloading the Project
1. Go to the repository page on GitHub.
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Extract the ZIP file on your local machine.

#### Install Required Libraries
Open your command line interface (Command Prompt, Terminal, etc.) and run:
```bash
pip install -r requirements.txt
```

#### Setting Up Your Environment
1. **Start Jupyter Notebook**: In the command line, type:
    ```bash
    jupyter notebook
    ```
   This will start the Jupyter server and open the Jupyter Notebook interface in your web browser.

2. **Open Your Notebook**: In the Jupyter interface, navigate to your notebook (e.g., `high_heat.ipynb`) and click to open it.

#### Running the Notebook
- **Execute Cells**: Click on a cell and press `Shift + Enter` to execute it. You can also use the **Run** button in the toolbar.

## Troubleshooting Common Issues

- **Import Errors**: If you encounter an error saying a module cannot be found, make sure it’s installed in your environment and correctly imported in your notebook.
- **File Not Found**: If the notebook cannot find your datasets, ensure the file paths are correct. They should be relative to where your notebook is located.

## Closing Jupyter Notebook
- **Shut Down the Notebook**: Close the tab in your web browser when you’re done.
- **Stop the Jupyter Server**: Go back to your command line and press `Ctrl + C` to stop the server. Confirm with `Y` when prompted.

---
