from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)


        data = toml.loads(content)
        print (data)


        name = data["tool"]["poetry"]["name"]
        description = data["tool"]["poetry"]["description"]
        dependencies = data["tool"]["poetry"]["dependencies"]
        dev_dependencies = data["tool"]["poetry"]["dev-dependencies"]


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
