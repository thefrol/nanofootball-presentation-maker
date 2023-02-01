"""A module for creating pptx from Nanofootball server request

use create_pptx(...) for real data
or create_from_test_data(...)

Example 1:
----------
    import nf_presentation

    # для тренировки
    pptx_bytes= nf_presentaion.from_training(input_data=training_data_dict)
    # или для одного упражнения
    pptx_bytes= nf_presentaion.from_single_exercise(
        input_data=exercise_data_dict)
"""

import json
import io
from typing import Union

from nf_presentation.renderers.compact_renderer import (
                                            CompactRenderer,
                                            ExerciseRenderOptions)

from nf_presentation.renderers.training_renderer import TrainingRenderer
from .data_classes import TrainingInfo, SingleExerciseInfo
from . import assets
from nf_presentation.logger import logger
from nf_presentation._settings import basic as basic_settings


def return_bytes(func):
    """a decorator
    Reads the created file objects and returns
    a bytes array as function standart return """
    def callee(*args, output_file: Union[str, None] = None, **kwargs):
        # target_stream= output_file or io.BytesIO()

        with io.BytesIO() as stream:

            func(*args, **kwargs, output_file=stream)

            stream.seek(0)
            data = stream.read()
            stream.close()

            if output_file is not None:
                with open(output_file, 'wb') as f:
                    f.write(data)

            return data
    return callee


@return_bytes
def from_training(input_data: dict, output_file: Union[str, None] = None):
    """DEPRECATED
    A function creating a pptx file from training of Nanofootball server
    Arguments:
        input_data: dict
            'test' - use a test data
            a dict-like object containing server request for making a pptx file
        output_file: str|None
            a destination for rendering pptx,
            may be a file-path string for saving locally


    Output:
        Byte-array
            returns a bytes of pptx document.
            This data can be written to file or sent over HTTP
    """
    logger.warn('function from_training() is not properly maintained. '
                + 'Please use from_event()')
    if input_data == 'test':
        with assets.get_training_data() as f:
            input_data = json.load(f)
    elif input_data == 'test-long':
        with assets.get_training_data(short=False) as f:
            input_data = json.load(f)

    training = TrainingInfo(raw_data=input_data)
    with TrainingRenderer() as renderer:
        renderer.add_title_slide(
            name=training.trainer_name,
            theme=training.main_objective)
        renderer.add_training_slide(training)
        for exercise in training.exercises:
            logger.debug(f'rendering {exercise.title}')
            renderer.add_exercise_slide(exercise=exercise, training=training)
        renderer.save(to=output_file)


@return_bytes
def from_event(input_data: dict, output_file: Union[str, None] = None):
    """A function creating a pptx file from event dict of Nanofootball
    Arguments:
        input_data: dict
            'test' - use a test data(2 exercises)
            a dict-like object containing server request for making a pptx file
        output_file: str|None
            a destination for rendering pptx,
            may be a file-path string for saving locally,


    Output:
        Byte-array
            returns a bytes of pptx document.
            This data can be written to file or be send over HTTP
    """
    event_data = input_data

    if event_data == 'test':
        with assets.get_event_data() as f:
            event_data: dict = json.load(f)

    if event_data.get('training') is None:
        logger.error('Event contains no training')
        return None

    training_data = event_data.get('training')
    training = TrainingInfo(raw_data=training_data)
    with TrainingRenderer() as renderer:
        renderer.add_title_slide(
            name=training.trainer_name,
            theme=training.main_objective)
        renderer.add_training_slide(training)
        for exercise in training.exercises:
            logger.debug(f'rendering {exercise.title}')
            renderer.add_exercise_slide(exercise=exercise, training=training)
        renderer.save(to=output_file)


@return_bytes
def from_single_exercise(
        input_data: Union[dict, str],
        render_options: dict,
        output_file: Union[str, None] = None
        ) -> bytes:
    """A function creating a pptx file from exercise object in Nanofootball API
    Arguments:
        input_data: dict | str
            'test' - use a test data
            dict - a dict-like object containing server
                request for making a pptx file
        output_file: str|None
            a destination for rendering pptx,
            may be a file-path string for saving locally,
        render_options: dict
            a set of items to show or not show on the rendered scheme
                ex. {
                'scheme_1': True,
                'scheme_2': True,
                'video_1': True,
                ...
                }

    Output:
        Byte-array
            returns a bytes of pptx document.
            This data can be written to file or sent over HTTP
    """
    if input_data == 'test':
        with assets.get_exercise_test_data() as f:
            input_data = json.load(f)

    exercise = SingleExerciseInfo(input_data)

    if render_options is None:
        render_options = None
    else:
        render_options = ExerciseRenderOptions(render_options)
    with CompactRenderer() as renderer:

        renderer.add_exercise_slide(exercise, render_options=render_options)
        renderer.save(to=output_file)
