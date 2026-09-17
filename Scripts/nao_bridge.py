from queue import Queue

answer = Queue()

answer.put("Cześć")

text = answer.get_nowait()

print(text)