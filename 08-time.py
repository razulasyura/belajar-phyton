import time  # import time
import calendar  # import calendar

# time
waktu = time.time()
localtime = time.localtime(waktu)
formatLocalTime = time.asctime(localtime)
print "Waktu menunjukan", localtime
print "Waktu dengan format", formatLocalTime

# calendar
cal = calendar.month(2020, 1)
print "Cetak Calendar"
print cal
