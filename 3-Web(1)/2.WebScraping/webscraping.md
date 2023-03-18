# The Tools in our Python Toolset

The three tools we have come across are requests, beautiful soup, and selenium. These have their own specific purpose:
- `requests`: Enable us to make HTTP requests, and recieve the response. If the rsponse is in json, we can use the `json` package or the `.json` method and convert the response into a python-friendly objects e.g. lists and dictionaries.
- `beatufiulsoup`: Sometimes a HTTP response will be in either HTML or XML, these are difficult to pass into Python-friendly objects, so `beautifulsoup` enables us to turn the response into a `soup` which can be easily parsered with bs4 methods. E.g. We can find a particular HTML element like a header.
- `selenium`: A lot of websites will require user interaction, and/or waiting for the interesting content to load.  `selenium` allows us to automate this interaction to navigate to the desired content.

> N.B. - If we are specifiically searching for HTML table elements, pandas has a helpful method: `pd.readhtml()`.
