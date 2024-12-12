## DUO API Python Interface 

This Python module provides a simple interface to interact with the Dienst Uitvoering Onderwijs (DUO) API. It allows you to query dataset tables and retrieve data based on specific filters.

**Features:**

* **Easy Data Retrieval:** Query DUO datasets using a user-friendly function `query()`.
* **Filtering Capabilities:** Filter your results by specific columns and values using the `filters` parameter in the `query()` function. 
* **Pagination Support:** Automatically handles pagination for large datasets by iterating through pages until all results are retrieved.

**Installation:**

This module can be installed directly from this repository using pip:

```bash
pip install <your_repository_name>  
```


**Usage Example:**

```python
import duo_api

# Query the 'adressen_vo' dataset and filter by municipality code
result = duo_api.query(
    resource_id='5187f8d5-ff9c-4284-8e06-4311f0354956', 
    filters={'GEMEENTENUMMER': ['0944','0907']},  
    limit=10  # Limit results to 10 per page
)

# Print the retrieved data
for row in result:
    print(row)
```

**API Reference:**

* **`request(url)`:** Internal function that handles API requests and retrieves JSON data. Should not be called directly by users.
* **`query(**kwargs)`:** Queries a DUO API table based on the provided parameters. 
    * `resource_id`: The ID of the dataset to query (e.g., '5187f8d5-ff9c-4284-8e06-4311f0354956').
    * `filters`: A dictionary where keys are column names and values are lists of filter values for those columns.
    * `limit`: The maximum number of results to retrieve per page (optional).
* **`urlConstructer(baseUrl, **kwargs)`:** Constructs the API URL based on the base URL and provided parameters.



**Notes:**

* You will need an active internet connection to use this module.
* The DUO API documentation can be found at [https://data.duo.nl/](https://data.duo.nl/).


