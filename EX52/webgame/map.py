class Scene(object):

    def __init__(self, title, urlname, description, helptext):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}
        self.helptext = helptext

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)
