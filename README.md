This library provides python Flask utilities and static assets for rendering Swagger UI.

# Flask settings
Any config settings starting with `SWAGGERUI_` will get added as a template variable.  For example, 
you can set the setting `SWAGGERUI_API_AUTH` to 'true', and the `{{api_auth}}` template variable will
get set to 'true'.

## Variables

Variable               | Type       | Description
-----------------------|------------|-----------------------------
SWAGGERUI_API_AUTH     | true/false | Enable API Key auth
SWAGGERUI_API_AUTH_KEY | string     | Optional value of the api key if you want to pre-fill in the input box.
SWAGGERUI_API_KEY_AUTHORIZATION_HEADER | string | Header used for authorization (aka, 'Authorization')
SWAGGERUI_API_KEY_AUTHORIZATION_PREFIX | string | Optional prefix to the authorization header value (i.e. 'Bearer ')
SWAGGERUI_API_KEY_AUTHORIZATION_LOCATION | string | Location of the the header.  Defaults to 'header' but can also be 'query', etc
SWAGGERUI_API_KEY_SECURITY_DEFINITION_NAME | string | The name of the OpenAPI SecurityDefinition section in your swagger json/yaml

# Example

```python
from flask import Flask, jsonify

from flask_swaggerui import render_swaggerui, build_static_blueprint

app = Flask(__name__)


@app.route('/')
def root():
    return render_swaggerui(swagger_spec_path="/spec")


@app.route('/spec')
def spec():
    return jsonify({"some swagger": "spec stuff"})


# Adds static assets for swagger-ui to path
app.register_blueprint(build_static_blueprint("swaggerui", __name__))

app.run(port=8080, debug=True)
```
