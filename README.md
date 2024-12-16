
<img src="https://mjconroy.com/wp-content/uploads/2023/04/ATU-Logo.png" width="250" height="150">



# **Higher Diploma in Computing: Data Analytics**

### **Module: Programming for Data Analytics**
***

**1.  Assignment 2: Weather**
-   Plot dry bulb temperature vs time using a Jupyter notebook. 

**2.  Assignment 3: Domains**
-   Create a pie chart of email domains from the csv file using the url provided.

**3.  Assignment 5: Risk**
-   Write a program that simulates 1000 individual battle rounds in Risk.
-   Create a full series of rounds for armies of arbitary sizes, until one side is wiped out. 

**4. Assignment 6: Weather Knock Airport**
-   Plot temperature, mean temperature each day and mean temperature each month from the csv file using the url provided. 
-   Plot windspeed, rolling windspeed over 24 hours, max windspeed per day and monthly mean of the daily max windspeeds.

***


### Method overview:
Data Processing and analysis:

-   Jupyter notebook: open source web application used for python coding in real time, text and visualisations. 


-   Pandas: open-source python library built on top of NumPy used for data manipulation and analysis. 
    -    The CSV datasets were loaded into a pandas dataFrame using ```pd.read_csv()```. The data was cleaned using methods like  ```dropna()``` to remove missing values.  `groupby()` splits data into groups and allowed aggregation of data using mean() etc.
    -    For time-series analysis, the pandas datetime function was used to process dates and times. `pd.to_datetime()` used to convert string dates into datetime objects. 
    
-   Data Visualisation: Matplotlib: python library used to create plots to display the data graphically. 

***




