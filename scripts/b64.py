import nf_presentation
import base64



pptx_bytes= nf_presentation.from_training(input_data='test')
# import codecs
# encoded4 = codecs.encode(pptx_bytes, 'utf-8')
# print(encoded4)

body = base64.b64encode(pptx_bytes).decode()

print(body)
base64.b64decode(body)