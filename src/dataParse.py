import sys
import bisect

dataStream = open("insight_testsuite/tests/test_1/input/itcont.txt", mode='r')
medianByZip = open("output/medianvals_by_zip.txt", mode='w')
medianBydate = open("output/medianvals_by_date.txt", mode='w')

def parse_data(data):
    data_array = data.split('|')
    data_dict = {"cmte_id": data_array[0],
                 "zip_code": data_array[10][:5],
                 "transaction_dt" : data_array[13],
                 "transaction_amt" : data_array[14],
                 "other_id" : data_array[15]}
    return data_dict

'''
def return_median(sorted_list):
    length = len(sorted_list)
    middle = length / 2
    if middle % 2 == 0:
        median = middle - 1
    else:
        median = middle
    print(sorted_list[median])
'''

sorted_list = []
for data in dataStream:
    donator_data = parse_data(data)
    print(donator_data)
