# NFA - NotFinancialAdvice
# project3 Installation Guide


project3 is a Python time series package that provides a single platform to access multiple time series packages, including prophet, … etc.
Follow the steps below to install and set up Project3 in your Python environment. 


**NOTE:** Make sure that you are using your conda environment that has anaconda installed. Create a new environment for this, using:

```shell
conda update anaconda
conda create -n project3 python=3.7 anaconda -y
conda activate project3
```

Before installing the project3 dependencies, you need to install a couple of libraries. First, install the `nb_conda` package that will allow you to switch between virtual environments in Jupyter lab.

```shell
conda install -c anaconda nb_conda -y
```

Follow the next steps to install project3 and all its dependencies in your Python virtual environment.

---

1. Download the project3 library **Prophet**. 
*from prophet import Prophet*

Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well

Example usage:

      from prophet import Prophet
      
      m = Prophet()
      
      m.fit(df)  # df is a pandas.DataFrame with 'y' and 'ds' columns
      
      future = m.make_future_dataframe(periods=365)
      
      m.predict(future)


```shell
pip install prophet
```

---

2. Download the project3 library **pandas-datareader**
*import pandas_datareader as pdr*

Pandas Datareader is a Python package that allows us to create a pandas DataFrame object by using various data sources from the internet. It is popularly used for working with realtime stock price datasets. Some popular data sources available on the internet including:
- Yahoo Finance
- Google Finance
- Morningstar
- IEX
- Robinhood
- Engima
- Quandl
- FRED
- World Bank
- OECD and many more.
Some documentation can be found below:


https://pydata.github.io/pandas-datareader/py-modindex.html

```shell
pip install pandas-datareader
```

3. Download the project3 library **yfinance**
gives you easy access to financial data available on Yahoo Finance


```shell
pip install yfinance
```


4. Download the project3 library **yahoofinancials**

```shell
pip install yahoofinancials
```
A python module that returns stock, cryptocurrency, forex, mutual fund, commodity futures, ETF, and US Treasury financial data from Yahoo Finance.



5. Download the project3 library **path**
implements path objects as first-class entities, allowing common operations on files to be invoked on those path objects directly.

```shell
pip install path
```


6. Download the project3 library **finta**
Common financial technical indicators implemented in Pandas. Finta supports over 80 trading indicators 



```shell
pip install finta
```


7. Download the project3 library **mplfinance**
matplotlib utilities for the visualization, and visual analysis, of financial data


```shell
pip install mplfinance
```

8. Download the project3 library **wordcloud**
A little word cloud generator in Python. 

```shell
pip install wordcloud
```


8. Run the following commands to confirm installation of all project3 packages. Look for version numbers with at least the following versions.  

```shell
conda list prophet
conda list pandas-datareader
conda list yfinance
conda list path
conda list finta
```
      
      
      
      
      
      
      
      

```text
prophet                   1.1
pandas-datareader         0.10.0
```


---

## Troubleshooting

If you experience blank plots rendering in your Jupyter Lab preview, try the following steps:

1. First, clear your browser cache.

    - If using Chrome, you can do this by right clicking and choosing `Inspect` from the drop menu.

      <img width=400 src=Images/clear_browser_cache1.PNG alt='clear_browser_cache1'><br>
      <br>

    - Next, hold down click on the browser reload button which will cause another drop down menu to appear.  From this menu select `Empty Cache and Hard Reload`.

      <img width=400 src=Images/clear_browser_cache2.PNG alt='clear_browser_cache2'><br>
      <br>

3. Then clear the Kernel cache:

    - Click the `Kernel` drop down menu inside Jupyter Lab.  From this menu, click `Restart Kernel and Clear Outputs`.

      <img width=400 src=Images/clear_kernel_cache.PNG alt='clear_kernel_cache'><br>
      <br>

4. After these steps are completed, re-run your notebook. 

5. If your browser is Chrome, and you continue to render blank plots after completing the previous 4 steps, try updating Chrome. Instructions for this can be found [here](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en).

If you have issues with project3 or Jupyter Lab, you may need to update your Conda environment. Follow the steps below to update the environment and then go back to the install guide to complete a fresh installation of project3.

1. Deactivate your current Conda environment. This is required in order to update the global Conda environment. Be sure to quit any running applications such as Jupyter prior to deactivating the environment.

    ```shell
    conda deactivate
    ```

2. Update Conda.

    ```shell
    conda update conda
    ```

3. Create a fresh Conda environment to use with project3.

    ```shell
    conda create -n project3 python=3.7 anaconda
    ```

4. Activate the new environment.

    ```shell
    conda activate project3
    ```

5. Install the project3 dependencies following the guide above.

---
