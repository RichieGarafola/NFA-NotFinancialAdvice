![alt="NotFinancialAdvice"](../Streamlit/Resources/LandingPage.jpg)

# NFA - NotFinancialAdvice
# NFA Installation Guide


NFA is a Python Financial Analysis package that provides a single platform to access multiple ways analyze the financial markets.

Follow the steps below to install and set up NFA in your Python environment. 


**NOTE:** Make sure that you are using your conda environment that has anaconda installed. Create a new environment for this, using:

```shell
conda update anaconda
conda create -n NFA python=3.7 anaconda -y
conda activate NFA
```

Before installing the NFA dependencies, you need to install a couple of libraries. First, install the `nb_conda` package that will allow you to switch between virtual environments in Jupyter lab.

```shell
conda install -c anaconda nb_conda -y
```

Follow the next steps to install NFA and all its dependencies in your Python virtual environment.

---

1. Download the NFA library **Prophet**. 

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

2. Download the NFA library **pandas-datareader**

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

---

3. Download the NFA library **yfinance**

Gives you easy access to All financial data available on Yahoo Finance

  Example usage:
    
    import yfinance as yf

    msft = yf.Ticker("MSFT")

    # get stock info
    msft.info


```shell
pip install yfinance
```

---

4. Download the NFA library **path**

Implements path objects as first-class entities, allowing common operations on files to be invoked on those path objects directly.

```shell
pip install path
```
---

5. Download the NFA library **finta**

Common financial technical indicators implemented in Pandas. Finta supports over 80 trading indicators 

```shell
pip install finta
```
---

6. Download the NFA library **mplfinance**

matplotlib utilities for the visualization, and visual analysis, of financial data

```shell
pip install mplfinance
```
---

7. Download the NFA library **wordcloud**

A little word cloud generator in Python. 

```shell
pip install wordcloud
```
---

8. Download the NFA library **streamlit**

Streamlit’s open-source app framework is the easiest way for data scientists and machine learning engineers to create beautiful, performant apps in only a few hours! All in pure Python. All for free.

```shell
pip install streamlit
```
---

9. Download the NFA library **datetime**

This package provides a DateTime data type, as known from Zope.
Unless you need to communicate with Zope APIs, you’re probably better off using Python’s built-in datetime module.

```shell
pip install datetime
```
---

10. Download the NFA library **vaderSentiment**

VADER Sentiment Analysis. VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media, and works well on texts from other domains.

```shell
pip install vaderSentiment
```

---

11. Download the NFA library **regex**

This regex implementation is backwards-compatible with the standard ‘re’ module, but offers additional functionality.

```shell
pip install regex
```

---

12. Download the NFA library **nltk**

The Natural Language Toolkit (NLTK) is a Python package for natural language processing. NLTK requires Python 3.7, 3.8, 3.9 or 3.10.

```shell
pip install nltk
```
---

13. Download the NFA library **snscrape**

snscrape is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or searches and returns the discovered items, e.g. the relevant posts.

```shell
pip install snscrape
```

---

14. Download the NFA library **oracledb**

The python-oracledb driver allows Python 3 applications to connect to Oracle Database.

```shell
pip install oracledb
```

---

15. Download the NFA library **sklearn**

A set of python modules for machine learning and data mining.

```shell
pip install sklearn
```
---

16. Download the NFA library **tensorflow**

TensorFlow is an open source machine learning framework for everyone.

```shell
pip install tensorflow
```

---

17. Run the following commands to confirm installation of all NFA packages. Look for version numbers with at least the following versions.  

```shell
conda list prophet
conda list pandas-datareader
conda list yfinance
conda list path
conda list finta
conda list mplfinance
conda list wordcloud
conda list streamlit
conda list datetime
conda list vaderSentiment
conda list regex
conda list nltk
conda list snscrape
conda list oracledb
conda list sklearn
conda list tensorflow

```
      
      
```text
prophet                   1.1
pandas-datareader         0.10.0
yfinance                  0.1.74
path                      16.4.0
finta                     1.3.*
mplfinance                0.12.9b1
wordcloud                 1.8.2.2
streamlit                 1.11.1
datetime                  4.5.*
vadersentiment            3.3.2
regex                     2022.3.2
nltk                      3.7
snscrape                  0.4.3.20220106
hvplot                    0.8.0
sklearn                   0.0
tensorflow                2.9.1

```


---

## Troubleshooting

If you experience blank plots rendering in your Jupyter Lab preview, try the following steps:

1. First, clear your browser cache.

    - If using Chrome, you can do this by right clicking and choosing `Inspect` from the drop menu.
    
    ![clear_browser_cache1](../Images/clear_browser_cache1.PNG)

    - Next, hold down click on the browser reload button which will cause another drop down menu to appear.  From this menu select `Empty Cache and Hard Reload`.

      ![clear_browser_cache2](../Images/clear_browser_cache2.PNG)

3. Then clear the Kernel cache:

    - Click the `Kernel` drop down menu inside Jupyter Lab.  From this menu, click `Restart Kernel and Clear Outputs`.

      ![clear_kernel_cache](../Images/clear_kernel_cache.PNG)

4. After these steps are completed, re-run your notebook. 

5. If your browser is Chrome, and you continue to render blank plots after completing the previous 4 steps, try updating Chrome. Instructions for this can be found [here](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en).

If you have issues with NFA or Jupyter Lab, you may need to update your Conda environment. Follow the steps below to update the environment and then go back to the install guide to complete a fresh installation of NFA.

1. Deactivate your current Conda environment. This is required in order to update the global Conda environment. Be sure to quit any running applications such as Jupyter prior to deactivating the environment.

    ```shell
    conda deactivate
    ```

2. Update Conda.

    ```shell
    conda update conda
    ```

3. Create a fresh Conda environment to use with NFA.

    ```shell
    conda create -n NFA python=3.7 anaconda
    ```

4. Activate the new environment.

    ```shell
    conda activate NFA
    ```

5. Install the NFA dependencies following the guide above.

---
