from nf_presentation.renderers.base_renderer import BaseRenderer
from nf_presentation.data_classes import SingleExerciseInfo
from nf_presentation.html_renderer import HTMLRenderer
from nf_presentation.scheme_renderer import SchemeRenderer
import nf_presentation.assets as assets

from nf_presentation._settings import compact_layout as current_layout
import nf_presentation.settings as base_settings

_default_description="""Описание:



Тренерские акценты:


"""

class RenderOptions:
    _media_fields=['video_1','video_2','animation_1','animation_2']
    def __init__(self,raw_data):
        self.raw_data=raw_data
        self.check()
    @property
    def media_fields_to_render(self) -> list[str]:
        """returns a list of edia fields should be rendered to a pptx
        ['video_2','animation_1']"""
        return [field for field in self._media_fields if self.raw_data.get(field)]  # if checked as True
    def check(self):
        #check if video or animation will be added to pptx
        if not any([self.raw_data.get(field) for field in self._media_fields]):
            print('WARN: (Render Options) no player links are marked to be added to pptx')






class CompactRenderer(BaseRenderer):
    def __init__(self, render_options:RenderOptions):
        super().__init__(ratio=base_settings.PRESENTATION_RATIO)
        self.render_options : RenderOptions = render_options
    def add_exercise_slide(self, exercise_data:dict,additional_params:list[str]=None):
        """
        Arguments:
            additional_params: if None- data would be taken from exercise info,
                if not - using current list of additional params"""
        exercise=SingleExerciseInfo(raw_data=exercise_data)
        slide=self.presentation_builder.create_slide()

        title=slide.create_title(base_settings.DEFAULT_SLIDE_TITLE).at(current_layout.TITLE_POSITION).with_size(current_layout.TITLE_SIZE)
        title.with_foreground(current_layout.TITLE_FOREGROUND).with_background(current_layout.TITLE_BACKGROUND)

        #decription_text=HTMLRenderer().render(exercise.description)
        description_text=_default_description
        right_table=slide.create_table().at(current_layout.RIGHT_TABLE_POSITION).with_width(current_layout.RIGHT_TABLE_WIDTH)
        right_table.append_row(description_text)
        # mayble here add default params iter
        
        if additional_params is None:
            left_rows=exercise.additional_params.items()
        else:
            left_rows=[(param,'') for param in additional_params]

        left_table=slide.create_table().at(current_layout.LEFT_TABLE_POSITION).with_width(current_layout.LEFT_TABLE_WIDTH)
        left_table.append_row(exercise.title)
        left_table.append_empty_row()
        
        for row in left_rows:
           left_table.append_row(*row) 
        # left_table.append_empty_row()
        # left_table.append_row('ссылки')
        # #maybe exercise info should return a tuples already

        s=SchemeRenderer()
        image_stream=s.to_stream(exercise.schemes[0])
        self._open_streams.append(image_stream)
        slide.create_image(image_stream).at(current_layout.SCHEME_POSITION).set_size(current_layout.SCHEME_WIDTH,None)

        #add links
        slide.create_text('Ссылки:').at(current_layout.LINKS_TITLE_POSITION)

        link_position=current_layout.LINKS_AREA
        for media_field in self.render_options.media_fields_to_render:
            player_url=exercise.get_media(media_field).nftv_player
            is_animation='animation' in media_field

            image_file=current_layout.LINKS_ANIMATION_ICON_FILENAME if is_animation else current_layout.LINKS_VIDEO_ICON_FILENAME
            image_stream=assets.convert_to_png(filename=image_file)
            self.track_stream(image_stream)
            slide.create_image(image_file=image_stream).at(link_position).with_size(current_layout.LINKS_IMAGE_SIZE).with_href(player_url)

            x_delta,y_delta=current_layout.LINKS_IMAGE_SIZE
            position_increment=x_delta,0
            link_position=link_position+position_increment



