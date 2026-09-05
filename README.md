# Robot-NAO-V6
A repository for documenting my internship work with the NAO V6 robot, including progress reports, experiments, and project materials

# Project goal: 
Build a locally running AI assistant for the NAO V6 robot that can understand speech, answer domain-specific questions using verified information, and control selected robot actions.

# 1.Installing and setting up all components

### 1.Install Python
First, you need to install Python.Version Python 3.13 from the official Microsoft Store.

### 2.Install VS Code
After that, I installed Visual Studio Code from the official website. Then, I opened VS Code and installed the Python extension by Microsoft.

### 3.Install Ollama
Now, I need to install a local AI tool on my computer. For this, I downloaded Ollama from the official website using the Windows installer.

### 4.Checking the installed components
I checked everything in CMD. I used `python --version` and `pip --version` to check Python and pip. Both commands work. Then, I used `ollama --version` to check Ollama. This command also works correctly.

### 5.Creating a working folder
I created a working folder where I will test Ollama using Python. After creating the folder, I opened it in Visual Studio Code.

### 6.Install LLM
Download the first local LLM using the command `ollama pull llama3.2:3b`. After the download is complete, run it using `ollama run llama3.2:3b`. The Llama model is now running locally, and we can chat with it. Everything works well.

### 7.Creating a Python file
Create a Python file `test_ollama.py` to work with Ollama. 
[Commit 44fa659](https://github.com/ezzyezn/Robot-NAO-V6/commit/44fa659fd820090ff111a0ae712b9d03fab528dd)

### 8.Install Ollama package
We also install the official Ollama package for Python. To do this, run `pip install ollama` in the Visual Studio Code terminal.

# 2.Testing LLM

### 1.First test
The first attempt to communicate with Ollama using Python code was successful. 
[Commit 25364c9](https://github.com/ezzyezn/Robot-NAO-V6/commit/25364c9f4a63638928a220a20e6facbad7fdb32a)

### 2.Second Test
In the next test, we enter a question in the terminal after starting the program. The LLM now follows the rules specified in the `content` field for the `system` role and answers only questions related to the given topic. The test was successful. 
[Commit a51f3b0](https://github.com/ezzyezn/Robot-NAO-V6/commit/a51f3b0081d020857cd4874ccb209efbb4cef4de),
[Commit d994bb9](https://github.com/ezzyezn/Robot-NAO-V6/commit/d994bb96011788e39cd32f6c0abe9de221d7645f).
*The model does not have the required information yet, so it cannot correctly answer the questions I need. In some cases, the model may make up answers. This is expected at this stage and will be fixed later.*

### 3.Third test
In this test, I added information for the LLM to use. The test was successful. 
[Commit 86ca1c6](https://github.com/ezzyezn/Robot-NAO-V6/commit/86ca1c6426b24ba4dcbec7402b22f43ece93bc59)

### 4.Fourth test
I moved the information from the `school_info` variable to a separate `TXT` file. I also changed the format for sending requests to the LLM chat to make the code cleaner and easier to understand. The test was successful. 
[Commit 98abfab](https://github.com/ezzyezn/Robot-NAO-V6/commit/98abfaba2b6162e671f79733bbe96459beb0bd46), 
[Commit 8b12979](https://github.com/ezzyezn/Robot-NAO-V6/commit/8b1297968d9f93350e490b12e5602271b968295a)

### 5.Fifth test
I split the information from `school_info` into separate lines, so the program does not need to check the whole text at once. I also split the user’s question into words. This helps the program find the correct line more accurately. I used the `best_score` and `score` variables to clearly show how the search works. I also added *stop words*. They are ignored when checking the lines, so common linking words do not increase the score.
[Commit 7906c2b](https://github.com/ezzyezn/Robot-NAO-V6/commit/7906c2b4f4fafa4d49a3ed50f7b7dd4ba95d9e75),
[Commit 349be3b](https://github.com/ezzyezn/Robot-NAO-V6/commit/349be3b0d5e8b8721d93a2e37bff5e8ca4a7d6c6),
[Commit 2c9fda4](https://github.com/ezzyezn/Robot-NAO-V6/commit/2c9fda4b7952bdd322dd5fe2ea0132c118447cc6),
[Commit 3103cc4](https://github.com/ezzyezn/Robot-NAO-V6/commit/3103cc41ac5bed4111172c5762d551f5e9b56221),
[Commit 6eb9e39](https://github.com/ezzyezn/Robot-NAO-V6/commit/6eb9e39f7f6d82fbeb72c3fd9f6794bab1db67e1)

### 6.Sixth test
Now, only information that matches the user’s question is sent to the LLM. Alternative responses were also added for cases when no match is found. This prevents the model from answering unrelated questions and making up incorrect information.
[Commit a2de900](https://github.com/ezzyezn/Robot-NAO-V6/commit/a2de900fe9f1c7d0d0fb040d23cfd68a5cdc73dd),
[Commit 8ecea8f](https://github.com/ezzyezn/Robot-NAO-V6/commit/8ecea8fd3e1e108a68350c4f04b05c044980c758),
[Commit e49aba0](https://github.com/ezzyezn/Robot-NAO-V6/commit/e49aba04cbf8a083bc9830805c3326b009ba5fc5)

### 7.Seventh test
This is one of the most difficult tests. Here, we need to understand vectors and the dot product. To see how they work, I created the `test_embedding.py` and `test_similarity_scalar.py` files. They show vectors and the dot product with clear examples.
[Commit 5eb7561](https://github.com/ezzyezn/Robot-NAO-V6/commit/5eb7561a53c4244ba8a7a2cb82791b52c601ff1a),
[Commit 7f3a2e5](https://github.com/ezzyezn/Robot-NAO-V6/commit/7f3a2e5d9ec5a118ce43d02969d00b25683efa4c),
[Commit 0d771eb](https://github.com/ezzyezn/Robot-NAO-V6/commit/0d771ebc358f642878ac91a17d6f799e2442d466),
[Commit ee3bdee](https://github.com/ezzyezn/Robot-NAO-V6/commit/ee3bdeeb7b297e6ee9ba439049666f4a0dca5bac).
*If the "nomic-embed-text" model is not installed, install it using this command in CMD:* `ollama pull nomic-embed-text`
#
### Latest changes:
[Commit ee3bdee](https://github.com/ezzyezn/Robot-NAO-V6/commit/ee3bdeeb7b297e6ee9ba439049666f4a0dca5bac)
