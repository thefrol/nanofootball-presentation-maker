"""Renders currently new version of training data"""

from nf_presentation import assets
import nf_presentation

train_data=nf_presentation.assets.get_as_json('training-data-v0-4-0')

data=nf_presentation.from_training(input_data=train_data,output_file='new_event.pptx')
assert data is not None
