import streamlit as st
import pandas as pd
import numpy as np
from heater_model import Heater, INPUT_SPECS, OUTPUT_SPECS, OUTPUT_SECTIONS
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Configure the page
st.set_page_config(
    page_title="🔥 Heater Efficiency Calculator",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional visuals with high contrast
st.markdown("""
<style>
    /* Main app background - professional dark theme */
    .main {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0a0e27 100%);
        color: #ffffff;
    }

    .stApp {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0a0e27 100%);
        color: #ffffff;
    }

    /* All body text - pure white for maximum contrast */
    p, span, div, label, .stMarkdown {
        color: #ffffff !important;
    }

    /* Metric containers - high contrast design */
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(14, 165, 233, 0.2) 0%, rgba(6, 182, 212, 0.2) 100%);
        border: 2px solid rgba(14, 165, 233, 0.6);
        padding: 1.2rem;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
    }

    div[data-testid="metric-container"] > label[data-testid="metric-label"] > div {
        color: #ffffff !important;
        font-weight: 700;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    div[data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: #38bdf8 !important;
        font-size: 2rem !important;
        font-weight: 700;
    }

    div[data-testid="metric-container"] [data-testid="stMetricDelta"] {
        color: #ffffff !important;
        font-weight: 600;
    }

    /* Sidebar - much lighter for better readability */
    div[data-testid="stSidebar"] > div {
        background: linear-gradient(180deg, #2d3748 0%, #1e3a5f 100%) !important;
    }

    /* Sidebar headings - pure white, larger */
    div[data-testid="stSidebar"] h2 {
        color: #ffffff !important;
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
    }

    div[data-testid="stSidebar"] h3 {
        color: #ffffff !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        margin-top: 1.5rem !important;
        margin-bottom: 0.8rem !important;
    }

    /* Sidebar input labels - bright white */
    div[data-testid="stSidebar"] label {
        color: #ffffff !important;
        font-weight: 500 !important;
        font-size: 0.9rem !important;
    }

    /* Sidebar input fields - white background, dark text, high contrast */
    div[data-testid="stSidebar"] .stNumberInput > div > div > input {
        background-color: #ffffff !important;
        color: #1a202c !important;
        border: 2px solid #0ea5e9 !important;
        border-radius: 6px;
        font-weight: 600 !important;
        font-size: 1rem !important;
        padding: 0.5rem !important;
    }

    div[data-testid="stSidebar"] .stNumberInput > div > div > input:focus {
        background-color: #ffffff !important;
        border: 3px solid #06b6d4 !important;
        box-shadow: 0 0 0 3px rgba(6, 182, 212, 0.3);
        outline: none;
    }

    /* Sidebar radio buttons */
    div[data-testid="stSidebar"] .stRadio > label {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
    }

    div[data-testid="stSidebar"] .stRadio label[data-baseweb="radio"] {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* Sidebar info/alert boxes */
    div[data-testid="stSidebar"] div[data-testid="stAlert"] {
        background-color: rgba(14, 165, 233, 0.3) !important;
        border: 2px solid rgba(14, 165, 233, 0.8) !important;
    }

    div[data-testid="stSidebar"] div[data-testid="stAlert"] * {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* Headers - bright and prominent */
    .custom-header {
        color: #38bdf8 !important;
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }

    .section-header {
        color: #0ea5e9 !important;
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid #0ea5e9;
        padding-bottom: 0.5rem;
    }

    /* Buttons - high contrast */
    .stButton > button {
        color: #ffffff !important;
        background: linear-gradient(135deg, #0284c7 0%, #0ea5e9 100%);
        border: none;
        font-weight: 700;
        font-size: 1.1rem;
        padding: 0.8rem 2rem;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #0ea5e9 0%, #38bdf8 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
    }

    /* Expanders - better contrast */
    div[data-testid="stExpander"] {
        background-color: rgba(45, 55, 72, 0.4);
        border-radius: 8px;
        border: 2px solid rgba(14, 165, 233, 0.4);
        margin: 0.5rem 0;
    }

    div[data-testid="stExpander"] summary {
        color: #ffffff !important;
        font-weight: 600;
    }

    div[data-testid="stExpander"] * {
        color: #ffffff !important;
    }

    /* Highlight boxes */
    .highlight-box {
        background: rgba(14, 165, 233, 0.2);
        color: #ffffff !important;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #0ea5e9;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }

    .highlight-box * {
        color: #ffffff !important;
        font-weight: 500;
    }

    /* Info/Alert boxes */
    div[data-testid="stAlert"] {
        background-color: rgba(14, 165, 233, 0.25) !important;
        border: 2px solid rgba(14, 165, 233, 0.7) !important;
    }

    div[data-testid="stAlert"] * {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* Tables - high contrast */
    table {
        color: #ffffff !important;
        border-collapse: separate;
        border-spacing: 0;
    }

    th {
        background-color: rgba(14, 165, 233, 0.4) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        padding: 0.8rem !important;
        border-bottom: 2px solid #0ea5e9;
    }

    td {
        color: #ffffff !important;
        padding: 0.6rem !important;
        font-weight: 500;
    }

    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .custom-header {
            font-size: 2rem !important;
        }

        .section-header {
            font-size: 1.4rem !important;
        }

        div[data-testid="metric-container"] [data-testid="stMetricValue"] {
            font-size: 1.5rem !important;
        }

        div[data-testid="stSidebar"] h2 {
            font-size: 1.2rem !important;
        }

        div[data-testid="stSidebar"] h3 {
            font-size: 1rem !important;
        }
    }

    /* Small mobile devices */
    @media (max-width: 480px) {
        .custom-header {
            font-size: 1.5rem !important;
        }

        .section-header {
            font-size: 1.2rem !important;
        }

        .stButton > button {
            font-size: 0.9rem !important;
            padding: 0.6rem 1.5rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for inputs
if 'heater_inputs' not in st.session_state:
    st.session_state.heater_inputs = {}

# Main header
st.markdown('<h1 class="custom-header">🔥 Heater Efficiency Calculator</h1>', unsafe_allow_html=True)
st.markdown(
    '<p style="text-align: center; font-size: 1.2rem; color: rgba(255, 255, 255, 0.8); margin-bottom: 2rem;">Advanced API-560 Based Heater Performance Analysis</p>',
    unsafe_allow_html=True
)

# Sidebar for inputs
with st.sidebar:
    st.markdown('<h2 class="section-header">⚙️ Input Parameters</h2>', unsafe_allow_html=True)

    # Group inputs by category
    basic_inputs = [s for s in INPUT_SPECS if s.row and s.row <= 8]
    composition_inputs = [s for s in INPUT_SPECS if s.row and 10 <= s.row <= 25]
    trends_inputs = [s for s in INPUT_SPECS if s.row and 27 <= s.row <= 31]
    cems_inputs = [s for s in INPUT_SPECS if s.row and 33 <= s.row <= 40]
    constants_inputs = [s for s in INPUT_SPECS if s.row and s.row >= 42]

    # Basic Operating Parameters
    st.markdown("### 🎯 Basic Operating Parameters")
    for spec in basic_inputs:
        key = spec.name
        label = f"{spec.desc} ({spec.uom})" if spec.uom else spec.desc

        # Set default values for demonstration
        default_values = {
            'fuel_gas_flow_corrected': 837.0,
            'fuel_gas_temp': 25.0,
            'air_temperature': 25.0,
            'o2_analyzer': 4.0,
            'stack_temp': 240.0,
            'arch_temp_bwt': 675.0,
        }

        default_val = default_values.get(key, 0.0)
        st.session_state.heater_inputs[key] = st.number_input(
            label,
            value=st.session_state.heater_inputs.get(key, default_val),
            step=0.1,
            key=f"input_{key}"
        )

    # Fuel Gas Composition
    st.markdown("### 🧪 Fuel Gas Composition")
    composition_defaults = {
        'c1': 51.1, 'c2': 13.4, 'c2_unsat': 0.0, 'c3': 9.06,
        'c3_unsat': 0.0, 'i_c4': 3.72, 'n_c4': 3.47, 'c4_unsat': 0.0,
        'c5': 0.75, 'c6': 0.0, 'n2': 0.0, 'h2': 70.83,
        'O2_argon': 0.0, 'co': 0.0, 'co2': 0.178, 'h2s': 0.0001
    }

    for spec in composition_inputs:
        key = spec.name
        label = f"{spec.desc} ({spec.uom})" if spec.uom else spec.desc
        default_val = composition_defaults.get(key, 0.0)
        st.session_state.heater_inputs[key] = st.number_input(
            label,
            value=st.session_state.heater_inputs.get(key, default_val),
            step=0.01,
            format="%.3f",
            key=f"input_{key}"
        )

    # Operating Trends
    st.markdown("### 📈 Operating Trends")
    trends_defaults = {
        'burner_pressure': 3.5,
        'draft_pressure': -2.0,
        'min_skin_coils_temp': 450.0,
        'max_skin_coils_temp': 500.0,
        'avg_skin_coils_temp': 475.0
    }

    for spec in trends_inputs:
        key = spec.name
        label = f"{spec.desc} ({spec.uom})" if spec.uom else spec.desc
        default_val = trends_defaults.get(key, 0.0)
        st.session_state.heater_inputs[key] = st.number_input(
            label,
            value=st.session_state.heater_inputs.get(key, default_val),
            step=0.1,
            key=f"input_{key}"
        )

    # CEMS Data
    st.markdown("### 🔬 CEMS Data")
    cems_defaults = {
        'dust_analyzer': 10.0,
        'flue_gas_sox_analyzer': 50.0,
        'flue_gas_nox_analyzer': 100.0,
        'flue_gas_co_analyzer': 150.0,
        'flue_gas_o2_analyzer': 4.2,
        'flue_gas_flow': 10000.0,
        'flue_gas_pressure': 1.0,
        'flue_gas_temp': 240.0
    }

    for spec in cems_inputs:
        key = spec.name
        label = f"{spec.desc} ({spec.uom})" if spec.uom else spec.desc
        default_val = cems_defaults.get(key, 0.0)
        st.session_state.heater_inputs[key] = st.number_input(
            label,
            value=st.session_state.heater_inputs.get(key, default_val),
            step=0.1,
            key=f"input_{key}"
        )

    # Constants
    st.markdown("### 🔢 Constants")
    constants_defaults = {
        'sea_level_pressure': 1013.0,
        'relative_humidity': 60.0,
        'altitude': 0.0,
        'radiation_loss': 3.0
    }

    for spec in constants_inputs:
        key = spec.name
        label = f"{spec.desc} ({spec.uom})" if spec.uom else spec.desc
        default_val = constants_defaults.get(key, 0.0)
        st.session_state.heater_inputs[key] = st.number_input(
            label,
            value=st.session_state.heater_inputs.get(key, default_val),
            step=0.1,
            key=f"input_{key}"
        )

    # Design Efficiency Targets
    st.markdown("### 🎯 Design Efficiency Targets")
    st.info("💡 **Note:** These values can be found in the fired heater datasheet or design specifications.")

    # Radio button to select which efficiency to input
    efficiency_input_mode = st.radio(
        "Select which design efficiency to input:",
        ["Design Thermal Efficiency", "Design Fuel Efficiency", "Input Both"],
        key="efficiency_mode"
    )

    if efficiency_input_mode == "Design Thermal Efficiency":
        design_thermal_eff = st.number_input(
            "Design Thermal Efficiency (%)",
            value=st.session_state.get('design_thermal_eff', 85.0),
            min_value=50.0,
            max_value=95.0,
            step=0.1,
            help="Thermal efficiency from heater datasheet",
            key="design_thermal_input"
        )
        st.session_state.design_thermal_eff = design_thermal_eff
        st.session_state.design_fuel_eff = None  # Will be calculated
        st.info("🔄 Design Fuel Efficiency will be calculated automatically based on fuel composition")

    elif efficiency_input_mode == "Design Fuel Efficiency":
        design_fuel_eff = st.number_input(
            "Design Fuel Efficiency (%)",
            value=st.session_state.get('design_fuel_eff', 87.0),
            min_value=50.0,
            max_value=95.0,
            step=0.1,
            help="Fuel efficiency from heater datasheet",
            key="design_fuel_input"
        )
        st.session_state.design_fuel_eff = design_fuel_eff
        st.session_state.design_thermal_eff = None  # Will be calculated
        st.info("🔄 Design Thermal Efficiency will be calculated automatically based on fuel composition")

    else:  # Input Both
        design_thermal_eff = st.number_input(
            "Design Thermal Efficiency (%)",
            value=st.session_state.get('design_thermal_eff', 85.0),
            min_value=50.0,
            max_value=95.0,
            step=0.1,
            help="Thermal efficiency from heater datasheet",
            key="design_thermal_both"
        )
        design_fuel_eff = st.number_input(
            "Design Fuel Efficiency (%)",
            value=st.session_state.get('design_fuel_eff', 87.0),
            min_value=50.0,
            max_value=95.0,
            step=0.1,
            help="Fuel efficiency from heater datasheet",
            key="design_fuel_both"
        )
        st.session_state.design_thermal_eff = design_thermal_eff
        st.session_state.design_fuel_eff = design_fuel_eff

# Calculate button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Calculate Heater Performance", use_container_width=True, type="primary"):
        try:
            # Create heater instance and compute
            heater = Heater(**st.session_state.heater_inputs)
            results = heater.compute()
            st.session_state.results = results

            # Calculate missing design efficiency if needed
            if hasattr(st.session_state, 'design_thermal_eff') and hasattr(st.session_state, 'design_fuel_eff'):
                # Get actual calculated values for precise efficiency relationship
                lhv = results.get('lower_heating_value', 12481.0)  # kcal/kg
                air_sensible = results.get('air_sensible_massic_heat_correction_wet_ha_wet', 49.7)  # kcal/kg
                fuel_sensible = results.get('fuel_sensible_massic_heat_correction_hf', 26.3)  # kcal/kg

                # Calculate the correct ratio based on actual heater model values
                # Ratio = (LHV + Air_Sensible + Fuel_Sensible) / LHV
                total_heat_input = lhv + air_sensible + fuel_sensible
                heat_input_ratio = total_heat_input / lhv

                if st.session_state.design_thermal_eff is None and st.session_state.design_fuel_eff is not None:
                    # Calculate thermal efficiency from fuel efficiency
                    # Thermal_Eff = Fuel_Eff / Ratio
                    st.session_state.design_thermal_eff = st.session_state.design_fuel_eff / heat_input_ratio

                elif st.session_state.design_fuel_eff is None and st.session_state.design_thermal_eff is not None:
                    # Calculate fuel efficiency from thermal efficiency
                    # Fuel_Eff = Thermal_Eff × Ratio
                    st.session_state.design_fuel_eff = st.session_state.design_thermal_eff * heat_input_ratio

            # Display calculated design efficiency if applicable
            if hasattr(st.session_state, 'design_thermal_eff') and hasattr(st.session_state, 'design_fuel_eff'):
                if efficiency_input_mode == "Design Thermal Efficiency":
                    st.info(f"🔄 **Calculated Design Fuel Efficiency:** {st.session_state.design_fuel_eff:.2f}%")
                    st.caption(f"📐 Heat Input Ratio: {heat_input_ratio:.4f} | LHV: {lhv:.1f} | Air: {air_sensible:.1f} | Fuel: {fuel_sensible:.1f} kcal/kg")
                elif efficiency_input_mode == "Design Fuel Efficiency":
                    st.info(f"🔄 **Calculated Design Thermal Efficiency:** {st.session_state.design_thermal_eff:.2f}%")
                    st.caption(f"📐 Heat Input Ratio: {heat_input_ratio:.4f} | LHV: {lhv:.1f} | Air: {air_sensible:.1f} | Fuel: {fuel_sensible:.1f} kcal/kg")

            st.success("✅ Calculation completed successfully!")
        except Exception as e:
            st.error(f"❌ Calculation failed: {str(e)}")
            st.session_state.results = None

# Display results
if 'results' in st.session_state and st.session_state.results:
    results = st.session_state.results

    # Key Performance Indicators
    st.markdown('<h2 class="section-header">📊 Key Performance Indicators</h2>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        thermal_eff = results.get('thermal_efficiency', 0)
        design_thermal_target = getattr(st.session_state, 'design_thermal_eff', 85.0)
        st.metric(
            label="🔥 Thermal Efficiency",
            value=f"{thermal_eff:.2f}%",
            delta=f"{thermal_eff - design_thermal_target:.2f}% from design"
        )

    with col2:
        fuel_eff = results.get('fuel_efficiency', 0)
        design_fuel_target = getattr(st.session_state, 'design_fuel_eff', 87.0)
        st.metric(
            label="⛽ Fuel Efficiency",
            value=f"{fuel_eff:.2f}%",
            delta=f"{fuel_eff - design_fuel_target:.2f}% from design"
        )

    with col3:
        excess_air = results.get('excess_air', 0)
        st.metric(
            label="💨 Excess Air",
            value=f"{excess_air:.1f}%",
            delta=f"{20 - excess_air:.1f}% from optimal" if excess_air > 20 else f"Optimal range"
        )

    with col4:
        ghg_rate = results.get('ghg_rate', 0)
        st.metric(
            label="🌍 GHG Rate",
            value=f"{ghg_rate:.3f} Ton CO2/h",
            delta=None
        )

    # Performance Chart
    st.markdown('<h2 class="section-header">📈 Performance Overview</h2>', unsafe_allow_html=True)

    # Create performance comparison chart
    design_thermal_target = getattr(st.session_state, 'design_thermal_eff', 85.0)
    design_fuel_target = getattr(st.session_state, 'design_fuel_eff', 87.0)

    performance_data = {
        'Metric': ['Thermal Efficiency', 'Fuel Efficiency', 'Excess Air Ratio'],
        'Actual': [thermal_eff, fuel_eff, excess_air/20*100],  # Normalize excess air
        'Design Target': [design_thermal_target, design_fuel_target, 100],  # Design values
        'Units': ['%', '%', '% of Optimal']
    }

    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Actual',
        x=performance_data['Metric'],
        y=performance_data['Actual'],
        marker_color='#0ea5e9',
        text=[f"{val:.1f}%" for val in performance_data['Actual']],
        textposition='auto',
        textfont=dict(size=14, color='white', family='Arial Black')
    ))

    fig.add_trace(go.Bar(
        name='Design Target',
        x=performance_data['Metric'],
        y=performance_data['Design Target'],
        marker_color='#38bdf8',
        text=[f"{val:.1f}%" for val in performance_data['Design Target']],
        textposition='auto',
        textfont=dict(size=14, color='white', family='Arial Black')
    ))

    fig.update_layout(
        title="Performance vs Design Target Values",
        barmode='group',
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    # Detailed Results by Section
    st.markdown('<h2 class="section-header">📋 Detailed Results</h2>', unsafe_allow_html=True)

    # Group outputs by section
    sections_to_show = [
        'Fuel data',
        'Heater performance Based on Wet Analyzer',
        'Heater performance Based on Dry Analyzer',
        'Fuel Gas Composition',
        'Calculations'
    ]

    for section_name in sections_to_show:
        if section_name in OUTPUT_SECTIONS:
            with st.expander(f"🔍 {section_name}", expanded=(section_name in ['Fuel data', 'Heater performance Based on Wet Analyzer'])):
                output_names = OUTPUT_SECTIONS[section_name]

                # Create DataFrame for this section
                section_data = []
                for output_name in output_names:
                    if output_name in results:
                        # Find the spec for units
                        spec = next((s for s in OUTPUT_SPECS if s.name == output_name), None)
                        unit = spec.uom if spec and spec.uom else ""
                        description = spec.desc if spec and spec.desc else output_name

                        section_data.append({
                            'Parameter': description,
                            'Value': f"{results[output_name]:.4f}",
                            'Unit': unit
                        })

                if section_data:
                    df = pd.DataFrame(section_data)

                    # Style the dataframe
                    st.markdown(
                        f'<div class="expander-content">',
                        unsafe_allow_html=True
                    )

                    # Display as formatted table
                    for _, row in df.iterrows():
                        col1, col2, col3 = st.columns([2, 1, 1])
                        with col1:
                            st.write(f"**{row['Parameter']}**")
                        with col2:
                            st.write(row['Value'])
                        with col3:
                            st.write(row['Unit'])

                    st.markdown('</div>', unsafe_allow_html=True)

    # Energy Balance Visualization
    st.markdown('<h2 class="section-header">⚡ Energy Balance</h2>', unsafe_allow_html=True)

    absorbed_duty = results.get('absorbed_duty', 0)
    radiant_duty = results.get('radiant_duty', 0)
    convection_duty = results.get('convection_duty', 0)
    heater_librated_heat = results.get('heater_librated_heat', 0)

    # Create energy balance pie chart
    energy_data = {
        'Energy Type': ['Radiant Duty', 'Convection Duty', 'Stack Losses'],
        'Value': [
            radiant_duty,
            convection_duty,
            heater_librated_heat - absorbed_duty
        ],
        'Colors': ['#0ea5e9', '#38bdf8', '#7dd3fc']
    }

    fig_pie = go.Figure(data=[go.Pie(
        labels=energy_data['Energy Type'],
        values=energy_data['Value'],
        hole=.3,
        marker_colors=energy_data['Colors'],
        textinfo='label+percent',
        textfont=dict(size=14, color='white', family='Arial Black'),
        marker=dict(line=dict(color='#0a0e27', width=2))
    )])

    fig_pie.update_layout(
        title="Energy Distribution",
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=400
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        st.plotly_chart(fig_pie, use_container_width=True)

    with col2:
        st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
        st.markdown("### 📈 Performance Summary")
        st.write(f"**Total Heat Liberation:** {heater_librated_heat:.3f} Gcal/h")
        st.write(f"**Absorbed Duty:** {absorbed_duty:.3f} Gcal/h")
        st.write(f"**Stack Losses:** {heater_librated_heat - absorbed_duty:.3f} Gcal/h")
        st.write(f"**Heat Absorption Efficiency:** {(absorbed_duty/heater_librated_heat)*100:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: rgba(255, 255, 255, 0.6);">🔥 Heater Efficiency Calculator | Based on API-560 Standards | Developed by Ahmed Mohamed Sabri</p>',
    unsafe_allow_html=True
)