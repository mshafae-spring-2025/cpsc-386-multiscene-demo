"""Game objects to create PyGame based games."""

import warnings

import pygame

from videogame import rgbcolors
from videogame import scene
from videogame import scenemanager


def display_info():
    """Print out information about the display driver and video information."""
    print(f'The display is using the "{pygame.display.get_driver()}" driver.')
    print("Video Info:")
    print(pygame.display.Info())

# pylint: disable=too-few-public-methods
class VideoGame:
    """Base class for creating PyGame games."""

    def __init__(
        self,
        window_width=800,
        window_height=800,
        window_title="My Awesome Game",
    ):
        """Initialize a new game with the given window size and window title."""
        pygame.init()
        self._window_size = (window_width, window_height)
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode(self._window_size)
        self._title = window_title
        pygame.display.set_caption(self._title)
        self._game_is_over = False
        if not pygame.font:
            warnings.warn("Fonts disabled.", RuntimeWarning)
        if not pygame.mixer:
            warnings.warn("Sound disabled.", RuntimeWarning)
        else:
            pygame.mixer.init()
        self._scene_manager = None

    # @property
    # def scene_manager(self):
    #     """Return the scene manager."""
    #     return _scene_manager

    def run(self):
        """Run the game; the main game loop."""
        raise NotImplementedError
# pylint: enable=too-few-public-methods


# pylint: disable=too-few-public-methods
class MultiSceneGameDemo(VideoGame):
    """Show a colored window with a colored message and a polygon."""

    def __init__(self):
        """Init the Pygame demo."""
        super().__init__(window_title="Multi Scene Demo")
        self._scene_manager = scenemanager.SceneManager()
        self._build_scenes()

    def _build_scenes(self):
        """Build scene graph for the game demo."""
        self._scene_manager.add(
            [
                scene.BlinkingTitle(
                    self._screen,
                    self._scene_manager,
                    "Multi Scene Demo",
                    rgbcolors.orange,
                    72,
                    rgbcolors.black,
                ),
                scene.RedCircleScene(self._screen, self._scene_manager),
                scene.GreenCircleScene(self._screen, self._scene_manager),
                scene.BlueCircleScene(self._screen, self._scene_manager),
            ]
        )
        self._scene_manager.set_next_scene('0')

    def run(self):
        """Run the game; the main game loop."""
        scene_iterator = iter(self._scene_manager)
        current_scene = next(scene_iterator)
        while not self._game_is_over:
            current_scene.start_scene()
            while current_scene.is_valid():
                current_scene.delta_time = self._clock.tick(
                    current_scene.frame_rate()
                )
                for event in pygame.event.get():
                    current_scene.process_event(event)
                current_scene.update_scene()
                current_scene.draw()
                # current_scene.render_updates()
                pygame.display.update()
            current_scene.end_scene()
            try:
                current_scene = next(scene_iterator)
            except StopIteration:
                self._game_is_over = True
        pygame.quit()
        return 0
# pylint: enable=too-few-public-methods
