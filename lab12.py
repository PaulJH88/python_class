countries = ["United States", "China", "Russia", "United Kingdom", "Germany", "France", "Japan", "India", "South Korea", "Saudi Arabia"]

try:
    print(countries.index("Poland"))

except Exception as e:
    print("Country not found, adding now")
    countries.insert(len(countries), "Poland")

print(countries.index("Poland"))

print(countries[3:])
countries[2] = "Kenya"
print(countries)

countries.insert(3, "Australia")
print(countries)

countries.pop(2)
print(countries)

better_countries = countries[-3:]
print(better_countries)

print(countries[0:4])