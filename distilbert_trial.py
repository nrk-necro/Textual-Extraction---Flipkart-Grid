from transformers import DistilBertTokenizer, DistilBertModel
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained("distilbert-base-uncased")
text = "Today is the twelveth of June. Today is harry's birthday"
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
print(output)
