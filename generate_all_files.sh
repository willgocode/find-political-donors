#!/bin/bash
#Run this to generate all test files and put them in their respective
#directories

#main test
python ./src/find_political_donors.py ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt

#test 1
python ./src/find_political_donors.py ./insight_testsuite/tests/test_1/input/itcont.txt\
                           ./insight_testsuite/tests/test_1/output/medianvals_by_zip.txt\
                           ./insight_testsuite/tests/test_1/output/medianvals_by_date.txt
#test 2
python ./src/find_political_donors.py ./insight_testsuite/tests/test_2/input/itcont.txt\
                           ./insight_testsuite/tests/test_2/output/medianvals_by_zip.txt\
                           ./insight_testsuite/tests/test_2/output/medianvals_by_date.txt
#test 3
python ./src/find_political_donors.py ./insight_testsuite/tests/test_3/input/itcont.txt\
                           ./insight_testsuite/tests/test_3/output/medianvals_by_zip.txt\
                           ./insight_testsuite/tests/test_3/output/medianvals_by_date.txt
#test 4
python ./src/find_political_donors.py ./insight_testsuite/tests/test_4/input/itcont.txt\
                           ./insight_testsuite/tests/test_4/output/medianvals_by_zip.txt\
                           ./insight_testsuite/tests/test_4/output/medianvals_by_date.txt
#test 5
python ./src/find_political_donors.py ./insight_testsuite/tests/test_5/input/itcont.txt\
                           ./insight_testsuite/tests/test_5/output/medianvals_by_zip.txt\
                           ./insight_testsuite/tests/test_5/output/medianvals_by_date.txt
#test 6
python ./src/find_political_donors.py ./insight_testsuite/tests/test_6/input/itcont.txt\
                           ./insight_testsuite/tests/test_6/output/medianvals_by_zip.txt\
                           ./insight_testsuite/tests/test_6/output/medianvals_by_date.txt

