
def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_url = "http://127.0.0.1:8000/complete/weibo/"
    auth_url = weibo_auth_url + "?client_id={client_id}&redirect_uri={redirect_uri}".format(client_id=3259101157, redirect_uri=redirect_url)

    return auth_url

