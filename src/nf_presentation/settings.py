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