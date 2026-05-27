from pathlib import Path
import pandas as pd
import unicodedata
import re

# Defining date parsing and coercing needs:

def parse_dates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in df.columns:
        if df[col].dtype == object:
            try:
                df[col] = pd.to_datetime(df[col], errors='raise')
            except Exception:
                pass
    return df

def coerce_numeric(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = pd.to_numeric(df[col], errors='ignore')
    return df

# Input section

raw_input = str(input("Copy your raw data file's path and provide it here: "))

clean_input = str(input("Provide the path to where you'd prefer your clean file resolves to: "))

a = []
a_flag = True
while a_flag == True:
    a_input = input("Enter the name of a date column you would like to parse: ")
    a.append(a_input)
    a_continue = input("Another? Y/N: ")
    if a_continue == "N":
        a_flag = False

b = []
b_flag = True
while b_flag == True:
    b_input = input("Enter the name of a numeric column you would like to configure: ")
    b.append(b_input)
    b_continue = input("Another? Y/N: ")
    if b_continue == "N":
        b_flag = False

c = []
c_flag = True
while c_flag == True:
    c_input = input("Enter the name of a column you would prefer to drop: ")
    c.append(c_input)
    c_continue = input("Another? Y/N: ")
    if c_continue == "N":
        c_flag = False

d = {}
d_flag = True
while d_flag == True:
    key_input = input("If there is a column you'd like to rename, provide said column's current name: ")
    value_input = input("Provide the name you'd prefer the column to have: ")
    d[key_input] = value_input
    d_continue = input("Another? Y/N: ")
    if d_continue == "N":
        d_flag = False

f = []
f_flag = True
while f_flag == True:
    f_input = input("If there is a column you'd like to normalize entirely, provide such a column's name here: ")
    f.append(f_input)
    f_continue = input("Another? Y/N: ")
    if f_continue == "N":
        f_flag = False

# Configuration the end user just created:

cleaning_config = {
    "date_columns": a,
    "numeric_columns": b,
    "drop_columns": c,
    "rename_columns": d,
    "normalize_columns": f
}

# Defining how to apply said configuration:

def apply_config(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if cleaning_config["drop_columns"]:
        df = df.drop(columns=cleaning_config["drop_columns"], errors="ignore")
    if cleaning_config["rename_columns"]:
        df = df.rename(columns=cleaning_config["rename_columns"])
    for col in cleaning_config["date_columns"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
    for col in cleaning_config["numeric_columns"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def normalize_string(s: str) -> str:
    if not isinstance(s, str):
        return s
    s = unicodedata.normalize("NFKD", s)
    s = s.lower()
    s = re.sub(r"[-_/]", "", s)
    s = re.sub(r"\s+", "", s)
    s = s.strip()
    return s

def normalize_text_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    df = df.copy()
    for col in columns:
        if col in df.columns:
            df[col] = df[col].apply(normalize_string)
    return df

# Defining what the actual cleaning process will entail:

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns =(
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    df = apply_config(df)
    if cleaning_config["normalize_columns"]:
        df = normalize_text_columns(df, cleaning_config["normalize_columns"])
    df = df.drop_duplicates()
    df = df.dropna(axis=1, how='all')
    df = parse_dates(df)
    df = coerce_numeric(df)
    return df


# Defining the overview inspection that will be provided to end user:

def inspect(df: pd.DataFrame, name: str = "DataFrame") -> None:
    print(f"\n--- {name} ---")
    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.dtypes)
    print("\nMissing Values:")
    print(df.isna().sum())

# What the script will actually output:

raw_filename = raw_input
clean_filename = clean_input

print("Loading raw data...")
df_raw = pd.read_csv(raw_filename)
inspect(df_raw, name = "Raw data")
print("Applying basic cleaning steps...")
df_clean = basic_clean(df_raw)
print("Saving cleaned data...")
(df_clean).to_csv(clean_input, index=False)
print("Done.")
