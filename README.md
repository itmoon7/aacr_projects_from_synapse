```markdown
# AACR Project GENIE Data Download

This repository contains scripts and guidelines for downloading AACR Project GENIE data from Synapse programmatically.

## Data Access Guideline

To access the AACR Project GENIE public dataset, follow these steps:

1. Visit the AACR Project GENIE Public dataset page: [AACR Project GENIE Public](https://www.synapse.org/Synapse:syn7222066/wiki/410922).
2. Review the dataset files: [AACR Project GENIE Public Files](https://www.synapse.org/Synapse:syn7222066/files/).

## Setting Up the Environment

We recommend using a Conda environment to manage dependencies. A `.yml` file has been provided to create the necessary environment with all required packages installed.

### Step 0: Register for a Synapse Account

If you do not have a Synapse account, register here: [Synapse Account Registration](https://accounts.synapse.org/register1?appId=synapse.org).

### Step 1: Create Conda Environment

To create the Conda environment, use the provided `.yml` file:

```bash
conda env create -f environment.yml
conda activate your_environment_name
```

### Step 2: Authentication

Authenticate your Synapse client by generating a personal access token. Follow the guidelines here: [Synapse Authentication](https://python-docs.synapse.org/tutorials/authentication/).

### Step 3: Request Access

Before downloading the data, you need to request access for the specific dataset release. For example, to request access for Release 15.1-public, visit the following link and click on "Request Access": [Request Access for Release 15.1-public](https://www.synapse.org/Synapse:syn55234548).

## Downloading Data Programmatically

After setting up your environment and authentication, you can download the data programmatically. 

### Example Code

Here is an example of how to download data using the Synapse Python client. Run the script using the following command:

```bash
python download_files_synapse.py [auth_token] [project_SynID] [local_path]
```

Replace `[auth_token]`, `[project_SynID]`, and `[local_path]` with your personal access token, project Synapse ID, and the desired local download path, respectively.

## Additional Resources

- [Downloading Data Programmatically](https://help.synapse.org/docs/Downloading-Data-Programmatically.2003796248.html)
- [AACR Project GENIE Public Dataset](https://www.synapse.org/Synapse:syn7222066/files/)

For further assistance, refer to the official Synapse documentation.
```

Make sure to adjust the `your_environment_name` in the conda activation command to match the name specified in your `.yml` file.
