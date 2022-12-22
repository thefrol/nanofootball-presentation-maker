from nf_presentation.builders import SlideBuilder, PresentationBuilder, RowTableBuilder, ImageBuilder

image_file='output_module.png'

p=PresentationBuilder()
s=SlideBuilder()



t=RowTableBuilder()
t.append_row('1',2,3)
t.append_row(3,4)

i=ImageBuilder(image_file).set_position(1,4).set_size(None,10)

s.title='sample fromo builders'
s.add_element(t)
s.add_element(i)

p.add_slide(s)

p.save('from builders.pptx')
