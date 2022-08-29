pytest -v -s -m "sanity" --html=Report/report_customer.html testCases/ --browser chrome
rem pytest -v -s -m "sanity or regression" --html=Report/report_customer.html testCases/ --browser chrome
rem pytest -v -s -m "sanity and regression" --html=Report/report_customer.html testCases/ --browser chrome
rem pytest -v -s -m "regression" --html=Report/report_customer.html testCases/ --browser chrome
