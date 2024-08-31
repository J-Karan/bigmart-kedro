# Big Mart Sales Prediction Project

## Overview

This Kedro project aims to build a predictive model for sales forecasting using the "big mart" dataset. The project covers data processing, data engineering, model building, and visualization. The following components are included:

- **Data Processing**: Clean and preprocess the data.
- **Data Engineering**: Feature engineering and transformation.
- **Model Building**: Training and evaluating predictive models.
- **Visualization**: Exploring the data and model results using Plotly and Matplotlib.
- **Pipeline Management**: Managing workflows with Kedro Pipelines and Nodes.
- **Pipeline Visualization**: Visualizing pipelines with Kedro Viz.

## Project Structure

- `src/`: Source code for the project.
  - `src/big_mart_pipelines/pipeline.py`: Defines the Kedro pipelines.
  - `src/big_mart_pipelines/nodes.py`: Contains functions for each node in the pipelines.
  - `src/big_mart_pipelines/filters.py`: Filters for data processing and engineering.
  - `src/big_mart_pipelines/models.py`: Model definitions and training functions.
  - `src/big_mart_pipelines/visualization.py`: Functions for generating plots and visualizations.
- `data/`: Directory for storing raw and processed data.
- `conf/`: Configuration files.
  - `conf/base/catalog.yml`: Data catalog configuration.
  - `conf/base/logging.yml`: Logging configuration.
- `notebooks/`: Jupyter notebooks for exploratory data analysis (EDA).
- `tests/`: Unit tests for the project.
