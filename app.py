import streamlit as st
import fastf1 as ff1
from fastf1 import plotting
import numpy as np
import plotly.graph_objects as go

# Enable the cache
ff1.Cache.enable_cache('cache') 

# Setup plotting
plotting.setup_mpl()

# Streamlit App
st.title('F1 Track Dominance Analysis')

# Year Selection
year = st.sidebar.selectbox('Select Year', [2024, 2023])

# Circuit Selection
circuit = st.sidebar.selectbox('Select Circuit', ['Silverstone', 'Monza', 'Belgium', 'Suzuka', 'Bahrain', 'Saudi Arabia',
                                                  'Australia', 'China', 'Azerbaijan', 'Miami', 'Imola', 'Monaco', 'Spain', 'Canada',
                                                  'Austria', 'Hungary', 'Netherlands', 'Singapore', 'Qatar', 'Austin',
                                                  'Mexico', 'Brazil', 'Abu Dhabi', 'Las Vegas'])

# Load session data
@st.cache_data
def load_session(year, circuit):
    quali = ff1.get_session(year, circuit, 'Q')
    quali.load()
    return quali

quali = load_session(year, circuit)

# Get qualifying sessions
q1, q2, q3 = quali.laps.split_qualifying_sessions()

# Get list of drivers who qualified for Q3
q3_drivers = q3['Driver'].unique()
selected_drivers = st.sidebar.multiselect('Select Drivers', q3_drivers, default=q3_drivers[:3])

# Check if at least one driver is selected
if not selected_drivers:
    st.warning('Please select at least one driver.')
else:
    # Retrieve telemetry data for selected drivers
    telemetries = {}
    for driver in selected_drivers:
        lap = q3.pick_driver(driver).pick_fastest()
        telemetries[driver] = lap.get_telemetry().add_distance()

    # Define number of minisectors dynamically
    num_minisectors = st.sidebar.slider('Number of Minisectors', min_value=10, max_value=50, value=25)
    minisectors = np.linspace(0, max(tel['Distance'].max() for tel in telemetries.values()), num_minisectors)

    # Determine fastest driver per minisector
    minisector_winner = []

    for i in range(len(minisectors) - 1):
        speeds = {driver: tel[(tel['Distance'] >= minisectors[i]) & (tel['Distance'] < minisectors[i+1])]['Speed'].mean()
                  for driver, tel in telemetries.items()}
        
        winner = max(speeds, key=speeds.get)
        minisector_winner.append(winner)

    # Create Plotly figure
    fig = go.Figure()

    distinct_colors = [
        "#FF0000",  # Red
        "#0000FF",  # Blue
        "#00FF00",  # Green
        "#FFA500",  # Orange
        "#800080",  # Purple
        "#00FFFF",  # Cyan
        "#FF00FF",  # Magenta
        "#FFFF00",  # Yellow
        "#A52A2A",  # Brown
        "#000000"   # Black
    ]

    # Assign colors to drivers from the distinct color list
    def assign_colors(drivers):
        return {driver: distinct_colors[i % len(distinct_colors)] for i, driver in enumerate(drivers)}

    colors = assign_colors(selected_drivers)

    # Add traces for each driver to the legend
    for driver in selected_drivers:
        fig.add_trace(go.Scatter(
            x=[None], y=[None], mode='lines',
            line=dict(color=colors[driver], width=4),
            name=driver,
            legendgroup=driver,
            showlegend=True
        ))

    # Dynamic line width and style
    line_width = st.sidebar.slider('Line Width', min_value=2, max_value=10, value=4)
    line_style = st.sidebar.selectbox('Line Style', ['solid', 'dash', 'dot', 'dashdot'])

    # Plot each minisector with improved line styling
    for i in range(len(minisectors) - 1):
        winner = minisector_winner[i]
        x = telemetries[winner][(telemetries[winner]['Distance'] >= minisectors[i]) & 
                                (telemetries[winner]['Distance'] < minisectors[i+1])]['X'].values
        y = telemetries[winner][(telemetries[winner]['Distance'] >= minisectors[i]) & 
                                (telemetries[winner]['Distance'] < minisectors[i+1])]['Y'].values

        fig.add_trace(go.Scatter(
            x=x, y=y,
            mode='lines',
            line=dict(color=colors[winner], width=line_width, dash=line_style),
            name=winner,
            showlegend=False
        ))

    # Add enhanced annotations with tooltips for each driver
    for idx, driver in enumerate(selected_drivers):
        driver_lap = q3.pick_driver(driver).pick_fastest()
        driver_time = ":".join(str(driver_lap.LapTime).split('.')[0][2:].split(' ')[-1].split(':')[1:])
        driver_position = q3[q3['Driver'] == driver].iloc[0]['Position']

        fig.add_annotation(
            x=0.5, y=1 - (idx * 0.1),  # Adjust y to stack annotations vertically
            xref='paper', yref='paper',
            text=f"<b>{driver}:</b> {driver_time} <b>(P{driver_position})</b>",
            showarrow=False,
            font=dict(size=12, color=colors[driver]),
            align='left',
            xanchor='center',
            yanchor='top',
            bordercolor=colors[driver],
            borderwidth=1,
            borderpad=4,
            bgcolor='rgba(255, 255, 255, 0.8)'
        )

    # Determine the fastest driver overall
    fastest_driver = q3.pick_fastest().Driver
    fastest_time = q3.pick_fastest().LapTime
    minutes = fastest_time.components.minutes
    seconds = fastest_time.components.seconds
    milliseconds = fastest_time.components.milliseconds
    formatted_fastest_time = f"{minutes}m {seconds}s {milliseconds}ms"

    # Beautify and Enhance the Plotly Figure
    fig.update_layout(
        title={
            'text': f'<b>Track Dominance Chart - {circuit} {year} Q3</b>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 24, 'color': 'black'}
        },
        xaxis_title='Distance (m)',
        yaxis_title='Track Position',
        legend_title='<b>Drivers</b>',
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        font=dict(family='Arial', size=14, color='black'),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5,
            bgcolor='rgba(255, 255, 255, 0.8)',
            bordercolor='black',
            borderwidth=1
        ),
        annotations=[
            dict(
                x=0.5, y=1.1, xref='paper', yref='paper',
                text=f"<b>Fastest Driver: {fastest_driver} ({formatted_fastest_time})</b>",
                showarrow=False,
                font=dict(size=16, color='black')
            )
        ],
        margin=dict(l=0, r=0, t=150, b=0)  # Adjust margins to fit title and annotations
    )

    # Display the enhanced plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)
