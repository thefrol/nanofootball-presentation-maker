import json
import io

from nanofoot import ExercisesService
from nf_presentation import ReportRenderer
from nf_presentation.data_classes import TrainingInfo
from nf_presentation import create_from_test_data,create_pptx

#create_from_test_data(output_file='from_test_data.pptx')


data=create_from_test_data()
print(data)

# name='Иванов А.А.'
# export_to='from_real_data.pptx'
# data_file='test_data.json'
# with open(data_file,'r',encoding='utf8') as f:
#     data=json.load(f)

# data['trainer']=name

# t=TrainingInfo(data=data)
# with ReportRenderer() as renderer:
#     renderer.add_title_slide(name=t.trainer_name)
#     for exercise in t.exercises:
#         print(exercise.name)
#         renderer.add_exercise_slide(exercise=exercise)
#     renderer.save(to=export_to)