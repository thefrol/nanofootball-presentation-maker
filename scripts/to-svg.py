from cairosvg import svg2png,svg2svg

from nf_presentation.assets import get_asset_stream

files=['movie_google_icon.svg','movie_google_icon.svg']

for file in files:
    with get_asset_stream(file) as f:
        bytes=svg2png(file_obj=f,output_width=300,output_height=300)