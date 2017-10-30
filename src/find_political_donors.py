import sys
import medianval_by_type_function as perform
import data_handling_functions as handle

#parse the input arguments
if len(sys.argv) != 4:
    print("Usage: python <src.py> <input.txt> <medianvals_by_zip.txt>\
            <medianvals_by_date.txt>")

#opening all relevant streams
data_stream = open(sys.argv[1], mode='r')
zip_stream = open(sys.argv[2], mode='w')
dt_stream = open(sys.argv[3], mode='w')

#will store the relevant information for the input
donation_data = []

#go through the input file and run parse_data() on each line, then add to
#donation_data list if it's a valid entry
for data in data_stream:
    parsed_data = handle.parse_data(data)
    if parsed_data["cmte_id"] != ""\
            and parsed_data["transaction_amt"] != ""\
            and parsed_data["other_id"] == "":
        donation_data.append(parsed_data)

#generates the median by zip file
perform.median_val_by(donation_data, "zip_code", zip_stream)

#generates the median by date file
test_dict = perform.median_val_by(donation_data, "transaction_dt", dt_stream)

#close the streams
zip_stream.close()
dt_stream.close()
