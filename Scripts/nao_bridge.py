from queue import Queue, Empty
import json

answers = Queue()

def get_next_answer():
    try:
        text = answers.get_nowait()
    except Empty:
        text = ""
    
    message = {"text": text}
    data = json.dumps(message, ensure_ascii=False)
    data = data.encode("utf-8")
    
    return data

answers.put("Czesc")

print(get_next_answer())
print(get_next_answer())