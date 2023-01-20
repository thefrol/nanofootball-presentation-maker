import re
import requests
from io import BytesIO

from cairosvg import svg2png,svg2svg

from .settings import svg_replacements,png_render_width,png_render_height
from nf_presentation._settings import basic as basic_settings
from nf_presentation.logger import logger


class SchemeRenderer:
    """a class for rendering scheme to png
    width: size of output png, defaults to settings.png_render_width
    height: size of output png, default to settings.png_render_height
    
    usage: 
        s=SchemeRenderer()
        s.render_png(svg_text=text,to_file='output_file.png')"""
    def __init__(self,width : int = png_render_width,height : int = png_render_height):
        self.width=width
        self.height=height

    @staticmethod
    def _link_replacement(match: re.Match) -> str:
        """a helper function for re.sub() function that replaces links
        get a link at input and returns a replacement"""
        found_string=str(match.group(0))
        return ("http://nanofootball.com"+str(found_string)) 

    def _replace_links(self,svg_text)->str:
        """a function replacing relative links to web links, like /static/schemeDrawer/... -> http://nanofootball.com/static/schemeDrawer/..."""
        pattern=r'/static/[^\s]*\.svg'
        return re.sub(pattern,string=svg_text,repl=self._link_replacement)
    
    def _fix_strings(self,svg_text:str)->str:
        """a function that fixes broken svg parameters"""
        for broken_string in svg_replacements:
            fixed_string=svg_replacements[broken_string]
            svg_text=svg_text.replace(broken_string,fixed_string)
        return svg_text
    
    def render_png(self,svg_text:str, to_file:str):
        """A function rendering scheme to png, 
        svg_text: a str containing svg image
        to_file: output file can be path string or file object"""
        # step 0. get original svg
        final_svg=self.prepare_svg(svg_text=svg_text)
        # step 3. rendering
        svg2png(
            bytestring=final_svg,
            output_width=self.width,
            output_height=self.height,
            write_to=to_file
            )

    def prepare_svg(self,svg_text:str):
        """returning fully prepared svg string with all replacements and fixes,
        mostry for use in debug"""
        # step 0. get original svg
        final_svg=svg_text
        # step 1. fix links
        final_svg=self._replace_links(final_svg)
        # step 2. fix broken paramenters
        final_svg=self._fix_strings(final_svg)
        return final_svg

    def to_stream(self,svg_text) -> BytesIO:
        stream=BytesIO()
        self.render_png(svg_text=svg_text,to_file=stream)
        return stream

class NewSchemeRenderer:
    def to_stream(self,sheme_id):
        url=basic_settings.scheme_url(sheme_id=sheme_id)
        with requests.get(url) as resp:
            if not resp.ok:
                logger.error(f'Cant download scheme {sheme_id}')
                raise RuntimeError(f'cant download {url}')
            return BytesIO(resp.content)


    


