import sys
from collections import defaultdict
import bisect

data_stream = open("insight_testsuite/tests/test_1/input/itcont.txt", mode='r')
zip_stream = open("output/medianvals_by_zip.txt", mode='w')
dt_stream = open("output/medianvals_by_date.txt", mode='w')

def parse_data(data):
    data_array = data.split('|')
    data_dict = {"cmte_id": data_array[0],
                 "zip_code": data_array[10][:5],
                 "transaction_dt" : data_array[13],
                 "transaction_amt" : int(data_array[14]),
                 "other_id" : data_array[15]}
    return data_dict

def return_median(sorted_list):
    length = len(sorted_list)
    middle = length / 2
    if length % 2 == 0:
        median = (float(sorted_list[middle]) + float(sorted_list[middle - 1])) / 2
        median = int(round(median))
    else:
        median = sorted_list[middle]
    return median

def write_file(stream, cmte_id, data_type, median, length, total_amt):
    stream.write(cmte_id + '|' + \
                 data_type + '|' + \
                 str(median) + '|' + \
                 str(length) + '|' + \
                 str(total_amt) + "\n")
    return

#   dict = {
#           donations["cmte_id"] : { 
#               donations[type_string] : [donations["transaction_amt"]] 
#           }
#   }
def median_val_by(donation_data, type_string, stream):
    data_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for donation in donation_data:
        cmte_id = donation["cmte_id"]
        data_type = donation[type_string]
        transaction_amt = donation["transaction_amt"]
        if len(data_dict[cmte_id][data_type]["total_amt"]) == 0:
            data_dict[cmte_id][data_type]["total_amt"].append(transaction_amt)
        else:
            current_total = data_dict[cmte_id][data_type]["total_amt"].pop(0)
            current_total += transaction_amt
            data_dict[cmte_id][data_type]["total_amt"].append(current_total)
        bisect.insort(data_dict[cmte_id][data_type]["transactions"], transaction_amt)
        median = return_median(data_dict[cmte_id][data_type]["transactions"])
        length = len(data_dict[cmte_id][data_type]["transactions"])
        if type_string == "zip_code":
            total_amt = data_dict[cmte_id][data_type]["total_amt"][0]
            write_file(stream, cmte_id, data_type, median, length, total_amt)
    if type_string == "transaction_dt":
        for key in data_dict:
            for secondary_key in data_dict[key]:
                total_amt = data_dict[key][secondary_key]["total_amt"][0]
                median = \
                return_median(data_dict[key][secondary_key]["transactions"])
                length = len(data_dict[key][secondary_key]["transactions"])
                write_file(stream, key, data_type, median, length, total_amt)
    return data_dict

donation_data = []
for data in data_stream:
    parsed_data = parse_data(data)
    if parsed_data["cmte_id"] != "" and parsed_data["transaction_amt"] != "" \
            and parsed_data["other_id"] == "":
        donation_data.append(parsed_data)

median_val_by(donation_data, "zip_code", zip_stream)
median_val_by(donation_data, "transaction_dt", dt_stream)

zip_stream.close()
dt_stream.close()
