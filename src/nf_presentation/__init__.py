"""A module for creating pptx from Nanofootball server request 

use create_pptx(...) for real data
or create_from_test_data(...)

Example 1:
----------
    from nf_presentation import create_pptx

    create_pptx(input_data=training_data_dict,output_file='output.pptx')

Example 2:
----------

    import io
    from nf_presentation import create_pptx

    with io.BytesIO() as f:
        create_pptx(input_data=training_data_dict, output_file=f)
        send_file(f)  # your server response to client

Example 3:
----------

    from nf_presentation import create_from_test_data

    create_from_test_data(output_file='output.pptx')

Example 4:
----------

    from nf_presentation import create_from_test_data

    with io.BytesIO() as f:
        create_from_test_data(output_file=f)
        send_file(f)  # your server response to client

"""

import json
from typing import Union,IO

from .report_renderer import ReportRenderer
from .data_classes import TrainingInfo
from . import assets


def create_pptx(input_data:dict,output_file:Union[str,IO]):
    """A function creating a pptx file from giant dict request from Nanofootball server
    Arguments:
        input_data: dict
            a dict-like object containing server request for making a pptx file
        output file: str|file
            a destination for rendering pptx, may be a string for saving locally,
            or a file-like object

    Output:
        None
            Function returns nothing
    """
    t=TrainingInfo(data=input_data)
    with ReportRenderer() as renderer:
        renderer.add_title_slide(name=t.trainer_name)
        for exercise in t.exercises:
            print(exercise.name)
            renderer.add_exercise_slide(exercise=exercise)
        renderer.save(to=output_file)

def create_from_test_data(output_file:Union[str,IO]):
    """A function creating a pptx file from test request, saved inside a packet
    Should be used to test this module works right on a target machine

    Arguments:
        output file: str|file
            a destination for rendering pptx, may be a string for saving locally,
            or a file-like object

    Output:
        None
            Function returns nothing   
    """
    with assets.get_test_data() as f:
        test_data=json.load(f)

    return create_pptx(input_data=test_data,output_file=output_file)