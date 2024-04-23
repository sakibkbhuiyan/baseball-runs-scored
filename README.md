Baseball Runs Scored Dashboard
==============================


This dashboard visualizes baseball game scores across different eras, allowing users to explore the distribution of runs scored by visiting and home teams.

<h2>Overview</h2>
The Baseball Runs Scored Dashboard is a web application built using Dash, a Python framework for building analytical web applications. It provides interactive visualizations of baseball game scores aggregated by era, allowing users to compare the distribution of runs scored in different historical periods.

--------

<h2>Features</h2>
<ul>
    <li>Heatmap Visualization: Explore the distribution of game scores using interactive heatmaps.
    <li>Histograms: View the density distribution of score differences for selected eras.
    <li>Era Selection: Choose from various historical eras to visualize the data.
</ul>

--------

<h2>Usage</h2>
<ol>
    <li>Clone the repository to your local machine.
    <li>Install the required dependencies by running <code>pip install -r requirements.txt </code>.
    <li>Run the Dash application using <code>python app.py </code>.
    <li>Access the dashboard in your web browser at <code>http://127.0.0.1:8050/</code>.
</ol>

--------

<h2> Demo </h2>
A demo of the dashboard is below: 
<br>
<img src="reports/figures/dash_app_gif.gif">

<h2>Data Source</h2>
The data used in this dashboard comes from Retrosheet's Baseball Game Logs, which includes detailed information about baseball games from various historical periods. The dataset is preprocessed and aggregated to provide insights into runs scored across different eras of baseball history.

--------

<h2>Contributors</h2>
<ul>
    <li><a href="https://github.com/sakibkbhuiyan">Sakib Bhuiyan</a>
</ul>

--------

<h2>License</h2>
This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.

--------

<h2>Project Organization</h2>

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<h2>Acknowledgements</h2>
<p><small>The information used here was obtained free of charge from and is copyrighted by Retrosheet.  Interested parties may contact Retrosheet at "www.retrosheet.org". </small></p>
<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
