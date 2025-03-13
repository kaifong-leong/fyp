with open("results.csv", "r", encoding="utf-8") as f:
    for line in f:
        # Look for 'FS_KEMs' in the raw text of the line
        if 'FS' in line:
            print(repr(line))
# import pandas as pd

# df = pd.read_csv("results_cloudflare.com.csv")  # or specify header, quotechar, etc., as needed
# print(df.columns)
# print(df.head(10))
