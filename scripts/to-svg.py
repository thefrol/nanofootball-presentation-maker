import json

from nf_presentation import scheme_renderer,assets
from nf_presentation.data_classes import SingleExerciseInfo

file_name='fallback_scheme.png'

with assets.get_exercise_test_data() as f:
    data=json.load(f)
exercise=SingleExerciseInfo(raw_data=data)

svg1:str=exercise.schemes[1]
        # links=get_links(svg1)

r=scheme_renderer.SchemeRenderer()
r.render_png(svg_text=svg1, to_file=file_name)