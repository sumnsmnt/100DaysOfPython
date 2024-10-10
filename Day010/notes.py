# ##### Funtions with Outputs #####

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "Please enter your name"
#     formated_f_name = f_name.title()
#     formted_l_name = l_name.title()
#     # print(f"{formated_f_name} {formted_l_name}")
#     return f"{formated_f_name} {formted_l_name}"

# # format_name("SUMAN", "samanta")
# # format_string = format_name("SUMAN", "samanta")
# format_string = format_name(input("What is your first name? "), input("What is your last name? "))
# print(format_string)


############## Days in Month ##############
# Create a function called days_in_month() which will take a year and a month as inputs.
# And it will use this info to work out the number of days in the month, then return 
# that as output. Keep in mind of leap year as well.

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_months(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month -= 1
    if is_leap_year(year):
        month_days[1] = 29
    return month_days[month]

year = int(input("Enter the year: "))
month = int(input("Enter a month: "))
days = days_in_months(year, month)
print(days)