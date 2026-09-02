# Robot-NAO-V6
A repository for documenting my internship work with the NAO V6 robot, including progress reports, experiments, and project materials

## 1.Installing and setting up all components

### 1.Install Python
First, you need to install Python. Version 3.12 is recommended, but I installed Python 3.13 from the official Microsoft Store.

### 2.Install VS Code
After that, I installed Visual Studio Code from the official website. Then, I opened VS Code and installed the Python extension by Microsoft.

### 3.Install Ollahama
Now, I need to install a local AI tool on my computer. For this, I downloaded Ollama from the official website using the Windows installer.

### 4.Checking the installed components
I checked everything in CMD. I used `python --version` and `pip --version` to check Python and pip. Both commands work. Then, I used `ollama --version` to check Ollama. This command also works correctly.

### 5.Creating a working folder
I created a working folder where I will test Ollama using Python. After creating the folder, I opened it in Visual Studio Code.

### 6.Install LLM
Download the first local LLM using the command `ollama pull llama3.2:3b`. After the download is complete, run it using `ollama run llama3.2:3b`. The Llama model is now running locally, and we can chat with it. Everything works well.

### 7.Creating a Python file
Create a Python file `test_ollama.py` to work with Ollama. [Commit](https://github.com/ezzyezn/Robot-NAO-V6/commit/44fa659fd820090ff111a0ae712b9d03fab528dd)

### 8.Install Ollama package
We also install the official Ollama package for Python. To do this, run `pip install ollama` in the Visual Studio Code terminal.
