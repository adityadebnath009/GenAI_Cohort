import tiktoken

enc = tiktoken.encoding_for_model("gpt-4") #enc is now a tokenizer object
text = "Hello, I am Aditya Debnath."
# Encode text into tokens (IDs)
tokens = enc.encode(text)
# Print the tokens
print("Tokens:", tokens)
tokens = [9906, 11, 358, 1097, 2467, 488, 64, 1611, 11328, 589, 13]
decoded_text = enc.decode(tokens)
print("Decoded Text:", decoded_text)
 

# Decode tokens back into text