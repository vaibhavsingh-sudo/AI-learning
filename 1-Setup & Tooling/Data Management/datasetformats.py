from datasets import load_dataset

dataset = load_dataset("wikimedia/wikipedia", "20220301.en",split="train")
dataset.to_csv("wikidata.csv")
dataset.to_json("wikidata.json")
dataset.to_parquet("wikidata.parquet")