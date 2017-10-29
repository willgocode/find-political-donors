#!/bin/bash
#
python ./src/data_parse.py ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt

#uncomment the following to run tests and generate other files
'
python ./src/data_parse.py ./insight_testsuite/tests/test_1/input/itcont.txt\
                            ./insight_testsuite/tests/test_1/output/medianvals_by_zip.txt\
                            ./insight_testsuite/tests/test_1/output/medianvals_by_date.txt
python ./src/data_parse.py ./insight_testsuite/tests/test_2/input/itcont.txt\
                            ./insight_testsuite/tests/test_2/output/medianvals_by_zip.txt\
                            ./insight_testsuite/tests/test_2/output/medianvals_by_date.txt
python ./src/data_parse.py ./insight_testsuite/tests/test_3/input/itcont.txt\
                            ./insight_testsuite/tests/test_3/output/medianvals_by_zip.txt\
                            ./insight_testsuite/tests/test_3/output/medianvals_by_date.txt
'