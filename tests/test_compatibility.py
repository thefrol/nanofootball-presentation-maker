import unittest
import nf_presentation

class TestV_0_2_0(unittest.TestCase):
    def test_exercise_export(self):
        render_options={
            'scheme_1':True,
            'video_1':True,
            'video_2':True,
            'animation_1':True,
            'animation_2':True,

        }
        data=nf_presentation.from_single_exercise(input_data='test',render_options=render_options)
        self.assertIsNotNone(data)
