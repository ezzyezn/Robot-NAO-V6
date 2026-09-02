import ollama ##import the ollama module

response = ollama.chat( ## call the chat function from the ollama module
    model="llama3.2:3b", ## name of the model we will use
    messages=[
        {"role": "user", ## role of the message sender, this role a standard role for user messages
         "content": "Hello, how are you?"}, ## The message we send to the model
    ])
print(response['message']['content']) ## print the response from the model