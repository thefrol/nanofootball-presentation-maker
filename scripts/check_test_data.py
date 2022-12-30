import json
data_file='test_data.json'
with open(data_file,'r',encoding='utf8') as f:
    data=json.load(f)

exercises=data.get('exercises_info')
print(len(exercises))

class ExerciseInfo:
    def __init__(self, data:dict):
        self.raw_data:dict=data
    @property
    def name(self):
        return self.raw_data.get('exercise_name',{}).get('ru')
    @property
    def scheme_main(self):
        return self.raw_data.get('exercise_scheme',{}).get('scheme_1')
    @property
    def description(self):
        return self.raw_data.get('exercise_description')

class TrainingInfo:
    def __init__(self,data:dict):
        self.raw_data=data
        self._exercises : list[ExerciseInfo] = None

    @property
    def exercises(self) -> list[ExerciseInfo]:
        if self._exercises is None:
            self._exercises= [ExerciseInfo(data) for data in self.raw_data.get('exercises_info')]
        return self._exercises

t=TrainingInfo(data=data)
for exercise in t.exercises:
    print(exercise.name)
    