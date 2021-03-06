# Finding Political Donors

## Introduction

This program will get data from the Federal Election Commission about political
donors using the [files found here](http://classic.fec.gov/finance/disclosure/ftpdet.shtml).
This information will help give insight as to what zip codes and on 
which dates the candiates receive their donations. The program will write two 
files `medianvals_by_zip.txt` and `medianvals_by_date.txt`. The file 
`medianvals_by_zip.txt` will treat the input data as streaming data; The script
will output to the file as the data comes in. It will organize the data by zip 
code. The file `medianvals_by_date.txt` will contain the same data but filtered
by date, contain unique values and sorted alphabetically by `cmte_id` and then 
sorted chronologically. 

## Implementation

The script is written in Python 2.7. It begins by getting the necessary fields from
the original input file. The data is then put into a dictionary with the keys
being `cmte_id`, `zip_code`, `transaction_dt`, `transaction_amt`, and `other_id`. 
The script will ignore lines that have `cmte_id`, `transaction_amt` or 
`other_id` as blank. The script will then store the parsed data into a list of 
donation data. This data is then passed to a function that will utilize a 
nested dictionary in the form of: 

```python
dict = {
    donations["cmte_id"] : { 
		donations[type_string] : {
			"total_amt": [],
			"transactions": [] 
		}
    }
}
```
This function will be used to create our data for both `medianvals_by_zip.txt` 
and `medianvals_by_date.txt` based on what was passed in for `type_string`.
Additionally, if the `type_string` passed in was `zip_code`, it'll write to the
`medianvals_by_zip.txt` immediately. After the end of parsing, the function 
will check to see if the `type_string` was `transaction_dt`. In the case that 
it is, it'll go through the data obtained from the function, filter and sort 
it, then write the results to `medianvals_by_date.txt`. Once both output files
are written to, the files are closed.
## Running

The script runs simply through `./run.sh` found in the root directory.
Additionally, if you wish to run it without the use of the script, you may run
the command 
    
	python ./src/data_parse.py <input.txt> <output1.txt> <output2.txt>

You may also run `./generate_all_files.sh` in order to automatically run the
script for all included test files in the `insight_testsuite` folder.
## Testing

The script will pass the provided test files in `insight_testsuite`. This can be
run by the following commands:


    cd insight_testsuite
    chmod 500 ./run_tests.sh
    ./run_tests.sh

The main program itself will run via `./run.sh`. It will test the input file 
found in the base directory and also output to the base directory. 
The test files include various ranges of lines of 50,000 from the FEC 2013-2014
, 2015-2016 and 2017-2018 individual contributions files.

## Comments

I wasn't quite sure what scalable meant in the sense of data engineering. I 
designed my script to be quite modular and tried to minimize redundant code by 
turning the redundancies into functions that can be called many times instead. 
I also took into consideration that the team may want to reuse the code behind 
finding `medianvals_by_zip` for later and it should be easy to call this 
function as long as it is given the correct information.

The only unit I really test is the `transaction_amt` as that's the only thing
that really needs to be tested. The rest of the data is treated as strings so
any sort of input would just be a string rather than a number. `transaction_amt`
is tested first, if it's blank then we just skip it before we ever convert it to
an integer. Since everything else can be handled perfectly fine as a string, the
script should hold up perfectly. 
