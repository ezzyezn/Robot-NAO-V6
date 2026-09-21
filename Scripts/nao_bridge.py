from queue import Queue, Empty
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

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

port = int(8765)

class RobotHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/next":
            self.send_error(404)
            return
        
        data = get_next_answer()
        
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)
    
def run_server():
    server = ThreadingHTTPServer(
        ("0.0.0.0", port),
        RobotHandler,
        ) 
    print(f"Most NAO urachomiony na porcie {port}")
    server.serve_forever()
    
if __name__ == "__main__":
    answers.put("Cześć! Jestem Tebit.")
    run_server()