import json
import pandas as pd
from vectordb.pinecone import pinecone


formatting_columns = ["gender","masterCategory","subCategory","articleType","baseColour","season","year","usage","productDisplayName"]
data_frame = pd.read_csv("data/styles.csv", on_bad_lines='skip')
data_frame = data_frame.head(10)
data_frame = data_frame.applymap(str)
data_frame['metadata'] = data_frame.apply(lambda row: json.loads(row.to_json()), axis=1)
data_frame['text_content'] = data_frame.apply(lambda row: ' :: '.join(map(str, row[formatting_columns])), axis=1)
print(data_frame)
data_frame.to_csv("data/sample_10_items.csv")

df = data_frame
op_columns = ["id","metadata","text_content"]
list_of_rows = [row[op_columns].to_dict() for _, row in df.iterrows()]

pinecone.upsert_documents(documents=list_of_rows)


