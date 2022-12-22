from nf_presentation.slide_builder import SlideBuilder,PresentationBuilder,RowTableBuilder

p=PresentationBuilder()
s=SlideBuilder()
t=RowTableBuilder()

t.append_row('1',2,3)
t.append_row(3,4)

s.title='sample fromo builders'
s.add_element(t)

p.add_slide(s)

p.save('from builders.pptx')
