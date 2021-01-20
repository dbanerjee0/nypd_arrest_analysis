import pandas as pd


df = pd.read_csv('nypd-arrest-data-2018-1.csv')

# 1. Offence descriptions : Top 10 in descending order, if any.
if df.empty:
    print("ERROR: No offences found.")
    exit(0)
if "OFNS_DESC" not in df.columns.values.tolist():
    print("ERROR: Cannot find column-name: 'OFNS_DESC'")
    exit(0)
offences_counts = df['OFNS_DESC'].value_counts(ascending=False, dropna=True)
offences_top_10 = offences_counts.head(10)
print(offences_top_10)
if len(offences_top_10.index) < 10:
    print("Less than 10 offences found.")

# 2. Export user query of subset of Offences, if found.
offence_description_mask = str(input("Enter full or part of an offence description (the search is case sensitive): "))
print("Look for offences containing: " + offence_description_mask)
df['OFNS_DESC'].fillna('', inplace=True)  # Replace any null values in column 'OFNS_DESC', with an empty string.
offences_subset = df[df['OFNS_DESC'].str.contains(offence_description_mask)]
print("Records found: " + str(len(offences_subset.index)))
if offences_subset.empty:
    print("-- Zero records found; no .CSV file output.")
else:
    offences_subset.to_csv('nypd_offences_query_subset.csv', index=False)
    print("++ Saved to .CSV file: 'nypd_offences_query_subset.csv'.")
