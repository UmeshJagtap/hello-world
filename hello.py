# Display Grettings

print("Hello, World")
print("__ Good Morning __")

# Display Time
from pytz import timezone
from datetime import datetime

ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
print(ind_time)