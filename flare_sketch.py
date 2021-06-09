import streamlit as st
from backmapping import *

# provide date and time
date = '2020-05-01 13:00:00'
d = st.date_input("Select date", datetime.date.today())
st.write('Selected date:', d)
t = st.time_input('Select time', datetime.time(16, 45))
st.write('Selected time:', t)


# Chose bodies/spacecraft and measured solar wind speeds
# (vst_list: leave empty for nominal speed of vsw=400 km/s)
st.write(print_body_list())

body_list = ['STEREO-A', 'STEREO-B', 'Earth', 'MPO', 'PSP', 'Solar Orbiter',
             'Mars']
vsw_list = [300, 400, 500, 600, 700, 800, 900, 200]

# Provide a reference longitude in Carrington coordinates (e.g. flare
# longitude)
reference_long = 20
reference_lat = -20

# Initialize the Bodies
c = HeliosphericConstellation(date, body_list, vsw_list, reference_long,
                              reference_lat)

# Display coordinates
st.write(c.coord_table)

# Make the longitudinal constellation plot
c.plot(
    plot_spirals=True,               # plot Parker spirals for each body
    plot_sun_body_line=True,         # plot straight line between Sun and body
    show_earth_centered_coord=True,  # display Earth-centered coordinate system
    outfile='plot.png'               # output file (optional)
)
