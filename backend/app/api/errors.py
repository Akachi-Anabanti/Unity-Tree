from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException
from app.api import api_v1_bp


def error_response(status_code, message=None):
    payload = {"error": HTTP_STATUS_CODES.get(status_code, "Unknown error")}
    if message:
        payload["msg"] = message
    return payload, status_code


def bad_request(message):
    return error_response(400, message)


def Unauthorized(message):
    return error_response(401, message)


def not_found(message):
    return error_response(404, message)


def forbidden(message):
    return error_response(403, message)


def internal_server_error(message):
    return error_response(message)


@api_v1_bp.errorhandler(HTTPException)
def handle_exception(e):
    return error_response(e.code)
