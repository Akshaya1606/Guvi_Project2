
# Phonepe Pulse Data Visualization and Exploration
A User-Friendly Tool Using Streamlit and Plotly

This project will be a live geo visualization dashboard that displays
information and insights from the Phonepe pulse Github repository in an interactive
and visually appealing manner.Users will be able to access the dashboard from a web browser and easily navigate
the different visualizations and facts and figures displayed. 

The dashboard will
provide valuable insights and information about the data in the Phonepe pulse
Github repository, making it a valuable tool for data analysis and decision-making.
Overall, the result of this project will be a comprehensive and user-friendly solution
for extracting, transforming, and visualizing data from the Phonepe pulse Github
repository.


## Problem Statement

The Phonepe pulse Github repository contains a large amount of data related to
various metrics and statistics. The goal is to extract this data and process it to obtain
insights and information that can be visualized in a user-friendly manner.
The solution must include the following steps:
1. Extract data from the Phonepe pulse Github repository through scripting and
clone it..

2. Transform the data into a suitable format and perform any necessary cleaning
and pre-processing steps.

3. Insert the transformed data into a MySQL database for efficient storage and
retrieval.

4. Create a live geo visualization dashboard using Streamlit and Plotly in Python
to display the data in an interactive and visually appealing manner.

5. Fetch the data from the MySQL database to display in the dashboard.

6. Provide at least 10 different dropdown options for users to select different
facts and figures to display on the dashboard.


The solution must be secure, efficient, and user-friendly. The dashboard must be
easily accessible and provide valuable insights and information about the data in the
Phonepe pulse Github repository.
## Solution Approach

1. Data extraction: Clone the Github using scripting to fetch the data from the
Phonepe pulse Github repository and store it in a suitable format such as CSV
or JSON.

2. Data transformation: Use a scripting language such as Python, along with
libraries such as Pandas, to manipulate and pre-process the data. This may
include cleaning the data, handling missing values, and transforming the data
into a format suitable for analysis and visualization.

3. Database insertion: Use the "mysql-connector-python" library in Python to
connect to a MySQL database and insert the transformed data using SQL
commands.

4. Dashboard creation: Use the Streamlit and Plotly libraries in Python to create
an interactive and visually appealing dashboard. Plotly's built-in geo map
functions can be used to display the data on a map and Streamlit can be used
to create a user-friendly interface with multiple dropdown options for users to
select different facts and figures to display.

5. Data retrieval: Use the "mysql-connector-python" library to connect to the
MySQL database and fetch the data into a Pandas dataframe. Use the data in
the dataframe to update the dashboard dynamically.

6. Deployment: Ensure the solution is secure, efficient, and user-friendly. Test
the solution thoroughly and deploy the dashboard publicly, making it
accessible to users.
## Dashboard Features

The Dashboard consists of four tabs

- Home
- About
- Explore Data
- Insights

    ## Home
    The Home tab consists of information about the PhonePe and some visual information related to the PhonePe

    ## About
    The About tab consists of information image and video content about the PhonePe Pulse

    ##Explore Data
    The Explore Data consists of visual analysis on the transaction and user transaction and Registration Details over the years

    ##Insights
    Here a dropdown with 10 insights will be available and from which we can analyse the data and valuable insights 
## Features

- User Friendly
- Dynamic performance
- Colourful Theme
- Visually Attractive 
- Valuable Insights from the visuals


## Installation

Install the following packages

```bash
  pip install pandas
  pip install os
  pip install json
  pip install sql.connector
  pip install plotly.express
  pip install streamlit

```
    
## Deployment

To deploy this project run

```bash
  streamlit run phonepevisual.py
```


## Inspired From

Here is the link of the original phonepe pulse application 

[Inspired From](https://www.phonepe.com/pulse/explore/transaction/2022/4/)


## Demo

Here is the link of the demo video
https://www.linkedin.com/posts/akshaya-s-19997820a_here-is-the-demo-video-of-my-user-friendly-activity-7192817995797127168-GApY?utm_source=share&utm_medium=member_desktop

