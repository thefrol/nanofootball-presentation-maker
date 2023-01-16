import nf_presentation

render_dict={
    'video_1':True
}


    

nf_presentation.from_single_exercise(
    input_data='test',
    render_options=render_dict,
    output_file='single.pptx'
)


data=nf_presentation.from_single_exercise(
    input_data='test',render_options=render_dict
)

print(data)