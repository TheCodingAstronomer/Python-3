monthConversions = {
    0: "January",
    1: "February",
    10: "March",
    100: "April",
    1000: "May",
    10000: "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions.get(100))
print(monthConversions["Sep"])
print(monthConversions.get(100000, "Not A Valid Key"))