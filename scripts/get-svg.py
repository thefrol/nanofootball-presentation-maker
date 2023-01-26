from nf_presentation.scheme_renderer import SchemeRenderer
import nf_presentation
from nanofoot import ExercisesService

exs_id = 2675
render_dict = {
    'video_1': True,
    'video_2': True,
    'animation_1': True,
    'animation_2': True,
    'scheme_1': False,
    'pips': 'aaa'
}

data = ExercisesService().get(exs_id=exs_id).raw_data

exs = nf_presentation.data_classes.SingleExerciseInfo(data)
with open('scheme.svg', 'w') as f:
    f.write(exs.old_schemes[0])


a = SchemeRenderer()
prepared = a.prepare_svg(exs.old_schemes[0])

with open('prepared_scheme.svg', 'w') as f:
    f.write(prepared)
