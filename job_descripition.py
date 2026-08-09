import pandas as pd


df = pd.read_csv(r"C:\Real Time Job Analytics Portal\job_descriptions.csv")


print(df.head())
print(df.info())
print("Shape:", df.shape)
print("Columns:\n", df.columns)


print("Missing Values:\n", df.isnull().sum())
print("Duplicate Rows:", df.duplicated().sum())
print(df.describe())


print("Work Type:", df["Work Type"].unique())
print("Preference:", df["Preference"].unique())
print("Job Portal:", df["Job Portal"].unique())
print("Qualifications:", df["Qualifications"].unique())
print("Country:", df["Country"].unique()[:20])
print("Job Titles:", df["Job Title"].unique()[:20])

print("Salary Sample:")
print(df["Salary Range"].head())

print("Experience Sample:")
print(df["Experience"].head())

print("Latitude Summary:")
print(df["latitude"].describe())

print("Longitude Summary:")
print(df["longitude"].describe())

print("Contact Person:")
print(df["Contact Person"].head())

print("Job Posting Date:")
print(df["Job Posting Date"].head())

df["Salary Numeric"] = (
    df["Salary Range"]
    .str.extract(r'(\d+)')
    .astype(int) * 1000
)

df["Experience Numeric"] = (
    df["Experience"]
    .str.extract(r'(\d+)')
    .astype(int)
)

df.to_csv("job_description_clean.csv", index=False)

print("Clean dataset saved successfully.")