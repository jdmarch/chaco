#!/usr/bin/env python
"""
Draws a static plot of bessel functions, oriented vertically, side-by-side.

You can experiment with using different containers (uncomment lines 30-31)
or different orientations on the plots (comment out line 41 and uncomment 42).
"""

# Major library imports
from numpy import arange
from scipy.special import jn

from chaco.example_support import COLOR_PALETTE

# Enthought library imports
from enable.api import Component, ComponentEditor
from traits.api import HasTraits, Instance
from traitsui.api import Item, Group, View
from chaco.api import PlotLabel, HPlotContainer, create_line_plot

#===============================================================================
# # Create the Chaco plot.
#===============================================================================
def _create_plot_component():
    numpoints = 100
    low = -5
    high = 15.0
    x = arange(low, high, (high-low)/numpoints)

    container = HPlotContainer(resizable = "hv", bgcolor="lightgray",
                               fill_padding=True, padding = 10)
    # container = VPlotContainer(resizable = "hv", bgcolor="lightgray",
    #                            fill_padding=True, padding = 10)


    # Plot some bessel functions
    value_range = None
    for i in range(10):
        y = jn(i, x)
        plot = create_line_plot((x,y), color=tuple(COLOR_PALETTE[i]), width=2.0,
                                orientation="v")
                               # orientation="h")
        plot.origin_axis_visible = True
        plot.origin = "top left"
        plot.padding_left = 10
        plot.padding_right = 10
        plot.border_visible = True
        plot.bgcolor = "white"
        if value_range is None:
            value_range = plot.value_mapper.range
        else:
            plot.value_range = value_range
            value_range.add(plot.value)
        if i%2 == 1:
            plot.line_style = "dash"
        container.add(plot)

    container.padding_top = 50
    container.overlays.append(PlotLabel("More Bessels",
                                        component=container,
                                        font = "swiss 16",
                                        overlay_position = "top"))

    return container

#===============================================================================
# Attributes to use for the plot view.
size=(800,600)
title="Vertical Line Plot"

#===============================================================================
# # Demo class that is used by the demo.py application.
#===============================================================================
class Demo(HasTraits):
    plot = Instance(Component)

    traits_view = View(
                    Group(
                        Item('plot', editor=ComponentEditor(size=size),
                             show_label=False),
                        orientation = "vertical"),
                    resizable=True, title=title,
                    width=size[0], height=size[1]
                    )

    def _plot_default(self):
         return _create_plot_component()

demo = Demo()

if __name__ == "__main__":
    demo.configure_traits()

# EOF
