from nf_presentation.renderers.base_renderer import BaseRenderer
from nf_presentation.data_classes import SingleExerciseInfo

from nf_presentation._settings import compact_layout as current_layout
import nf_presentation.settings as base_settings

class CompactRenderer(BaseRenderer):
    def __init__(self):
        super().__init__(ratio=base_settings.PRESENTATION_RATIO)
    def add_exercise_slide(self, exercise_data:dict):
        pass

