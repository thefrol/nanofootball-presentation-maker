#import pptx

#file='from_real_data_9641.pptx'

#p=pptx.Presentation(file)
#print(p.slide_width,p.slide_height,type(p.slide_width))

#for 4x3: w= 9144000 h=6858000
#for 16x9: w=9144000 h=5143500

from nf_presentation.builders import Ratios

Ratios.get_by_alias('16:9')