from bottle import request, abort


def abort_if_not_authorized():
    username = request.get_cookie("account", secret='spiss-project')
    if not username:
        abort(401, "Not Authenticated !")
