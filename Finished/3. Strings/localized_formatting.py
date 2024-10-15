# Example file for Advanced Python by Joe Marini
# Localized string formatting use the locale

import locale

val1 = 123456.78

# Set the locale to the user's default.
locale.setlocale(locale.LC_ALL, '')

# Retrieve the current locale and some information
loc = locale.getlocale()
print(loc)

# Use the localeconv() function to see the settings for the locale
for k,v in locale.localeconv().items():
    print(f"{k}: {v}")

# Format the number using the locale
local_str = locale.str(val1)
print(local_str)
local_str = locale.localize(local_str, grouping=True)
print(local_str)

# Format the number for a specific locale
locale.setlocale(locale.LC_ALL, 'de_DE')
local_str = locale.str(val1)
print(local_str)

# Format the number as a currency string.
locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')
currency_string = locale.currency(val1, grouping=True)
print(currency_string)
