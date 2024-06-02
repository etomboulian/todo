from flask import Flask, Blueprint

app = Flask(__name__)

# Register the SSR website bp
import server.web as web
app.register_blueprint(web.bp)

# Register the api bp
import server.api as api
app.register_blueprint(api.bp)


