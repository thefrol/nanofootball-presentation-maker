import json

from nf_presentation import assets
from nf_presentation.data_classes import TrainingInfo, from_key

with assets.get_training_data() as f:
    data = json.load(f)

t = TrainingInfo(data)

print(t.id)
print(t.field_size)
print(t.team_name)
print(t.trainer_name)
print(t.objectives)


class Test:
    @from_key('name')
    def stuff(self): return {'name': 'success'}


print(Test().stuff)

new_training_data = assets.get_as_json('training-data-v0-3-1')
t_new=TrainingInfo(new_training_data)

print(t_new.exercises[0].additional_params.len)

for exercise in t_new.exercises:
    print(exercise.additional_params.coach_position)

print('end')

