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
