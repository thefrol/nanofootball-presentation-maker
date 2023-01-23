import unittest
import nf_presentation

class TestSigleExerciseExport(unittest.TestCase):
    def test_render_with_new_scheme(self):
        render_options={
            'scheme_1':True,
            'video_1':True,
            'video_2':True,
            'animation_1':True,
            'animation_2':True,

        }
        data=nf_presentation.from_single_exercise(input_data='test',render_options=render_options)
        self.assertIsNotNone(data)

    def test_render_with_old_scheme(self):
        render_options={
            'scheme_1_old':True,
            'video_1':True,
            'video_2':True,
            'animation_1':True,
            'animation_2':True,

        }
        data=nf_presentation.from_single_exercise(input_data='test',render_options=render_options)
        self.assertIsNotNone(data)

    def test_render_with_none_options(self):
        render_options=None
        data=nf_presentation.from_single_exercise(input_data='test',render_options=render_options)
        self.assertIsNotNone(data)

class TestTrainingExport(unittest.TestCase):
    def test_short(self):
        render_options=None
        data=nf_presentation.from_training(input_data='test')
        self.assertIsNotNone(data)
    def test_long(self):
        render_options=None
        data=nf_presentation.from_training(input_data='test-long')
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()

