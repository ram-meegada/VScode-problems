from datetime import datetime, date
from dateutil.relativedelta import relativedelta

bought_subscription_date = date(2023,9,9)
trial_duration_completing_date = bought_subscription_date + relativedelta(months=1)
print(trial_duration_completing_date)