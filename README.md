# 🔥 Heater Efficiency Calculator

A stunning Streamlit web application for calculating heater efficiency based on API-560 standards. This application wraps around the core Python heater model to provide an intuitive, visual interface for heater performance analysis.

## ✨ Features

- **🎯 Interactive Input Interface**: Organized input sections for all heater parameters
- **📊 Real-time Calculations**: Instant computation of heater performance metrics
- **🎨 Modern UI**: Beautiful gradient design with glass morphism effects
- **📈 Visualizations**: Interactive charts and graphs using Plotly
- **⚡ Energy Balance**: Visual representation of energy distribution
- **🔍 Expandable Sections**: Detailed results organized by categories
- **📱 Responsive Design**: Works on desktop and mobile devices

## 🏗️ Application Structure

### Input Categories:
1. **🎯 Basic Operating Parameters**
   - Fuel gas flow, temperature
   - Air temperature, O2 analyzer readings
   - Stack temperature, arch temperature

2. **🧪 Fuel Gas Composition**
   - Complete hydrocarbon composition (C1-C6+)
   - Inert gases (N2, CO2, H2S)
   - Hydrogen content

3. **📈 Operating Trends**
   - Burner and draft pressures
   - Coil skin temperatures (min/max/avg)

4. **🔬 CEMS Data**
   - Emissions monitoring data
   - Flue gas analyzers

5. **🔢 Constants**
   - Environmental conditions
   - System constants

### Output Sections:
- **📊 Key Performance Indicators**: Main efficiency metrics
- **📈 Performance Overview**: Comparison charts
- **🔍 Detailed Results**: Section-wise calculations
- **⚡ Energy Balance**: Energy distribution visualization

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd /home/amsamms/projects/Heater_effeciency_streamlit
   ```

2. **Activate the virtual environment**
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies** (if not already installed)
   ```bash
   pip install streamlit pandas numpy plotly
   ```

4. **Run the application**
   ```bash
   streamlit run heater_app.py
   ```

5. **Open your browser** and navigate to `http://localhost:8501`

## 📊 Using the Application

1. **Input Parameters**: Use the sidebar to enter all required parameters
   - Default values are provided for quick testing
   - All inputs are organized by category for easy navigation

2. **Calculate**: Click the "🚀 Calculate Heater Performance" button
   - The application will process all inputs using the core heater model
   - Results will be displayed immediately

3. **View Results**:
   - **KPIs**: Key metrics displayed at the top
   - **Charts**: Interactive performance visualizations
   - **Detailed Data**: Expandable sections with complete results
   - **Energy Balance**: Visual representation of heat distribution

## 🎨 Design Features

- **Gradient Background**: Beautiful purple-blue gradient theme
- **Glass Morphism**: Modern translucent elements with blur effects
- **Interactive Charts**: Plotly-powered visualizations
- **Responsive Layout**: Adapts to different screen sizes
- **Color-coded Metrics**: Visual indicators for performance levels

## 🔧 Technical Details

- **Backend**: `heater_model.py` - Core calculation engine based on API-560
- **Frontend**: `heater_app.py` - Streamlit web interface
- **Visualizations**: Plotly for interactive charts and graphs
- **Styling**: Custom CSS for modern, appealing interface

## 📈 Key Metrics Calculated

- **Thermal Efficiency**: Overall heater thermal performance
- **Fuel Efficiency**: Fuel utilization effectiveness
- **Excess Air**: Combustion air optimization
- **GHG Emissions**: Environmental impact assessment
- **Energy Distribution**: Radiant vs convection duties
- **Stack Losses**: Heat losses through flue gas

## 🛠️ Customization

The application is highly customizable:
- Modify input defaults in the sidebar sections
- Adjust visualization themes and colors
- Add new calculated parameters
- Extend output sections

## 📝 Notes

- All calculations are based on the tested `heater_model.py`
- Input validation ensures reliable calculations
- Results match Excel reference file accuracy
- Designed for both quick analysis and detailed study

## 👨‍💻 Developer

**Ahmed Mohamed Sabri**
- Email: ahmedsabri85@gmail.com
- GitHub: @amsamms

---

*🔥 Advanced heater efficiency calculations made beautiful and accessible*