
### Heroes Of Pymoli Data Analysis
* % of the 53 players only have one purchase for in-game purchases..

* The game also is played by those aged 20-24 spending 3.05 per purchase whereas older player in the 35-39 range spend about $.55 more per purchase.  

* Females tend to spend $.18 more per purchase than males.


-----

# Note
* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.


```python
# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()
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
      <th>Purchase ID</th>
      <th>SN</th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Lisim78</td>
      <td>20</td>
      <td>Male</td>
      <td>108</td>
      <td>Extraction, Quickblade Of Trembling Hands</td>
      <td>3.53</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Lisovynya38</td>
      <td>40</td>
      <td>Male</td>
      <td>143</td>
      <td>Frenzied Scimitar</td>
      <td>1.56</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Ithergue48</td>
      <td>24</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>4.88</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Chamassasya86</td>
      <td>24</td>
      <td>Male</td>
      <td>100</td>
      <td>Blindscythe</td>
      <td>3.27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Iskosia90</td>
      <td>23</td>
      <td>Male</td>
      <td>131</td>
      <td>Fury</td>
      <td>1.44</td>
    </tr>
  </tbody>
</table>
</div>



## Player Count

* Display the total number of players



```python
player_count = purchase_data['SN'].value_counts()

players = len(player_count)

players
```




    576



## Purchasing Analysis (Total)

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame



```python
unique_items = purchase_data['Item ID'].value_counts()
item = (len(unique_items))
#print (len(unique_items))
avg_price =  purchase_data['Price'].mean()

#print (avg_price)

purchase = purchase_data['Purchase ID'].count()
#print (purchase)

revenue = purchase_data['Price'].sum()

#print (revenue)

summary = pd.DataFrame({'Number of Unique Items': [item],
                       'Average Price': [avg_price],
                       'Number of Purchases': [purchase],
                       'Total Revenue': [revenue]})

summary['Average Price'] = summary['Average Price'].map("${:,.2f}".format)
summary['Total Revenue'] = summary['Total Revenue'].map("${:,.2f}".format)
summary
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
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Number of Unique Items</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>$3.05</td>
      <td>780</td>
      <td>183</td>
      <td>$2,379.77</td>
    </tr>
  </tbody>
</table>
</div>



## Gender Demographics

* Run basic calculations to obtain number of unique items, average price, etc.


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame



```python
gender_count = purchase_data['Gender'].value_counts()

gender_count

#summary = pd.dataframe({'Gender': gender,
                       #'Total Count': gender_count})

```




    Male                     652
    Female                   113
    Other / Non-Disclosed     15
    Name: Gender, dtype: int64




```python
percentage = (gender_count/ purchase) * 100
print(percentage)

percentage.to_frame(name=None)
```

    Male                     83.589744
    Female                   14.487179
    Other / Non-Disclosed     1.923077
    Name: Gender, dtype: float64
    




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
      <th>Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>83.589744</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>14.487179</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.923077</td>
    </tr>
  </tbody>
</table>
</div>




```python
gender_summary = pd.DataFrame({"Percentage of Players": percentage,
                       "Total Counts": gender_count})

gender_summary['Percentage of Players'] = gender_summary['Percentage of Players'].map("{0:,.2f}".format)
gender_summary
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
      <th>Percentage of Players</th>
      <th>Total Counts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>83.59</td>
      <td>652</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>14.49</td>
      <td>113</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.92</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




## Purchasing Analysis (Gender)

* Run basic calculations to obtain purchase count, avg. purchase price, etc. by gender


* For normalized purchasing, divide total purchase value by purchase count, by gender


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


```python
avg_purchase = purchase_data.groupby(['Gender'])

avg_purchase1 = avg_purchase['Price'].mean()
#print(avg_purchase1)


total_purchase = avg_purchase['Price'].sum()
#print(total_purchase)

normal = total_purchase / gender_count

#print(normal)

genderpur_summary = pd.DataFrame({"Purchase Counts": gender_count,
                       "Average Purchase Price": avg_purchase1,
                        "Total Purchase Value": total_purchase,
                        "Normalized Totals": normal})
genderpur_summary['Average Purchase Price'] = genderpur_summary['Average Purchase Price'].map("${:,.2f}".format)
genderpur_summary["Total Purchase Value"] = genderpur_summary["Total Purchase Value"].map("${:,.2f}".format)
genderpur_summary["Normalized Totals"] = genderpur_summary["Normalized Totals"].map("${:,.2f}".format)
genderpur_summary
#gender_summary = pd.DataFrame({"Avg Purchase": avg_purchase,
                       #"Total Counts": gender_count})
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
      <th>Average Purchase Price</th>
      <th>Normalized Totals</th>
      <th>Purchase Counts</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>$3.20</td>
      <td>$3.20</td>
      <td>113</td>
      <td>$361.94</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>$3.02</td>
      <td>$3.02</td>
      <td>652</td>
      <td>$1,967.64</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>$3.35</td>
      <td>$3.35</td>
      <td>15</td>
      <td>$50.19</td>
    </tr>
  </tbody>
</table>
</div>



## Age Demographics

* Establish bins for ages


* Categorize the existing players using the age bins. Hint: use pd.cut()


* Calculate the numbers and percentages by age group


* Create a summary data frame to hold the results


* Optional: round the percentage column to two decimal points


* Display Age Demographics Table



```python
# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

pd.cut(purchase_data['Age'],age_bins, labels=group_names)

purchase_data['age range'] = pd.cut(purchase_data['Age'],age_bins, labels=group_names)

purchase_data.head()


age_count = purchase_data['age range'].value_counts()

print(age_count)

age_percentage = (age_count / players) * 100

print(age_percentage)


genderage_summary = pd.DataFrame({"Percentage of Players": age_percentage,
                       "Total Counts": age_count})
genderage_summary["Percentage of Players"] = genderage_summary["Percentage of Players"].map("{:,.2f}".format)
genderage_summary
```

    20-24    365
    15-19    136
    25-29    101
    30-34     73
    35-39     41
    10-14     28
    <10       23
    40+       13
    Name: age range, dtype: int64
    




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
      <th>Percentage of Players</th>
      <th>Total Counts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20-24</th>
      <td>63.37</td>
      <td>365</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>23.61</td>
      <td>136</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>17.53</td>
      <td>101</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>12.67</td>
      <td>73</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>7.12</td>
      <td>41</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>4.86</td>
      <td>28</td>
    </tr>
    <tr>
      <th>&lt;10</th>
      <td>3.99</td>
      <td>23</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>2.26</td>
      <td>13</td>
    </tr>
  </tbody>
</table>
</div>



## Purchasing Analysis (Age)

* Bin the purchase_data data frame by age


* Run basic calculations to obtain purchase count, avg. purchase price, etc. in the table below


* Calculate Normalized Purchasing


* Create a summary data frame to hold the results


* Optional: give the displayed data cleaner formatting


* Display the summary data frame


```python
# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]
pd.cut(purchase_data['Age'],age_bins, labels=group_names)

purchase_data['age range'] = pd.cut(purchase_data['Age'],age_bins, labels=group_names)

purchase_data.head()

app_age = purchase_data.groupby(['age range'])
avg_purchaseage = app_age['Price'].mean()
print(avg_purchaseage)

tot_purchaseage = app_age['Price'].sum()
print(tot_purchaseage)

normal_purage = tot_purchaseage / age_count

genderagepur_summary = pd.DataFrame({"Purchase Count": age_count,
                            "Average Purchase Price": avg_purchaseage, 
                           "Total Purchase Value": tot_purchaseage,
                                    "Normalized Totals": normal_purage})
genderagepur_summary["Average Purchase Price"] = genderagepur_summary["Average Purchase Price"].map("${:,.2f}".format)
genderagepur_summary["Total Purchase Value"] = genderagepur_summary["Total Purchase Value"].map("${:,.2f}".format)
genderagepur_summary["Normalized Totals"] = genderagepur_summary["Normalized Totals"].map("${:,.2f}".format)
genderagepur_summary
```

    age range
    <10      3.353478
    10-14    2.956429
    15-19    3.035956
    20-24    3.052219
    25-29    2.900990
    30-34    2.931507
    35-39    3.601707
    40+      2.941538
    Name: Price, dtype: float64
    age range
    <10        77.13
    10-14      82.78
    15-19     412.89
    20-24    1114.06
    25-29     293.00
    30-34     214.00
    35-39     147.67
    40+        38.24
    Name: Price, dtype: float64
    




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
      <th>Average Purchase Price</th>
      <th>Normalized Totals</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10-14</th>
      <td>$2.96</td>
      <td>$2.96</td>
      <td>28</td>
      <td>$82.78</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>$3.04</td>
      <td>$3.04</td>
      <td>136</td>
      <td>$412.89</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>$3.05</td>
      <td>$3.05</td>
      <td>365</td>
      <td>$1,114.06</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>$2.90</td>
      <td>$2.90</td>
      <td>101</td>
      <td>$293.00</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>$2.93</td>
      <td>$2.93</td>
      <td>73</td>
      <td>$214.00</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>$3.60</td>
      <td>$3.60</td>
      <td>41</td>
      <td>$147.67</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>$2.94</td>
      <td>$2.94</td>
      <td>13</td>
      <td>$38.24</td>
    </tr>
    <tr>
      <th>&lt;10</th>
      <td>$3.35</td>
      <td>$3.35</td>
      <td>23</td>
      <td>$77.13</td>
    </tr>
  </tbody>
</table>
</div>



## Top Spenders

* Run basic calculations to obtain the results in the table below


* Create a summary data frame to hold the results


* Sort the total purchase value column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame




```python
SN_count = purchase_data['SN'].value_counts()

SN_count

purchaseSN = purchase_data.groupby(['SN'])

avg_purchaseSN = purchaseSN['Price'].mean()
#print(avg_purchaseSN)


total_purchaseSN = purchaseSN['Price'].sum()
#print(total_purchaseSN)


topspender_summary = pd.DataFrame({"Purchase Counts": SN_count,
                       "Average Purchase Price": avg_purchaseSN,
                        "Total Purchase Value": total_purchaseSN})


topspender_sort = topspender_summary.sort_values('Total Purchase Value',ascending=False)
#topspender_sort = topspender_summary.sort_values('Purchase Counts',ascending=False)
topspender_sort['Average Purchase Price'] = topspender_sort['Average Purchase Price'].map("${:,.2f}".format)
topspender_sort["Total Purchase Value"] = topspender_sort["Total Purchase Value"].map("${:,.2f}".format)
#topspender_sort['Purchase Counts'].value_counts()

topspender_sort.head()
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
      <th>Average Purchase Price</th>
      <th>Purchase Counts</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Lisosia93</th>
      <td>$3.79</td>
      <td>5</td>
      <td>$18.96</td>
    </tr>
    <tr>
      <th>Idastidru52</th>
      <td>$3.86</td>
      <td>4</td>
      <td>$15.45</td>
    </tr>
    <tr>
      <th>Chamjask73</th>
      <td>$4.61</td>
      <td>3</td>
      <td>$13.83</td>
    </tr>
    <tr>
      <th>Iral74</th>
      <td>$3.40</td>
      <td>4</td>
      <td>$13.62</td>
    </tr>
    <tr>
      <th>Iskadarya95</th>
      <td>$4.37</td>
      <td>3</td>
      <td>$13.10</td>
    </tr>
  </tbody>
</table>
</div>



## Most Popular Items

* Retrieve the Item ID, Item Name, and Item Price columns


* Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value


* Create a summary data frame to hold the results


* Sort the purchase count column in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the summary data frame




```python
#Item_count = purchase_data['Item ID'].value_counts()

#Item_count

item = purchase_data.groupby(['Item ID', 'Item Name'])



avg_purchaseitem = item['Price'].mean()
#print(avg_purchaseitem)


total_purchaseitem = item['Price'].sum()
#print(total_purchaseitem)


topitem_summary = pd.DataFrame({"Item Price": avg_purchaseitem,
                                "Total Purchase Value": total_purchaseitem})
                              #"Purchase Count": Item_count})


topitem_summary['Item Price'] = topitem_summary['Item Price'].map("${:,.2f}".format)
topitem_summary["Total Purchase Value"] = topitem_summary["Total Purchase Value"].map("${:,.2f}".format)

topitem_summary.head()
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
      <th></th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <th>Splinter</th>
      <td>$1.28</td>
      <td>$5.12</td>
    </tr>
    <tr>
      <th>1</th>
      <th>Crucifer</th>
      <td>$3.26</td>
      <td>$9.78</td>
    </tr>
    <tr>
      <th>2</th>
      <th>Verdict</th>
      <td>$2.48</td>
      <td>$14.88</td>
    </tr>
    <tr>
      <th>3</th>
      <th>Phantomlight</th>
      <td>$2.49</td>
      <td>$14.94</td>
    </tr>
    <tr>
      <th>4</th>
      <th>Bloodlord's Fetish</th>
      <td>$1.70</td>
      <td>$8.50</td>
    </tr>
  </tbody>
</table>
</div>



## Most Profitable Items

* Sort the above table by total purchase value in descending order


* Optional: give the displayed data cleaner formatting


* Display a preview of the data frame




```python
topitem_sort = topitem_summary.sort_values('Total Purchase Value',ascending=False)

topitem_sort['Item Price'] = topitem_sort['Item Price'].map("${:,.2f}".format)
topitem_sort["Total Purchase Value"] = topitem_sort["Total Purchase Value"].map("${:,.2f}".format)

topitem_sort.head()
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
      <th></th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>178</th>
      <th>Oathbreaker, Last Hope of the Breaking Storm</th>
      <td>$4.23</td>
      <td>$50.76</td>
    </tr>
    <tr>
      <th>82</th>
      <th>Nirvana</th>
      <td>$4.90</td>
      <td>$44.10</td>
    </tr>
    <tr>
      <th>145</th>
      <th>Fiery Glass Crusader</th>
      <td>$4.58</td>
      <td>$41.22</td>
    </tr>
    <tr>
      <th>92</th>
      <th>Final Critic</th>
      <td>$4.88</td>
      <td>$39.04</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>$4.35</td>
      <td>$34.80</td>
    </tr>
  </tbody>
</table>
</div>


