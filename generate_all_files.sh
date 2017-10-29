#!/bin/bash
#Run this to generate all test files and put them in their respective
#directories

#main test
python ./src/data_parse.py ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt

#test 1
python ./src/data_parse.py ./insight_testsuite/tests/test_1/input/itcont.txt\
                            ./insight_testsuite/tests/test_1/output/medianvals_by_zip.txt\
                            ./insight_testsuite/tests/test_1/output/medianvals_by_date.txt
#test 2
python ./src/data_parse.py ./insight_testsuite/tests/test_2/input/itcont.txt\
                            ./insight_testsuite/tests/test_2/output/medianvals_by_zip.txt\
                            ./insight_testsuite/tests/test_2/output/medianvals_by_date.txt
#test 3
python ./src/data_parse.py ./insight_testsuite/tests/test_3/input/itcont.txt\
                            ./insight_testsuite/tests/test_3/output/medianvals_by_zip.txt\
                            ./insight_testsuite/tests/test_3/output/medianvals_by_date.txt

