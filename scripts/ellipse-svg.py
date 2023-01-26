from cairosvg import svg2png

source = 'prepared_scheme.svg'
out = 'ellipse.png'
with open(source, 'r') as f:
    svg2png(file_obj=f, write_to=out, unsafe=True)

