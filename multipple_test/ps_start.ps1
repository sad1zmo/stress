$count = 10

1..$count | ForEach-Object -Parallel {python.exe E:\Avarage\stress_test\start_test.py} -ThrottleLimit $count
