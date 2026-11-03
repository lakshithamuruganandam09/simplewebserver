# EX01 Developing a Simple Webserver
## Date:26/09/26

## AIM:
To develop a simple webserver to serve html pages and display the Windows Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>Sample Web Page</title>
    </head>
    <body>
   	<table border="3" cellspacing="10" cellpadding="20">
	<caption>lakshitha M(26018363)</caption>
		<tr bgcolor="cyan">
			<th>S.No.</th>
			<th>device type</th>
			<th>device info</th>
			<th>description</th>
		</tr>
		<tr>
			<td>1</td>
			<td>laptop</td>
			<td>device name</td>
			<td>TL15-53M-G2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>LAPTOP</td>
            <td>pricessor</td>
            <td>Intel(R)Core(TM)5 210H(2.20GHz)</td>
		    
		</tr>
        <tr> 
            <td>3</td>
            <td>laptop</td>
            <td>Installed RAM</td>
            <td>16.0GB(15.7)GB usable</td>
        </tr>
	</table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()

## OUTPUT:

<img width="1920" height="1080" alt="Screenshot (21)" src="https://github.com/user-attachments/assets/0c0f8fa3-66ef-427c-9bb2-e23fdee809f6" />
<img width="1920" height="1080" alt="Screenshot (22)" src="https://github.com/user-attachments/assets/f54bba8f-a311-4758-90e0-e702661d515f" />


## RESULT:
The program for implementing simple webserver is executed successfully.
