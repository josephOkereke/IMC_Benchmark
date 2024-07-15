import duckdb

# Connect to DuckDB
con = duckdb.connect()

# Load the tpch extension
con.execute("INSTALL tpch")
con.execute("LOAD tpch")

# Generate TPC-H data with a scale factor of 1
con.execute("CALL dbgen(sf=1)")

# List of TPC-H tables
tpch_tables = [
    'customer',
    'lineitem',
    'nation',
    'orders',
    'part',
    'partsupp',
    'region',
    'supplier'
]

# Save each table to a Parquet file
for table in tpch_tables:
    con.execute(f"COPY {table} TO '{table}.parquet' (FORMAT PARQUET)")
