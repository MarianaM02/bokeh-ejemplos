import random

from bokeh.plotting import figure, curdoc
from bokeh.driving import linear
import bokeh

from bokeh.io import output_file, show
from bokeh.models import (BoxZoomTool, Circle, HoverTool,
                          MultiLine, Plot, Range1d, ResetTool)
from bokeh.palettes import Spectral4
from bokeh.plotting import from_networkx
from bokeh.driving import count

p = figure(plot_width= 1000, plot_height = 400)
p.x_range.follow = "end"
p.x_range.follow_interval = 50
p.x_range.range_padding = 0
r1 = p.line([], [], color=Spectral4[1], line_width=2)
r2 = p.line([], [], color=Spectral4[2], line_width=2)

ds1 = r1.data_source
ds2 = r2.data_source

@linear()
def update(step):
	ds1.data['x'].append(step)
	ds1.data['y'].append(random.randint(0, 1000))
	ds2.data['x'].append(step)
	ds2.data['y'].append(random.randint(0, 1000))
	ds1.trigger('data', ds1.data, ds1.data)
	ds2.trigger('data', ds2.data, ds2.data)

curdoc().add_root(p)
curdoc().add_periodic_callback(update, 400)
