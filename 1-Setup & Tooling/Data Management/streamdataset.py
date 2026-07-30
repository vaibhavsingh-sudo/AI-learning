from datasets import load_dataset

dataset = load_dataset("wikimedia/wikipedia", "20220301.en",streaming=True,split="train")
for i, example in enumerate(dataset):
    print(example["title"])
    if i>=4:
        break   