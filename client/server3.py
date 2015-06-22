import SimpleHTTPServer
import SocketServer

PORT = 8008

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

#change ip and port since i am testing on server 
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()