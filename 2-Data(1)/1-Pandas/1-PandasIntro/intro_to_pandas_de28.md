# Pandas

**Pandas** is a **Python Library**, specifically designed for data manipulation and analysis. It is built on top of NumPy, a scientific computing libary that provides a number of useful numberical tools.

So far in Python, we have worked with data in a few in-built datatypes like lists, strings and dictionaries. Pandas introduces a few more useful datatypes: the `Series` and `DataFrame`, which allow us to manipulate more complex tabular data (data with rows and columns).

The functionality provided by pandas is similar to SQL, we can:

- Reduce our dataset by cleverly picking only columns and rows
- Filter data
- Aggregate data
- Sort data

We can also joining multiple datasets together, reshape the data and even plot the data on a graph.

## Pandas vs. SQL

With the similarily of features, you may wonder when to use pandas over SQL and visa versa.

Pros of pandas:

- It's lightweight compared to SQL, and a much more appropriate tool for small datasets.
- The data source/target is much more flexible, your data doesn't have to already exist in a database.
  - It is very simple to load data from files, e.g. csv, excel
  - pandas has in-built tools to wrangle json and html data if you're workign with data from the web.
  - There are also in-built tools to read/write from databases.
- It integrates nicely with the rest of your Python code, so your data manipulation can be included simply as part of your Python pipeline: your ETL code can sit neatly before your ML code or data viz code in same `.py` file.
- You can leverage lots of in-built Python packages and toolign, e.g string manipulation, the datetime library, mathematical functions and ML libraries.

Cons of pandas:

- `Series` and `DataFrame` objects are stored in RAM, so your dataset is limited by the amount of RAM on your machine.
- For complex queries and aggregations, on larger datasets, SQL is much more efficient.
- Pandas does not leverage inter-table relationships like key constraints.
- The inferface is much more clunky than SQL.

## A word of warning

Once you start using pandas, you'll want to use it everywhere! While incedibly useful, the pandas package is large, and if you just need to manipulate a few 10s of 'rows' of data, considering using alternative data formats that are more lightweight e.g. dictionaries, json and yaml. Depending on your situation even 100s and 1000s of 'rows' worth of data might not warrant using pandas.

## Getting started

To get started we need to install pandas (it is included already with the Anaconda distribution), and simply import:

```python
# We typically alias pandas to the shorter 'pd'
import pandas as pd

# Sometimes it is useful to explicitly use numpy as well
import numpy as np
```
