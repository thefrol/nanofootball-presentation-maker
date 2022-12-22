import pptx
from pptx import Presentation
from pptx.shapes.placeholder import SlidePlaceholder
from pptx.slide import Slide

file='sample.pptx'

p:pptx.Presentation=pptx.Presentation(pptx=file)
slide:Slide=p.slides[0]
for shape in slide.shapes:
    print(shape.name)
    # for placeholder in shape.placeholders:
    #     print('...'+placeholder.name)
#placeholder:SlidePlaceholder=slide.shapes.placeholders[13]
#
print(placeholder.placeholder_format)

