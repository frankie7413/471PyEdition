import SimpleHTTPServer
import SocketServer
#http://stackoverflow.com/questions/19571282/using-forever-js-with-python
#ssh -i appleprivatekey.pem root@45.55.220.106
#forever start -c python server3.py
#default port for dev is 8008 prod is 8080
PORT = 8080

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

#change ip and port since i am testing on server
#quotations empty for dev 45.55.220.106
httpd = SocketServer.TCPServer(("45.55.220.106", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
