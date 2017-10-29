import sys
import data_handling_functions as handle

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
    features = handle.get_data(data_dict, cmte_id, data_type)
    write_file(stream, cmte_id, data_type, features[0], features[1], features[2])
    return
