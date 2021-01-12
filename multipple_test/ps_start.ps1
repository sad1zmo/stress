$count = 3

1..$count | ForEach-Object -Parallel {python.exe D:\stress\multipple_test\start_test.py} -ThrottleLimit $count
