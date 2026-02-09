# Group Exercise – Chapter 3: Time Series Analysis

## 👥 Group Members

| Name | Matriculation Number | Role |
|------|----------------------|------|
| Arya Shinde | 100006646 | Co-Ordinator |
| Mirang Bhandari | 100007049 | Team Member |
| Yash Annapure | 100006547 | Team Member |
| Anushka Sawant | 100006644 | Team Member | 

## 📋 Overview
Comprehensive analysis of time series data using classical statistical methods. This project demonstrates key techniques for time series analysis including visualization, decomposition, trend estimation, and forecasting using real-world temperature data.

## 📊 Dataset
**Source:** Daily Minimum Temperatures in Melbourne
- **Link:** [Daily Minimum Temperatures Dataset](https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv)
- **Time Period:** 1981-1990 (10 years)
- **Frequency:** Daily measurements
- **Variable:** Minimum temperature in degrees Celsius (°C)
- **Records:** 3,650 observations

## 🎯 Project Objectives
This exercise explores fundamental time series analysis concepts:
1. Understand time series characteristics and visualization
2. Decompose time series into trend, seasonal, and residual components
3. Estimate trends using moving averages
4. Build predictive models using autoregressive (AR) methods
5. Evaluate forecast performance on out-of-sample data

## 📖 Notebook Contents

### Section 1: Plotting the Time Series
- Load the Melbourne temperature dataset
- Create visualization of raw time series data
- Identify patterns, trends, and seasonality visually
- **Key Insight:** Observe the clear seasonal pattern with annual cycles

### Section 2: Time Series Decomposition
- Apply seasonal decomposition (additive model)
- Period: 365 days (annual seasonality)
- Components extracted:
  - **Trend:** Long-term movement in temperatures
  - **Seasonal:** Regular annual cycles
  - **Residual:** Irregular noise/remainder
- **Visualization:** Four-panel plot showing all components

### Section 3: Trend Estimation using Moving Average
- Calculate 30-day moving average
- Smooth raw data to isolate trend
- **Method:** Rolling window with window size = 30 days
- Overlay original and smoothed series
- **Use Case:** Identify underlying trend separated from noise

### Section 4: Autoregressive (AR) Forecasting Model
- **Data Split:** 
  - Training: 9 years (first 3,285 observations)
  - Testing: 1 year (last 365 observations)
- **Model:** AutoReg with 7-day lag
- **Rationale:** 7-day lag captures weekly patterns in temperature
- **Forecast:** 1-year ahead predictions on test set
- **Metrics:** Visual comparison of actual vs predicted values

### Section 5: Results Visualization
- Side-by-side comparison of actual vs forecasted values
- Temporal plot showing forecast accuracy
- **Observations:** Assess model performance and residual patterns

## 🛠 Technologies & Dependencies

### Core Libraries
- **pandas** (>=1.0.0): Data manipulation and analysis
- **numpy** (>=1.18.0): Numerical computing
- **matplotlib** (>=3.0.0): Data visualization
- **seaborn** (>=0.11.0): Statistical data visualization

### Statistical & ML Libraries
- **scikit-learn** (>=0.24.0): Machine learning utilities
- **statsmodels** (>=0.14.6): Statistical modeling and time series analysis

### Environment
- **Python:** 3.13
- **Package Manager:** pip or uv

## 📦 Installation & Setup

### Option 1: Using pip (Virtual Environment Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn "statsmodels>=0.14.6"
```

### Option 2: Using uv (Faster alternative)
```bash
# Install dependencies
uv pip install pandas numpy matplotlib seaborn scikit-learn "statsmodels>=0.14.6"
```

## 🚀 How to Run the Project

### Running the Jupyter Notebook
1. **Install Jupyter:**
   ```bash
   pip install jupyter notebook
   ```

2. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

3. **Open the notebook:**
   - Navigate to the project directory
   - Click on `Group Exercise – Chapter 3 Time Series Analysis.ipynb`
   - Run cells sequentially (Shift + Enter) or use Run All

### Running via Python Script
```bash
# Extract and run notebook code as Python script
python main.py
```

## 📁 Project Structure
```
Group-Exercise-Chapter-3-Time-Series-Analysis/
├── Group Exercise – Chapter 3 Time Series Analysis.ipynb  # Main analysis notebook
├── main.py                                                 # Python entry point
├── pyproject.toml                                          # Project configuration
├── uv.lock                                                 # Dependency lock file
├── .python-version                                         # Python version (3.13)
└── README.md                                               # This file
```

## 💡 Key Concepts & Learnings

### Time Series Decomposition
Separating a time series into three components helps understand underlying patterns:
- **Trend:** General direction of movement over time
- **Seasonality:** Regular, repeating patterns (weekly, monthly, yearly)
- **Residual:** Random fluctuations after removing trend and seasonality

### Moving Average
- Simple smoothing technique to estimate trend
- Reduces noise while preserving signal
- 30-day window balances smoothness vs responsiveness

### Autoregressive Models (AR)
- Assumes current value depends on past values
- AR(7) uses past 7 days to predict today's value
- Useful for capturing autocorrelation in time series
- Limited for long-term forecasting but good for short-term

### Evaluation
- Visual inspection of forecast vs actual
- Residual analysis (should appear random)
- Metrics: MAE, RMSE, MAPE (can be added for enhancement)

## 🔍 Results & Findings

### Main Observations:
1. **Seasonality:** Clear annual pattern with temperature cycles
2. **Trend:** Long-term mean appears relatively stable
3. **Forecast Performance:** AR(7) captures short-term dynamics reasonably well
4. **Forecast Limitations:** Pure AR model struggles with seasonal turning points

### Potential Improvements:
- SARIMA (Seasonal ARIMA) for seasonal models
- ARIMA with exogenous variables (humidity, pressure)
- Machine learning models (LSTM, Prophet)
- Ensemble methods combining multiple models

## 📚 References & Further Reading

### Time Series Books:
- "Forecasting: Principles and Practice" by Hyndman & Athanasopoulos
- "Time Series Analysis and Its Applications" by Shumway & Stoffer

### Library Documentation:
- [statsmodels Time Series](https://www.statsmodels.org/stable/tsa.html)
- [pandas Time Series](https://pandas.pydata.org/docs/user_guide/timeseries.html)
- [scikit-learn](https://scikit-learn.org/)

### Dataset Source:
- [Jason Brownlee's Datasets](https://github.com/jbrownlee/Datasets)

## 📝 Notes for Users

1. **Data Download:** The notebook downloads data directly from GitHub, so internet connection is required on first run
2. **Reproducibility:** Set random seeds if using stochastic models
3. **Customization:** Easily modify window sizes, lags, and time periods for different analysis
4. **Error Handling:** Add try-except blocks for production use
