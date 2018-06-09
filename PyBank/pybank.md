

```python
import pandas as pd
import csv
import numpy as nb
```


```python
#import CSV file

budget = "budget_data_2.csv"

budget_df = pd.read_csv(budget)

budget_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jan-2009</td>
      <td>943690</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Feb-2009</td>
      <td>1062565</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mar-2009</td>
      <td>210079</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Apr-2009</td>
      <td>-735286</td>
    </tr>
    <tr>
      <th>4</th>
      <td>May-2009</td>
      <td>842933</td>
    </tr>
  </tbody>
</table>
</div>




```python

Total = "Total Months: " + str(len(budget_df))


```


```python
total_sum = budget_df["Revenue"].sum()

sum_revenue = "Total Revenue: $" + str(total_sum)

sum_revenue
```




    'Total Revenue: $36973911'




```python
Change = budget_df["Revenue"] - budget_df["Revenue"].shift(-1)

Change.head()
```




    0    -118875.0
    1     852486.0
    2     945365.0
    3   -1578219.0
    4     484242.0
    Name: Revenue, dtype: float64




```python
budget_df = budget_df.assign(Change=Change.values)


budget_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Revenue</th>
      <th>Change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jan-2009</td>
      <td>943690</td>
      <td>-118875.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Feb-2009</td>
      <td>1062565</td>
      <td>852486.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mar-2009</td>
      <td>210079</td>
      <td>945365.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Apr-2009</td>
      <td>-735286</td>
      <td>-1578219.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>May-2009</td>
      <td>842933</td>
      <td>484242.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
max_change = budget_df.loc[budget_df["Change"].idxmax()]
 
Date = max_change["Date"]
Change = max_change["Change"]
x = int(Change)

max = "Greatest Increase in Revenue: " + str(Date) + " ($" + str(x) + ")"
max
```




    'Greatest Increase in Revenue: May-2014 ($1947745)'




```python
min_change = budget_df.loc[budget_df["Change"].idxmin()]
 
Date = min_change["Date"]
Change = min_change["Change"]
x = int(Change)

min = "Greatest Decrease in Revenue: " + str(Date) + " ($" + str(x) + ")"
min
```




    'Greatest Decrease in Revenue: Jun-2014 ($-1645140)'




```python
avg = budget_df["Change"].mean()

avg = int(avg)

out = "Average Revenue Change: $" + str(avg)

out

```




    'Average Revenue Change: $5955'




```python
"Financial Analysis" 


```




    'Financial Analysis'




```python
print("Financial Analysis") 
print("---------------------------------------------------")

print (Total)
print (sum_revenue)
print (max)
print (min)
```

    Financial Analysis
    ---------------------------------------------------
    Total Months: 86
    Total Revenue: $36973911
    Greatest Increase in Revenue: May-2014 ($1947745)
    Greatest Decrease in Revenue: Jun-2014 ($-1645140)
    


```python



```
