workflow work {
  foreach -parallel ($i in 1..3) { 
    python.exe E:\Avarage\stress_test\start_test.py
  }
}