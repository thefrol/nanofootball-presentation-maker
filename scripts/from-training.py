import nf_presentation

data = nf_presentation.from_training(input_data='test', output_file='training.pptx')
assert data is not None
