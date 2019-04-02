import pyarrow.parquet as pq
file_name = './safe_dataset.sample/sample/part-00000-34d9b361-ea79-42eb-82ee-9c9f9259c339-c000.snappy.parquet'

table = pq.read_table(file_name)
print(table)