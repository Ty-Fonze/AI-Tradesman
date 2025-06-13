import financedatabase as fd

equities = fd.Equities()

# Check the type of 'data'
print(type(equities.data))

# If it's a dict:
if isinstance(equities.data, dict):
    print(list(equities.data.keys())[:10])
    # Show info for the first ticker
    first_ticker = list(equities.data.keys())[0]
    print(f"{first_ticker}: {equities.data[first_ticker]}")
# If it's a DataFrame
elif hasattr(equities.data, 'head'):
    print(equities.data.head(10))
else:
    print("Unknown data type:", type(equities.data))