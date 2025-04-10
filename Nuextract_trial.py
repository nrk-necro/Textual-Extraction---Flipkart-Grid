import json
from transformers import AutoModelForCausalLM, AutoTokenizer

def predict_NuExtract(model, tokenizer, text, schema, example=[]):
    # Proper formatting of the schema
    schema = json.dumps(json.loads(schema), indent=4)
    input_llm = "<|input|>\n### Template:\n" + schema + "\n"
    
    # Check if there are examples and append text properly
    for i in example:
        if i != "":
            input_llm += "### Text:\n" + text + "\n<|output|>\n"
    
    # Tokenizing the input text and moving to GPU
    input_ids = tokenizer(input_llm, return_tensors="pt", truncation=True, max_length=4000).to("cuda")
    
    # Generating the output and decoding
    output = tokenizer.decode(model.generate(**input_ids)[0], skip_special_tokens=True)
    
    # Extracting the relevant portion of the output
    return output.split("<|output|>")[1].split("<|end-output|>")[0]

# Load the model and tokenizer
model = AutoModelForCausalLM.from_pretrained("numind/NuExtract-tiny", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("numind/NuExtract-tiny", trust_remote_code=True)

# Move model to GPU
model.to("cuda")

# Set the model to evaluation mode
model.eval()

# Example text and schema
text = """A music festival featuring local bands will be held at Central Park on Saturday, July 4th, starting at 10:00 AM. Admission is free."""

schema = """
{
    "Events": {
        "Name": "",
        "Description": "",
        "Location": "",
        "Date": "",
        "Start_Time": "",
        "Admission": ""
    }
}
"""

# Call the predict function and print the prediction
prediction = predict_NuExtract(model, tokenizer, text, schema)

print(prediction)

