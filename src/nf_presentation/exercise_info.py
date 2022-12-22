class ExerciseInfo:
    """A class representing info we get for an exercise to a python object"""
    def __init__(self, raw_data:dict):
        self.raw_data=raw_data
    @property
    def additional_params(self):
        """returning exercise.additinal_params as dict, converting from list[dict]"""
        return { entry.get('title',''):entry.get('value','') for entry in self.raw_data.get('additional_params',{})}
    @property
    def description(self):
        return self.raw_data.get('desctiption','')
    @property
    def title(self):
        return self.get('title','')
        
