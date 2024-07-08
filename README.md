# AACR Project Data Download

This repository contains scripts and instructions for downloading AACR Project data from Synapse programmatically.

## Setting Up the Environment and Downloading Data

We recommend using a Conda environment to manage dependencies. `environment.yml` file has been provided to create the necessary environment with all required packages installed.

### Step 0: Register for a Synapse Account

If you do not have a Synapse account, register here: [Synapse Account Registration](https://accounts.synapse.org/register1?appId=synapse.org).

### Step 1: Create Conda Environment

To create the Conda environment, use the provided `environment.yml` file:

```bash
conda env create -f environment.yml
conda activate aacr_project_genie
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
