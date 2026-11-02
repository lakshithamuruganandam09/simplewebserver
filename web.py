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