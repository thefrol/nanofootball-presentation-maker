import nf_presentation

data = nf_presentation.from_event(input_data='test', output_file='event.pptx')
assert data is not None
