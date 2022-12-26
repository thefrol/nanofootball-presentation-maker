#
# Output formatting
#

#presentation
PRESENTATION_RATIO='16:9'

# left side
SCHEME_POSITION=(0.4,3.5)
SCHEME_HEIGHT=8.5 # not used atm
SCHEME_WIDTH=11

ADDITIONAL_TABLE_POSITION=(0.4,11.5)
ADDITIONAL_TABLE_WIDTH=11

#right side

BASIC_TABLE_POSITION=(12.0,3.5)
BASIC_TABLE_WIDTH=12.5

LINKS_TABLE_POSTION=(12,16)
LINKS_TABLE_WIDTH=12.5

DEFAULT_SLIDE_TITLE='Основная часть'

# PRESENTATION SETTINGS

DEFAULT_TITLE='---' #TODO default value for non found items

DEFAULT_TABLE_WIDTH=3
DEFAULT_TABLE_ROW_HEIGHT=0.7

# SVG SETTINGS
svg_replacements={
    'markerwidth':'markerWidth',
    'markerheight':'markerHeight',
    'viewbox':'viewBox',
    'refx':'refX',
    'refy':'refY'
}

png_render_width=600
png_render_height=400

def add_svg_replacement(old:str,new:str):
    svg_replacements[old]=new


