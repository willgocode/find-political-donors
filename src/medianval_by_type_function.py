import bisect
from collections import defaultdict, OrderedDict
import write_functions as writer

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
        transaction_amt = int(donation["transaction_amt"])

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
            current_total = data_dict[cmte_id][data_type]["total_amt"].pop(0)
            current_total += transaction_amt
            data_dict[cmte_id][data_type]["total_amt"].append(current_total)

        #using bisect library to insert data into sorted list
        bisect.insort(data_dict[cmte_id][data_type]["transactions"], transaction_amt)

        #if it's streaming data, then write immediately
        if type_string == "zip_code":
            writer.write_helper(data_dict, stream, cmte_id, data_type) 

    #if by date then go through and write to file
    if type_string == "transaction_dt":
        unique_list = list(set(tuple_list))
        sorted_unique_list = sorted(unique_list, key = lambda x:(x[0], x[1]))
        for tup in sorted_unique_list:
            writer.write_helper(data_dict, stream, tup[0], tup[1])
    #return the dictionary
    return data_dict
