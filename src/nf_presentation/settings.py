
#PRESENTATION SETTINGS

DEFAULT_TITLE='---'

DEFAULT_TABLE_WIDTH=3
DEFAULT_TABLE_ROW_HEIGHT=1

##SVG SETTINGS
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


