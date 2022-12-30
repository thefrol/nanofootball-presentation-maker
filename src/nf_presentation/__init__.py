import json

from .report_renderer import ReportRenderer
from .data_classes import TrainingInfo
from . import assets


def create_pptx(input_data:dict,output_file:str):
    t=TrainingInfo(data=input_data)
    with ReportRenderer() as renderer:
        renderer.add_title_slide(name=t.trainer_name)
        for exercise in t.exercises:
            print(exercise.name)
            renderer.add_exercise_slide(exercise=exercise)
        renderer.save(to=output_file)

def create_from_test_data(output_file):
    with assets.get_test_data() as f:
        test_data=json.load(f)

    return create_pptx(input_data=test_data,output_file=output_file)