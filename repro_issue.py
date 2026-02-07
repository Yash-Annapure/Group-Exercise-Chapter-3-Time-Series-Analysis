
import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

# Create synthetic daily data without frequency
dates = pd.date_range(start='2020-01-01', periods=730, freq='D')
# Drop freq to simulate the user's issue (loading from csv often doesn't set freq)
dates.freq = None 
data = np.random.randn(730)
series = pd.Series(data, index=dates)

print("Series index freq:", series.index.freq)

try:
    print("\nRunning seasonal_decompose without frequency...")
    result = seasonal_decompose(series, model='additive', period=365)
    print("Success (with potential warnings)")
except Exception as e:
    print(f"Failed: {e}")

# Fix: Set frequency
print("\nFixing frequency...")
series = series.asfreq('D')
print("Series index freq:", series.index.freq)

try:
    print("\nRunning seasonal_decompose with frequency...")
    result = seasonal_decompose(series, model='additive', period=365)
    print("Success (warnings should be gone)")
except Exception as e:
    print(f"Failed: {e}")
