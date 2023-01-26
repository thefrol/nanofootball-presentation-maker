import json

from nf_presentation import assets
from nf_presentation.data_classes import TrainingInfo

with assets.get_training_data() as f:
    data = json.load(f)

t = TrainingInfo(data)

print(t.id)
print(t.field_size)
print(t.team_name)
print(t.trainer_name)
print(t.objectives)
