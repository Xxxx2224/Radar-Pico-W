import socket

led_state = False

html = """<!DOCTYPE html><html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}
.buttonGreen { background-color: #4CAF50; border: 2px solid #000000;; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; }
.buttonRed { background-color: #D11D53; border: 2px solid #000000;; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; }
text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
</style></head>
<body><center><h1>Control Panel</h1></center><br><br>
<center> <a href="/?led=on" class="buttonGreen">LED ON</a>
<br><br>
<center> <a href="/?led=off" class="buttonRed">LED OFF</a>
<br><br>
<p>%s<p></body></html>
"""

def handle_request(request):
    global led_state
    response = ""
    if 'led=on' in request:
        led_state = True
        response = "LED is ON"
    elif 'led=off' in request:
        led_state = False
        response = "LED is OFF"
    return html % response

def run_server():
    addr = ('0.0.0.0', 8000)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(addr)
    s.listen(1)
    print('Server is running at addr')
    
    while True:
        conn, addr = s.accept()
        print('Connected to', addr)
        request = conn.recv(1024).decode()
        print("Request:")
        print(request)
        
        response = handle_request(request)
        
        conn.sendall('HTTP/1.1 200 OK\nContent-Type: text/html\n\n'.encode() + response.encode())
        conn.close()

if __name__ == "__main__":
    run_server()
