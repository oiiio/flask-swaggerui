from flask import current_app
from flask import render_template_string, Blueprint, send_from_directory
import os

DIRECTORY = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_PATH = os.path.join(DIRECTORY, "templates/swagger-ui.html")


SWAGGERUI_DEFAULTS = {
    'API_AUTH': False,
    'API_AUTH_KEY': '',
    'API_KEY_AUTHORIZATION_HEADER': "api_key",
    'API_KEY_AUTHORIZATION_PREFIX': "",
    'API_KEY_AUTHORIZATION_LOCATION': "query",
    'API_KEY_SECURITY_DEFINITION_NAME': "api_key"
}


def render_swaggerui(swagger_spec_path, static_prefix="/swagger-ui-static",
                     **kwargs):
    with open(TEMPLATE_PATH) as f:
        template_string = f.read()

    config = {}
    config.update(SWAGGERUI_DEFAULTS)
    config.update(current_app.config.get_namespace('SWAGGERUI_'))

    for n, v in config.items():
        if isinstance(v, bool):
            v = str(v).lower()
        kwargs[n.lower()] = v

    return render_template_string(
        template_string, swagger_spec_path=swagger_spec_path,
        static_prefix=static_prefix, **kwargs)


def build_static_blueprint(*args, **kwargs):
    #kwargs['url_prefix'] = kwargs.get('url_prefix', "").rstrip("/") + \
    #                       "/swagger-ui"

    bp = Blueprint(*args, **kwargs)

    @bp.route('/swagger-ui-static/<path:fn>')
    def swaggerui_static(fn):
        return send_from_directory(os.path.join(DIRECTORY, "static"), fn)

    return bp
