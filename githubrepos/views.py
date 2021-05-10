from pyramid.view import (view_config,view_defaults)
import requests as req

@view_defaults(route_name='home')
class ReposViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='home.pt')
    def home(self):
        url = "https://api.github.com/repositories"
        resp = req.get(url)
        obj=resp.json()
        return {'obj': obj}

    @view_config(route_name='repo', renderer='repo.pt')
    def repo(self):
        owner = self.request.matchdict['owner']
        repo = self.request.matchdict['repo']
        url="https://api.github.com/repos/{}/{}".format(owner,repo)
        resp = req.get(url)
        obj=resp.json()
        return obj

