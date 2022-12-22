from .builders import PresentationBuilder
from .exercise_info import ExerciseInfo
from .scheme_renderer import SchemeRenderer
from .settings import (
                ADDITIONAL_TABLE_POSITION, ADDITIONAL_TABLE_WIDTH,
                BASIC_TABLE_POSITION, BASIC_TABLE_WIDTH,
                LINKS_TABLE_POSTION,LINKS_TABLE_WIDTH,
                SCHEME_HEIGHT,SCHEME_WIDTH, SCHEME_POSITION,
                DEFAULT_SLIDE_TITLE
                )

class ReportRenderer:
    def __init__(self):
        self.presentation_builder=PresentationBuilder()
    def add_exercise_slide(self,exercise_data:dict):
        exercise=ExerciseInfo(raw_data=exercise_data)
        slide=self.presentation_builder.create_slide(title=DEFAULT_SLIDE_TITLE)

        basic_info_table=slide.create_table().at(BASIC_TABLE_POSITION).with_width(BASIC_TABLE_WIDTH)
        basic_info_table.append_row(exercise.title)
        basic_info_table.append_empty_row()
        basic_info_table.append_row(exercise.description)
        # mayble here add default params iter

        additional_info_table=slide.create_table().at(ADDITIONAL_TABLE_POSITION).with_width(ADDITIONAL_TABLE_WIDTH)
        for row in list(exercise.additional_params.items()):
           additional_info_table.append_row(*row) 
        #maybe exercise info should return a tuples already

        links_table=slide.create_table().at(LINKS_TABLE_POSTION).with_width(LINKS_TABLE_WIDTH)
        links_table.append_row('ссылки')
        links_table.append_row('ссылки')

        #creating a scheme
        s=SchemeRenderer()
        image_stream=s.to_stream(exercise.schemes[0])
        slide.create_image(image_stream).at(SCHEME_POSITION).set_size(SCHEME_WIDTH,None)



    def add_title_slide(self,title_data:dict):
        pass
    def save(self,to:str):
        self.presentation_builder.save(to)