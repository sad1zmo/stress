$count = 15

1..$count | ForEach-Object -Parallel {python.exe E:\Avarage\stress_test\start_test.py} -ThrottleLimit $count
Get-Content E:\Avarage\stress_test\app.log -Wait -Tail 0