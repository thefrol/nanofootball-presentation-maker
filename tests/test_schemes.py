import json
import unittest
import nf_presentation
import pathlib

from nf_presentation.scheme_renderer import SchemeRenderer
from nf_presentation import assets
from nf_presentation.data_classes import SingleExerciseInfo



class TestRendering(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.files_to_delete=[]
    
    def setUp(self) -> None:
        with assets.get_exercise_test_data() as f:
            data=json.load(f)
        self.exercise=SingleExerciseInfo(raw_data=data)
        self.streams=[]

    #we need a test for old schemes too
   
    def test_scheme_1(self):
        s=self.exercise.scheme_1.to_stream()
        self.streams.append(s)
        data=s.read()
        self.assertGreater(len(data),0)

    def test_scheme_2(self):
        s=self.exercise.scheme_2.to_stream()
        self.streams.append(s)
        data=s.read()
        self.assertGreater(len(data),0)


    def tearDown(self) -> None:
        for file in self.files_to_delete:
            path_obj=pathlib.Path(file)
            if path_obj.exists():
                path_obj.unlink()




if __name__ == '__main__':
    unittest.main()




