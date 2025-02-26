
"""A class to manage transitions from one scene to another."""

class SceneManagerDict:
    def __init__(self):
        self._scene_dict = {}
        self._current_scene = None
        self._next_scene = None
        # This is a safety to ensure that calling
        # next() twice in a row without calling set_next_scene()
        # will raise StopIteration.
        self._reloaded = True

    def set_next_scene(self, key):
        self._next_scene = self._scene_dict[key]
        self._reloaded = True

    def add(self, scene_list):
        for (index, scene) in enumerate(scene_list):
            self._scene_dict[str(index)] = scene
        self._current_scene = self._scene_dict['0']

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_scene and self._reloaded:
            self._reloaded = False
            return self._next_scene
        else:
            raise StopIteration

class SceneManager:
    def __init__(self, scenes_list=None):
        self._scenes = scenes_list
        self._current_scene = None
        self._next_scene = None
    def __iter__(self):
        return iter(self._scenes)
    def add(self, scene):
        self._scenes.append(scene)
