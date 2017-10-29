# About
The main driver script is `find_political_donors.py`. 

`data_handling_functions.py` will contain:

```
parse_data: function used to pick out CMTE_ID, ZIP_CODE, TRANSACTION_DT, 
TRANSACTION_AMT and OTHER_ID from input file and return the values as a dictionary.
```
```
return_median: function used to get the running median from a dictionary. Will round 
up if the median ends in .5 or higher and round down to the nearest number otherwise.
```
```
get_data: function used to get the features based on whether the function being run is
medianvals_by_zip or medianvals_by_date. It will get the transaction list, number of 
transactions, total amount of transactions and the median. It will return a list of 
these features.
```

`write_functions.py` will contain:
```
write_file: uesd to write one line to the appropriate stream given the data it needs 
to output.
```
```
write_helper: will be the main function to call when you want to write a line to 
the stream. It will automatically get the data from the get_data function and 
run the write_file function to commit the results.
```

`medianval_by_type_function.py` will contain:
```
median_val_by: this function will do all the heavy lifting of the program. It will 
detect if it's filtering by transactions or by zip codes and then return a dictionary
of the data at the end. Additionally it will write to the appropriate stream based on
what type_string it is given.
```