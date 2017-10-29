#!/bin/bash
#Run this to generate all test files and put them in their respective
#directories

#main test
echo "Performing main test."
python ./src/find_political_donors.py ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt
echo "Main test complete."
#test 1
echo "Performing test_1."
python ./src/find_political_donors.py ./insight_testsuite/tests/test_1/input/itcont.txt\
                           ./insight_testsuite/tests/test_1/output/medianvals_by_zip.txt\
                           ./insight_testsuite/tests/test_1/output/medianvals_by_date.txt
echo "test_1 complete."
#test 2
echo "Performing test_2."
python ./src/find_political_donors.py ./insight_testsuite/tests/test_2/input/itcont.txt\
                           ./insight_testsuite/tests/test_2/output/medianvals_by_zip.txt\
                           ./insight_testsuite/tests/test_2/output/medianvals_by_date.txt
echo "test_2 complete."
#test 3
echo "Performing test_3."
python ./src/find_political_donors.py ./insight_testsuite/tests/test_3/input/itcont.txt\
                           ./insight_testsuite/tests/test_3/output/medianvals_by_zip.txt\
                           ./insight_testsuite/tests/test_3/output/medianvals_by_date.txt
echo "test_3 complete."
#test 4
echo "Performing test_4."
python ./src/find_political_donors.py ./insight_testsuite/tests/test_4/input/itcont.txt\
                           ./insight_testsuite/tests/test_4/output/medianvals_by_zip.txt\
                           ./insight_testsuite/tests/test_4/output/medianvals_by_date.txt
echo "test_4 complete."
#test 5
echo "Performing test_5."
python ./src/find_political_donors.py ./insight_testsuite/tests/test_5/input/itcont.txt\
                           ./insight_testsuite/tests/test_5/output/medianvals_by_zip.txt\
                           ./insight_testsuite/tests/test_5/output/medianvals_by_date.txt
echo "test_5 complete."
#test 6
echo "Performing test_6."
python ./src/find_political_donors.py ./insight_testsuite/tests/test_6/input/itcont.txt\
                           ./insight_testsuite/tests/test_6/output/medianvals_by_zip.txt\
                           ./insight_testsuite/tests/test_6/output/medianvals_by_date.txt
echo "test_6 complete."
