import json
import pandas as pd
from vectordb.pinecone import pinecone


data_to_insert = 5000

formatting_columns = ["gender","masterCategory","subCategory","articleType","baseColour","season","year","usage","productDisplayName"]
data_frame = pd.read_csv("data/styles.csv", on_bad_lines='skip')
data_frame = data_frame.iloc[100:data_to_insert]
data_frame = data_frame.applymap(str)
data_frame['metadata'] = data_frame.apply(lambda row: json.loads(row.to_json()), axis=1)
data_frame['text_content'] = data_frame.apply(lambda row: ' :: '.join(map(str, row[formatting_columns])), axis=1)
data_frame.to_csv(f"data/sample_{data_to_insert}_items.csv")

df = data_frame
op_columns = ["id","metadata","text_content"]
list_of_rows = [row[op_columns].to_dict() for _, row in df.iterrows()]
print(list_of_rows)
pinecone.upsert_documents(documents=list_of_rows)