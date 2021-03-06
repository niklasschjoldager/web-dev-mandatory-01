from bottle import error, get, redirect, run, static_file, view


############################################################
@get("/app.css")
def _():
    return static_file("/app.css", root="./styles")


############################################################
import index_get  # GET
import login_get  # GET
import logout_get  # GET
import home_get  # GET
import tweet_edit_get  # GET

import signup_post  # POST
import login_post  # POST
import tweet_create_post  # POST
import tweet_delete_post  # POST
import tweet_edit_post  # POST


############################################################
@error(404)
@view("404")
def _(error):
    return


############################################################
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")
