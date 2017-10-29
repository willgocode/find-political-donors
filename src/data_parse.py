import sys
from collections import defaultdict
from collections import OrderedDict
import bisect

#parse input arguments
if len(sys.argv) != 4:
    print("Usage: python <src.py> <input.txt> <medianvals_by_zip.txt>\
        <medianvals_by_date.txt>")

#opening all relevant streams
data_stream = open(sys.argv[1], mode='r')
zip_stream = open(sys.argv[2], mode='w')
dt_stream = open(sys.argv[3], mode='w')

#grabs necessary data
def parse_data(data):
    data_array = data.split('|')
    data_dict = {"cmte_id": data_array[0],
                 "zip_code": data_array[10][:5],
                 "transaction_dt" : data_array[13],
                 "transaction_amt" : data_array[14],
                 "other_id" : data_array[15]}
    return data_dict

#returns median; rounds up if >.5, down` if <.5
def return_median(sorted_list):
    length = len(sorted_list)
    middle = length / 2
    if length % 2 == 0:
        median = (float(sorted_list[middle]) + float(sorted_list[middle - 1])) / 2
        median = int(round(median))
    else:
        median = sorted_list[middle]
    return median

#will get the [0]median, [1]# of transactions and [3]total monetary value
#and return as a list
def get_data(data_dict, cmte_id, data_type):
    return_list = []
    return_list.append(return_median(data_dict[cmte_id][data_type]["transactions"]))
    return_list.append(len(data_dict[cmte_id][data_type]["transactions"]))
    return_list.append(data_dict[cmte_id][data_type]["total_amt"][0])
    return return_list

#used to write to file. opens the appropriate stream and writes relevant data
def write_file(stream, cmte_id, data_type, median, length, total_amt):
    stream.write(cmte_id + '|' + \
                 data_type + '|' + \
                 str(median) + '|' + \
                 str(length) + '|' + \
                 str(total_amt) + "\n")
    return

#gets the features for the given cmte_id and data_type from the data_dict
def write_helper(data_dict, stream, cmte_id, data_type):
    features = get_data(data_dict, cmte_id, data_type)
    write_file(stream, cmte_id, data_type, features[0], features[1], features[2])
    return

#The following function uses this dictionary structure:
#   dict = {
#           donations["cmte_id"] : { 
#               donations[type_string] : {
#                   "total_amt": [],
#                   "transactions": [] 
#           }
#   }
#this function is cool because it can be used for either by zip code or by
#transaction date based on what's passed in type_string during the function call
def median_val_by(donation_data, type_string, stream):
    #generates the nested dictionary with a list at the end
    data_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    tuple_list = []
    for donation in donation_data:
        cmte_id = donation["cmte_id"]
        transaction_amt = donation["transaction_amt"]

        #check if the value at donation[type_string] is valid
        data_type = donation[type_string]
        if data_type == "":
            pass
        elif type_string == "zip_code" and len(data_type) != 5:
            pass
        elif type_string == "transaction_dt" and len(data_type) != 8:
            pass

        tuple_list.append((cmte_id, data_type))
        #will check to see if anything is in the list, if not: add new entry
        if len(data_dict[cmte_id][data_type]["total_amt"]) == 0:
            data_dict[cmte_id][data_type]["total_amt"].append(transaction_amt)
        else:
            current_total = int(data_dict[cmte_id][data_type]["total_amt"].pop(0))
            current_total += int(transaction_amt)
            data_dict[cmte_id][data_type]["total_amt"].append(current_total)

        #using bisect library to insert data into sorted list
        bisect.insort(data_dict[cmte_id][data_type]["transactions"], transaction_amt)

        #if it's streaming data, then write immediately
        if type_string == "zip_code":
            write_helper(data_dict, stream, cmte_id, data_type) 

    #if by date then go through and write to file
    if type_string == "transaction_dt":
        unique_list = list(set(tuple_list))
        sorted_unique_list = sorted(unique_list, key = lambda x:(x[0], x[1]))
        for tup in sorted_unique_list:
            write_helper(data_dict, stream, tup[0], tup[1])
    #return the dictionary
    return data_dict

#will store the relevant information for the input
donation_data = []

#go through the input file and run parse_data() on each line, then add to
#donation_data list
for data in data_stream:
    parsed_data = parse_data(data)
    if parsed_data["cmte_id"] != "" and parsed_data["transaction_amt"] != "" \
            and parsed_data["other_id"] == "":
        donation_data.append(parsed_data)

#generates the median by zip streaming file
median_val_by(donation_data, "zip_code", zip_stream)

#generates the median by date dictionary
median_val_by(donation_data, "transaction_dt", dt_stream)

#close the streams
zip_stream.close()
dt_stream.close()