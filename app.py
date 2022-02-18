from bottle import error, get, redirect, run, static_file, view


############################################################
@get("/app.css")
def _():
    return static_file("app.css", root=".")


############################################################
import index_get  # GET
import signup_get  # GET
import login_get  # GET

import signup_post  # POST
import login_post  # POST

############################################################
@error(404)
@view("404")
def _(error):
    return


############################################################
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")
