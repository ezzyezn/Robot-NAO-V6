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
Create a Python file `test_ollama.py` to work with Ollama. [Commit 44fa659](https://github.com/ezzyezn/Robot-NAO-V6/commit/44fa659fd820090ff111a0ae712b9d03fab528dd)

### 8.Install Ollama package
We also install the official Ollama package for Python. To do this, run `pip install ollama` in the Visual Studio Code terminal.

# 2.Testing LLM

### 1.First test
The first attempt to communicate with Ollama using Python code was successful. [Commit 25364c9](https://github.com/ezzyezn/Robot-NAO-V6/commit/25364c9f4a63638928a220a20e6facbad7fdb32a)

### 2.Second Test
In the next test, we enter a question in the terminal after starting the program. The LLM now follows the rules specified in the `content` field for the `system` role and answers only questions related to the given topic. The test was successful. [Commit a51f3b0](https://github.com/ezzyezn/Robot-NAO-V6/commit/a51f3b0081d020857cd4874ccb209efbb4cef4de), [Commit d994bb9](https://github.com/ezzyezn/Robot-NAO-V6/commit/d994bb96011788e39cd32f6c0abe9de221d7645f)
*The model does not have the required information yet, so it cannot correctly answer the questions I need. In some cases, the model may make up answers. This is expected at this stage and will be fixed later.*

### 3.Third test
In this test, I added information for the LLM to use. The test was successful. [Commit 86ca1c6](https://github.com/ezzyezn/Robot-NAO-V6/commit/86ca1c6426b24ba4dcbec7402b22f43ece93bc59)

### 4.Fourth test
I moved the information from the `school_info` variable to a separate `TXT` file. I also changed the format for sending requests to the LLM chat to make the code cleaner and easier to understand. The test was successful. [Commit 98abfab](https://github.com/ezzyezn/Robot-NAO-V6/commit/98abfaba2b6162e671f79733bbe96459beb0bd46), [Commit 8b12979](https://github.com/ezzyezn/Robot-NAO-V6/commit/8b1297968d9f93350e490b12e5602271b968295a)

#
### Latest changes:
[Commit 8b12979](https://github.com/ezzyezn/Robot-NAO-V6/commit/8b1297968d9f93350e490b12e5602271b968295a)
