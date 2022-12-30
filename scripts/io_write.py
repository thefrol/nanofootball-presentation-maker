import io
from nf_presentation import create_from_test_data

with io.BytesIO() as f:
    create_from_test_data(output_file=f)
    