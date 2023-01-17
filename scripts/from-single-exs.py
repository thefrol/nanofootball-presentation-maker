import nf_presentation
from nanofoot import ExercisesService

render_dict={
    'video_1':True,
    'video_2':True,
    'animation_1':True,
    'animation_2':True,
    'scheme_1':False,
    'pips':'aaa'
}

#data=ExercisesService().get(9490).raw_data
    

nf_presentation.from_single_exercise(
    input_data='test',
    render_options=render_dict,
    output_file='single.pptx'
)

