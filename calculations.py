import json
import os

folder = os.path.dirname(__file__)
config_path = os.path.join(folder, "config.json")

with open(config_path, "r") as file:

    config = json.load(file)


# Calculate base pay, after tax.

def base_pay(hours_earned):

    hourly_rate = config["values"]["base_rate"] * hours_earned * config["values"]["tax"]
    
    return hourly_rate

# Calculate service charge, after tax, between an estimated minimum and maximum amount.

def service_charge(hours_earned):
    
    service_pay_min = config["values"]["min_sc"] * hours_earned * config["values"]["tax"]
    service_pay_max = config["values"]["max_sc"] * hours_earned * config["values"]["tax"]

    return service_pay_min, service_pay_max

# Calculate holiday pay this month.

def holiday_pay(holiday):

    holiday_rate = holiday * config["values"]["base_rate"] * 7

    return holiday_rate

def pay_calc(hours, holiday):

    base = float(base_pay(hours))

    service_min, service_max = service_charge(hours)

    holiday_earned = float(holiday_pay(holiday))    

    lower = base + service_min + holiday_earned
    upper = base + service_max + holiday_earned

    return lower, upper
