import sys

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
