"""
Auto-generated Heater model scaffolding from: Heater Eff Ahmed Adel rev03.xlsx
Sheet: Heater Calculations
Generated: 2025-08-17T07:05:56
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional, List
import math
import re
import collections

# --------------------------
# Specs (from the spreadsheet)
# --------------------------
@dataclass(frozen=True)
class InputSpec:
    name: str
    desc: str
    uom: Optional[str] = None
    row: Optional[int] = None

@dataclass(frozen=True)
class OutputSpec:
    name: str
    desc: str
    uom: Optional[str] = None
    section: Optional[str] = None
    row: Optional[int] = None
    excel_formula: Optional[str] = None
    computed_snapshot: Optional[float] = None

INPUT_SPECS: List[InputSpec] = [
    InputSpec(name='fuel_gas_flow_corrected', desc='Fuel Gas Flow corrected', uom='Nm3/h', row=3),
    InputSpec(name='fuel_gas_temp', desc='Fuel Gas Temp.', uom='°C', row=4),
    InputSpec(name='air_temperature', desc='Air Temperature', uom='°C', row=5),
    InputSpec(name='o2_analyzer', desc='O2 Analyzer', uom='Wet % Vol.', row=6),
    InputSpec(name='stack_temp', desc='Stack Temp', uom='°C', row=7),
    InputSpec(name='arch_temp_bwt', desc='Arch Temp. (BWT)', uom='°C', row=8),
    InputSpec(name='fuel_gas_composition', desc='Fuel Gas Composition', uom=None, row=9),
    InputSpec(name='c1', desc='C1', uom='% mol', row=10),
    InputSpec(name='c2', desc='C2', uom='% mol', row=11),
    InputSpec(name='c2_unsat', desc='C2=', uom='% mol', row=12),
    InputSpec(name='c3', desc='C3', uom='% mol', row=13),
    InputSpec(name='c3_unsat', desc='C3=', uom='% mol', row=14),
    InputSpec(name='i_c4', desc='i-C4', uom='% mol', row=15),
    InputSpec(name='n_c4', desc='n-C4', uom='% mol', row=16),
    InputSpec(name='c4_unsat', desc='C4=', uom='% mol', row=17),
    InputSpec(name='c5', desc='C5', uom='% mol', row=18),
    InputSpec(name='c6', desc='C6+', uom='% mol', row=19),
    InputSpec(name='n2', desc='N2', uom='% mol', row=20),
    InputSpec(name='h2', desc='H2', uom='% mol', row=21),
    InputSpec(name='O2_argon', desc='02/Argon', uom='% mol', row=22),
    InputSpec(name='co', desc='CO', uom='% mol', row=23),
    InputSpec(name='co2', desc='CO2', uom='% mol', row=24),
    InputSpec(name='h2s', desc='H2S', uom='% mol', row=25),
    InputSpec(name='trends', desc='Trends', uom=None, row=26),
    InputSpec(name='burner_pressure', desc='Burner Pressure', uom='barg', row=27),
    InputSpec(name='draft_pressure', desc='Draft Pressure', uom='mm H2O', row=28),
    InputSpec(name='min_skin_coils_temp', desc='Min Skin Coils Temp.', uom='°C', row=29),
    InputSpec(name='max_skin_coils_temp', desc='Max Skin Coils Temp.', uom='°C', row=30),
    InputSpec(name='avg_skin_coils_temp', desc='Avg. Skin Coils Temp.', uom='°C', row=31),
    InputSpec(name='continuous_emission_monitoring_system_cems', desc='Continuous Emission Monitoring System (CEMS)', uom=None, row=32),
    InputSpec(name='dust_analyzer', desc='Dust Analyzer', uom='mg/Nm3', row=33),
    InputSpec(name='flue_gas_sox_analyzer', desc='Flue Gas SOx Analyzer', uom='mg/Nm3', row=34),
    InputSpec(name='flue_gas_nox_analyzer', desc='Flue Gas NOx Analyzer', uom='mg/Nm3', row=35),
    InputSpec(name='flue_gas_co_analyzer', desc='Flue Gas CO Analyzer', uom='mg/Nm3', row=36),
    InputSpec(name='flue_gas_o2_analyzer', desc='Flue Gas O2 Analyzer', uom='Dry % Vol.', row=37),
    InputSpec(name='flue_gas_flow', desc='Flue Gas Flow', uom='Nm3/hr', row=38),
    InputSpec(name='flue_gas_pressure', desc='Flue Gas Pressure', uom='mbar', row=39),
    InputSpec(name='flue_gas_temp', desc='Flue Gas Temp.', uom='°C', row=40),
    InputSpec(name='constants', desc='Constants', uom=None, row=41),
    InputSpec(name='sea_level_pressure', desc='Sea level Pressure', uom='hPa', row=42),
    InputSpec(name='relative_humidity', desc='Relative Humidity', uom='%', row=43),
    InputSpec(name='altitude', desc='Altitude', uom='m', row=44),
    InputSpec(name='radiation_loss', desc='Radiation Loss', uom='%', row=45),
]

OUTPUT_SPECS: List[OutputSpec] = [
    OutputSpec(name='molecular_weight', desc='Molecular Weight', uom='Kg/Kg mole', section='Fuel data', row=50, excel_formula='=C464', computed_snapshot=14.721108495178662),
    OutputSpec(name='lower_heating_value', desc='Lower Heating Value', uom='Kcal/Kg', section='Fuel data', row=51, excel_formula='=C190', computed_snapshot=12481.056546241161),
    OutputSpec(name='lower_heating_value_nm3', desc='Lower Heating Value', uom='Kcal/NM3', section='Fuel data', row=52, excel_formula='=C51*C50/22.414', computed_snapshot=8197.33146924583),
    OutputSpec(name='ghg_Ton CO2/Kg Fuel', desc='GHG', uom='Ton CO2/Kg Fuel', section='Fuel data', row=53, excel_formula='=C508', computed_snapshot=0.0026997287877411334),
    OutputSpec(name='ghg_Ton CO2/Nm3 Fuel',  desc='GHG', uom='Ton CO2/Nm3 Fuel',  section='Fuel data', row=54, excel_formula='=C509', computed_snapshot=0.0018721113284108143),
    OutputSpec(name='ghg_Ton CO2/Gcal Fuel', desc='GHG', uom='Ton CO2/Gcal Fuel', section='Fuel data', row=55, excel_formula='=C510', computed_snapshot=0.2252116851952069),
    OutputSpec(name='flue_gas_acid_dewpoint', desc='Flue Gas Acid dewpoint', uom='°C', section='Fuel data', row=56, excel_formula='=C505', computed_snapshot=94.37477113621881),
    OutputSpec(name='excess_air', desc='Excess Air', uom='%', section='Heater performance Based on Wet Analyzer', row=59, excel_formula='=C366', computed_snapshot=25.586438900926286),
    OutputSpec(name='thermal_efficiency', desc='Thermal Efficiency', uom='%', section='Heater performance Based on Wet Analyzer', row=60, excel_formula='=C409', computed_snapshot=86.97263442103639),
    OutputSpec(name='fuel_efficiency', desc='Fuel  Efficiency', uom='%', section='Heater performance Based on Wet Analyzer', row=61, excel_formula='=C411', computed_snapshot=87.50222394974901),
    OutputSpec(name='heater_librated_heat', desc='Heater Librated Heat', uom='=Gcal/h', section='Heater performance Based on Wet Analyzer', row=62, excel_formula='=C420', computed_snapshot=7.240932206765787),
    OutputSpec(name='absorbed_duty', desc='Absorbed Duty', uom='=Gcal/h', section='Heater performance Based on Wet Analyzer', row=63, excel_formula='=C421', computed_snapshot=6.297629496865491),
    OutputSpec(name='radiant_duty', desc='Radiant Duty', uom='=Gcal/h', section='Heater performance Based on Wet Analyzer', row=64, excel_formula='=C423', computed_snapshot=4.6341509956091755),
    OutputSpec(name='convection_duty', desc='Convection Duty', uom='=Gcal/h', section='Heater performance Based on Wet Analyzer', row=65, excel_formula='=C425', computed_snapshot=1.6634785012563151),
    OutputSpec(name='flue_gas_flow', desc='Flue Gas Flow', uom='Nm3/h', section='Heater performance Based on Wet Analyzer', row=66, excel_formula='=C529', computed_snapshot=10777.249175438252),
    OutputSpec(name='ghg_rate', desc='GHG Rate', uom='Ton CO2/h', section='Heater performance Based on Wet Analyzer', row=67, excel_formula='=C511', computed_snapshot=1.566257876988374),
    OutputSpec(name='expected_o2_dry_analyzer', desc='Expected O2 Dry Analyzer', uom='Mole %', section='Heater performance Based on Wet Analyzer', row=68, excel_formula='=C528/(C528+C527+C526)*100', computed_snapshot=4.21300402091054),
    OutputSpec(name='excess_air_dry', desc='Excess Air', uom='%', section='Heater performance Based on Dry Analyzer', row=71, excel_formula='=C370', computed_snapshot=31.11948499074093),
    OutputSpec(name='thermal_efficiency_dry', desc='Thermal Efficiency', uom='%', section='Heater performance Based on Dry Analyzer', row=72, excel_formula='=C413', computed_snapshot=86.97489765435608),
    OutputSpec(name='fuel_efficiency_dry', desc='Fuel  Efficiency', uom='%', section='Heater performance Based on Dry Analyzer', row=73, excel_formula='=C415', computed_snapshot=87.51970568946476),
    OutputSpec(name='heater_librated_heat_dry', desc='Heater Librated Heat', uom='Gcal/hr', section='Heater performance Based on Dry Analyzer', row=74, excel_formula='=C420', computed_snapshot=7.240932206765787),
    OutputSpec(name='absorbed_duty_dry', desc='Absorbed Duty', uom='Gcal/hr', section='Heater performance Based on Dry Analyzer', row=75, excel_formula='=C422', computed_snapshot=6.297793376055851),
    OutputSpec(name='radiant_duty_dry', desc='Radiant Duty', uom='Gcal/hr', section='Heater performance Based on Dry Analyzer', row=76, excel_formula='=C424', computed_snapshot=4.57091315651099),
    OutputSpec(name='convection_duty_dry', desc='Convection Duty', uom='Gcal/hr', section='Heater performance Based on Dry Analyzer', row=77, excel_formula='=C426', computed_snapshot=1.726880219544861),
    OutputSpec(name='flue_gas_flow_rate', desc='Flue Gas Flow Rate', uom='Nm3/h', section='Heater performance Based on Dry Analyzer', row=78, excel_formula='=C542', computed_snapshot=1757.825757318079),
    OutputSpec(name="ghg_rate_dry", desc='GHG Rate', uom='Ton CO2/h', section='Heater performance Based on Dry Analyzer', row=79, excel_formula='=C67', computed_snapshot=1.566257876988374),
    OutputSpec(name='expected_o2_wet_analyzer', desc='Expected O2 Wet Analyzer', uom='Mole %', section='Heater performance Based on Dry Analyzer', row=80, excel_formula='=C545/C546*100', computed_snapshot=4.121824942343213),
    OutputSpec(name='actual_air_pressur', desc='Actual Air Pressur', uom='hPa', section='Calculations', row=85, excel_formula='=IF(C42="","",C42*EXP(-9.80665*0.0289644*C44/(8.31432*(C5+273.16))))', computed_snapshot=1013),
    OutputSpec(name='stuaration_vapor_pressure', desc='Stuaration vapor pressure', uom='Pa', section='Calculations', row=86, excel_formula='=IF(C42="","",610.78*10^(7.5*C5/(C5+237.3)))', computed_snapshot=3167.489286056397),
    OutputSpec(name='water_vapor_pressure', desc='Water vapor pressure', uom='Pa', section='Calculations', row=87, excel_formula='=IF(C42="","",C86*C43/100)', computed_snapshot=1583.7446430281984),
    OutputSpec(name='water_vapor_pressure_mbar', desc='Water vapor pressure', uom='mbar', section='Calculations', row=88, excel_formula='=C87/100', computed_snapshot=18.89),
    OutputSpec(name='stack_temp_before_damper_calculated', desc='Stack Temp. Before Damper Calculated', uom='R', section='Calculations', row=89, excel_formula='=IF(C7="","",C7*9/5+491.67)', computed_snapshot=925.5948035430908),
    OutputSpec(name='bwt_temp_calculated', desc='BWT Temp Calculated', uom='R', section='Calculations', row=90, excel_formula='=IF(C8="","",C8*9/5+491.67)', computed_snapshot=1702.646010131836),
    OutputSpec(name='air_temperature_calculated', desc='Air Temperature calculated', uom='°F', section='Calculations', row=91, excel_formula='=C5*1.8+32', computed_snapshot=77),
    OutputSpec(name='air_temperature', desc='Air Temperature', uom='°R', section='Calculations', row=92, excel_formula='=IF(C5="","",C5*9/5+491.67)', computed_snapshot=536.6700000000001),
    OutputSpec(name='c1', desc='C1', uom='% mol', section='Fuel Gas Composition', row=95, excel_formula='=C10/SUM($C$10:$C$25)*100', computed_snapshot=33.47273122572164),
    OutputSpec(name='c2', desc='C2', uom='% mol', section='Fuel Gas Composition', row=96, excel_formula='=C11/SUM($C$10:$C$25)*100', computed_snapshot=8.800129491756776),
    OutputSpec(name="c2_fuel_gas", desc='C2=', uom='% mol', section='Fuel Gas Composition', row=97, excel_formula='=C12/SUM($C$10:$C$25)*100', computed_snapshot=0),
    OutputSpec(name='c3', desc='C3', uom='% mol', section='Fuel Gas Composition', row=98, excel_formula='=C13/SUM($C$10:$C$25)*100', computed_snapshot=5.944501813662963),
    OutputSpec(name="c3_fuel_gas", desc='C3=', uom='% mol', section='Fuel Gas Composition', row=99, excel_formula='=C14/SUM($C$10:$C$25)*100', computed_snapshot=0),
    OutputSpec(name='i_c4', desc='i-C4', uom='% mol', section='Fuel Gas Composition', row=100, excel_formula='=C15/SUM($C$10:$C$25)*100', computed_snapshot=2.439145683343124),
    OutputSpec(name='n_c4', desc='n-C4', uom='% mol', section='Fuel Gas Composition', row=101, excel_formula='=C16/SUM($C$10:$C$25)*100', computed_snapshot=2.2769544751939983),
    OutputSpec(name='c4', desc='C4=', uom='% mol', section='Fuel Gas Composition', row=102, excel_formula='=C17/SUM($C$10:$C$25)*100', computed_snapshot=0),
    OutputSpec(name='c5', desc='C5', uom='% mol', section='Fuel Gas Composition', row=103, excel_formula='=C18/SUM($C$10:$C$25)*100', computed_snapshot=0.49109421659751423),
    OutputSpec(name='c6', desc='C6+', uom='% mol', section='Fuel Gas Composition', row=104, excel_formula='=C19/SUM($C$10:$C$25)*100', computed_snapshot=0),
    OutputSpec(name='n2', desc='N2', uom='% mol', section='Fuel Gas Composition', row=105, excel_formula='=C20/SUM($C$10:$C$25)*100', computed_snapshot=0),
    OutputSpec(name='h2', desc='H2', uom='% mol', section='Fuel Gas Composition', row=106, excel_formula='=C21/SUM($C$10:$C$25)*100', computed_snapshot=46.458612725996716),
    OutputSpec(name='v_02_argon', desc='02/Argon', uom='% mol', section='Fuel Gas Composition', row=107, excel_formula='=C22/SUM($C$10:$C$25)*100', computed_snapshot=0),
    OutputSpec(name='co', desc='CO', uom='% mol', section='Fuel Gas Composition', row=108, excel_formula='=C23/SUM($C$10:$C$25)*100', computed_snapshot=0),
    OutputSpec(name='co2', desc='CO2', uom='% mol', section='Fuel Gas Composition', row=109, excel_formula='=C24/SUM($C$10:$C$25)*100', computed_snapshot=0.11677198173640109),
    OutputSpec(name='h2s', desc='H2S', uom='% mol', section='Fuel Gas Composition', row=110, excel_formula='=C25/SUM($C$10:$C$25)*100', computed_snapshot=5.838599086820055e-05),
    OutputSpec(name='total', desc='Total', uom=None, section='Fuel Gas Composition', row=111, excel_formula='=IF(C95="","",SUM(C95:C110))', computed_snapshot=100.00000000000001),
    OutputSpec(name="c1_mw", desc='C1', uom='kg/kg mole', section='MW', row=115, excel_formula='=16.043', computed_snapshot=16.043),
    OutputSpec(name="c2_mw", desc='C2', uom='kg/kg mole', section='MW', row=116, excel_formula='=30.07', computed_snapshot=30.07),
    OutputSpec(name="c2_unsat_mw", desc='C2=', uom='kg/kg mole', section='MW', row=117, excel_formula='=28.054', computed_snapshot=28.054),
    OutputSpec(name="c3_mw", desc='C3', uom='kg/kg mole', section='MW', row=118, excel_formula='=44.097', computed_snapshot=44.097),
    OutputSpec(name="c3_unsat_mw", desc='C3=', uom='kg/kg mole', section='MW', row=119, excel_formula='=42.081', computed_snapshot=42.081),
    OutputSpec(name="i_c4_mw", desc='i-C4', uom='kg/kg mole', section='MW', row=120, excel_formula='=58.124', computed_snapshot=58.124),
    OutputSpec(name="n_c4_mw", desc='n-C4', uom='kg/kg mole', section='MW', row=121, excel_formula='=58.124', computed_snapshot=58.124),
    OutputSpec(name="c4_mw", desc='C4=', uom='kg/kg mole', section='MW', row=122, excel_formula='=56.108', computed_snapshot=56.108),
    OutputSpec(name="c5_mw", desc='C5', uom='kg/kg mole', section='MW', row=123, excel_formula='=72.151', computed_snapshot=72.151),
    OutputSpec(name="c6_mw", desc='C6+', uom='kg/kg mole', section='MW', row=124, excel_formula='=86.178', computed_snapshot=86.178),
    OutputSpec(name="n2_mw", desc='N2', uom='kg/kg mole', section='MW', row=125, excel_formula='=28.013', computed_snapshot=28.013),
    OutputSpec(name="h2_mw", desc='H2', uom='kg/kg mole', section='MW', row=126, excel_formula='=2.016', computed_snapshot=2.016),
    OutputSpec(name="v_02_argon_mw", desc='02/Argon', uom='kg/kg mole', section='MW', row=127, excel_formula='=31.999', computed_snapshot=31.999),
    OutputSpec(name="co_mw", desc='CO', uom='kg/kg mole', section='MW', row=128, excel_formula='=28.01', computed_snapshot=28.01),
    OutputSpec(name="co2_mw", desc='CO2', uom='kg/kg mole', section='MW', row=129, excel_formula='=44.01', computed_snapshot=44.01),
    OutputSpec(name="h2s_mw", desc='H2S', uom='kg/kg mole', section='MW', row=130, excel_formula='=34.076', computed_snapshot=34.076),
    OutputSpec(name="c1_mass_kg", desc='C1', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=134, excel_formula='=IF(C95="","",C95*C115/100)', computed_snapshot=5.3700302705425225),
    OutputSpec(name="c2_mass_kg", desc='C2', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=135, excel_formula='=IF(C96="","",C96*C116/100)', computed_snapshot=2.6461989381712625),
    OutputSpec(name="c2_unsat_mass_kg", desc='C2=', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=136, excel_formula='=IF(C97="","",C97*C117/100)', computed_snapshot=0),
    OutputSpec(name="c3_mass_kg", desc='C3', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=137, excel_formula='=IF(C98="","",C98*C118/100)', computed_snapshot=2.6213469647709564),
    OutputSpec(name="c3_unsat_mass_kg", desc='C3=', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=138, excel_formula='=IF(C99="","",C99*C119/100)', computed_snapshot=0),
    OutputSpec(name="i_c4_mass_kg", desc='i-C4', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=139, excel_formula='=IF(C100="","",C100*C120/100)', computed_snapshot=1.4177290369863575),
    OutputSpec(name="n_c4_mass_kg", desc='n-C4', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=140, excel_formula='=IF(C101="","",C101*C121/100)', computed_snapshot=1.3234570191617596),
    OutputSpec(name="c4_mass_kg", desc='C4=', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=141, excel_formula='=IF(C102="","",C102*C122/100)', computed_snapshot=0),
    OutputSpec(name="c5_mass_kg", desc='C5', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=142, excel_formula='=IF(C103="","",C103*C123/100)', computed_snapshot=0.3543293882172725),
    OutputSpec(name="c6_mass_kg", desc='C6+', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=143, excel_formula='=IF(C104="","",C104*C124/100)', computed_snapshot=0),
    OutputSpec(name="n2_mass_kg", desc='N2', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=144, excel_formula='=IF(C105="","",C105*C125/100)', computed_snapshot=0),
    OutputSpec(name="h2_mass_kg", desc='H2', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=145, excel_formula='=IF(C106="","",C106*C126/100)', computed_snapshot=0.9366056325560937),
    OutputSpec(name="v_02_argon_mass_kg", desc='02/Argon', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=146, excel_formula='=IF(C107="","",C107*C127/100)', computed_snapshot=0),
    OutputSpec(name="co_mass_kg", desc='CO', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=147, excel_formula='=IF(C108="","",C108*C128/100)', computed_snapshot=0),
    OutputSpec(name="co2_mass_kg", desc='CO2', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=148, excel_formula='=IF(C109="","",C109*C129/100)', computed_snapshot=0.05139134916219012),
    OutputSpec(name="h2s_mass_kg", desc='H2S', uom='kg', section='( 1 X 2 ) - Total Mass (kg)', row=149, excel_formula='=IF(C110="","",C110*C130/100)', computed_snapshot=1.989561024824802e-05),
    OutputSpec(name="total_mass_kg", desc='Total', uom='kg Fuel', section='( 1 X 2 ) - Total Mass (kg)', row=150, excel_formula='=IF(C134="","",SUM(C134:C149))', computed_snapshot=14.721108495178665),
    OutputSpec(name="c1_row_154", desc='C1', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=154, excel_formula='=11949.4444444444', computed_snapshot=11949.4444444444),
    OutputSpec(name="c2_row_155", desc='C2', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=155, excel_formula='=11348.3333333333', computed_snapshot=11348.3333333333),
    OutputSpec(name="c2_row_156", desc='C2=', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=156, excel_formula='=11263.8888888889', computed_snapshot=11263.8888888889),
    OutputSpec(name="c3_row_157", desc='C3', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=157, excel_formula='=11066.6666666667', computed_snapshot=11066.6666666667),
    OutputSpec(name="c3_row_158", desc='C3=', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=158, excel_formula='=10930.5555555556', computed_snapshot=10930.5555555556),
    OutputSpec(name="i_c4_row_159", desc='i-C4', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=159, excel_formula='=10885.5555555556', computed_snapshot=10885.5555555556),
    OutputSpec(name="n_c4_row_160", desc='n-C4', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=160, excel_formula='=10920', computed_snapshot=10920),
    OutputSpec(name="c4_row_161", desc='C4=', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=161, excel_formula='=10816.111111', computed_snapshot=10816.111111),
    OutputSpec(name="c5_row_162", desc='C5', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=162, excel_formula='=10742.2222222222', computed_snapshot=10742.2222222222),
    OutputSpec(name="c6_row_163", desc='C6+', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=163, excel_formula='=10685', computed_snapshot=10685),
    OutputSpec(name="n2_row_164", desc='N2', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=164, excel_formula='=0', computed_snapshot=0),
    OutputSpec(name="h2_row_165", desc='H2', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=165, excel_formula='=28651.6666666667', computed_snapshot=28651.6666666667),
    OutputSpec(name="v_02_argon_row_166", desc='02/Argon', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=166, excel_formula='=0', computed_snapshot=0),
    OutputSpec(name="co_row_167", desc='CO', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=167, excel_formula='=2413.333333', computed_snapshot=2413.333333),
    OutputSpec(name="co2_row_168", desc='CO2', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=168, excel_formula='=0', computed_snapshot=0),
    OutputSpec(name="h2s_row_169", desc='H2S', uom='kcal / kg', section='Net Heating Value ( kcal/kg )', row=169, excel_formula='=3630', computed_snapshot=3630),
    OutputSpec(name="c1_row_173", desc='C1', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=173, excel_formula='=IF(C134="","",C134*C154)', computed_snapshot=64168.878382832605),
    OutputSpec(name="c2_row_174", desc='C2', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=174, excel_formula='=IF(C135="","",C135*C155)', computed_snapshot=30029.94761668012),
    OutputSpec(name="c2_row_175", desc='C2=', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=175, excel_formula='=IF(C136="","",C136*C156)', computed_snapshot=0),
    OutputSpec(name="c3_row_176", desc='C3', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=176, excel_formula='=IF(C137="","",C137*C157)', computed_snapshot=29009.57307679867),
    OutputSpec(name="c3_row_177", desc='C3=', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=177, excel_formula='=IF(C138="","",C138*C158)', computed_snapshot=0),
    OutputSpec(name="i_c4_row_178", desc='i-C4', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=178, excel_formula='=IF(C139="","",C139*C159)', computed_snapshot=15432.768194839335),
    OutputSpec(name="n_c4_row_179", desc='n-C4', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=179, excel_formula='=IF(C140="","",C140*C160)', computed_snapshot=14452.150649246416),
    OutputSpec(name="c4_row_180", desc='C4=', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=180, excel_formula='=IF(C141="","",C141*C161)', computed_snapshot=0),
    OutputSpec(name="c5_row_181", desc='C5', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=181, excel_formula='=IF(C142="","",C142*C162)', computed_snapshot=3806.285028093982),
    OutputSpec(name="c6_row_182", desc='C6+', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=182, excel_formula='=IF(C143="","",C143*C163)', computed_snapshot=0),
    OutputSpec(name="n2_row_183", desc='N2', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=183, excel_formula='=IF(C144="","",C144*C164)', computed_snapshot=0),
    OutputSpec(name="h2_row_184", desc='H2', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=184, excel_formula='=IF(C145="","",C145*C165)', computed_snapshot=26835.31238211971),
    OutputSpec(name="v_02_argon_row_185", desc='02/Argon', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=185, excel_formula='=IF(C146="","",C146*C166)', computed_snapshot=0),
    OutputSpec(name="co_row_186", desc='CO', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=186, excel_formula='=IF(C147="","",C147*C167)', computed_snapshot=0),
    OutputSpec(name="co2_row_187", desc='CO2', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=187, excel_formula='=IF(C148="","",C148*C168)', computed_snapshot=0),
    OutputSpec(name="h2s_row_188", desc='H2S', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=188, excel_formula='=IF(C149="","",C149*C169)', computed_snapshot=0.07222106520114031),
    OutputSpec(name="total_row_189", desc='Total', uom='kcal', section='( 3 X 4 ) - Heating Value ( kcal )', row=189, excel_formula='=IF(C173="","",SUM(C173:C188))', computed_snapshot=183734.98755167605),
    OutputSpec(name='total_per_kg_of_fuel_hl', desc='Total per kg of Fuel hL', uom='kcal / kg', section='( 3 X 4 ) - Heating Value ( kcal )', row=190, excel_formula='=IF(C189="","",C189/C150)', computed_snapshot=12481.056546241161),
    OutputSpec(name="c1_air_required_total", desc='C1', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=194, excel_formula='=17.24', computed_snapshot=17.24),
    OutputSpec(name="c2_air_required_total", desc='C2', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=195, excel_formula='=16.09', computed_snapshot=16.09),
    OutputSpec(name="c2_unsat_air_required_kg", desc='C2=', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=196, excel_formula='=14.79', computed_snapshot=14.79),
    OutputSpec(name="c3_air_required_total", desc='C3', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=197, excel_formula='=15.68', computed_snapshot=15.68),
    OutputSpec(name="c3_unsat_air_required_kg", desc='C3=', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=198, excel_formula='=14.79', computed_snapshot=14.79),
    OutputSpec(name="i_c4_air_required_total", desc='i-C4', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=199, excel_formula='=15.46', computed_snapshot=15.46),
    OutputSpec(name="n_c4_air_required_total", desc='n-C4', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=200, excel_formula='=15.46', computed_snapshot=15.46),
    OutputSpec(name="c4_air_required_total", desc='C4=', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=201, excel_formula='=14.79', computed_snapshot=14.79),
    OutputSpec(name="c5_air_required_total", desc='C5', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=202, excel_formula='=15.33', computed_snapshot=15.33),
    OutputSpec(name="c6_air_required_total", desc='C6+', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=203, excel_formula='=15.24', computed_snapshot=15.24),
    OutputSpec(name="n2_air_required_total", desc='N2', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=204, excel_formula='=0', computed_snapshot=0),
    OutputSpec(name="h2_air_required_total", desc='H2', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=205, excel_formula='=34.29', computed_snapshot=34.29),
    OutputSpec(name="v_02_argon_air_required_total", desc='02/Argon', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=206, excel_formula='=-4.32', computed_snapshot=-4.32),
    OutputSpec(name="co_air_required_total", desc='CO', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=207, excel_formula='=2.47', computed_snapshot=2.47),
    OutputSpec(name="co2_air_required_total", desc='CO2', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=208, excel_formula='=0', computed_snapshot=0),
    OutputSpec(name="h2s_air_required_total", desc='H2S', uom='kg of Air/kg', section='Air Required ( kg of Air / kg )', row=209, excel_formula='=6.08', computed_snapshot=6.08),
    OutputSpec(name="c1_air_required_total_total_kg", desc='C1', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=213, excel_formula='=IF(C134="","",C134*C194)', computed_snapshot=92.57932186415307),
    OutputSpec(name="c2_air_required_total_total_kg", desc='C2', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=214, excel_formula='=IF(C135="","",C135*C195)', computed_snapshot=42.57734091517561),
    OutputSpec(name="c2_unsat_air_required_total", desc='C2=', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=215, excel_formula='=IF(C136="","",C136*C196)', computed_snapshot=0),
    OutputSpec(name="c3_air_required_total_total_kg", desc='C3', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=216, excel_formula='=IF(C137="","",C137*C197)', computed_snapshot=41.102720407608594),
    OutputSpec(name="c3_unsat_air_required_total", desc='C3=', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=217, excel_formula='=IF(C138="","",C138*C198)', computed_snapshot=0),
    OutputSpec(name="i_c4_air_required_total_total_kg", desc='i-C4', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=218, excel_formula='=IF(C139="","",C139*C199)', computed_snapshot=21.918090911809088),
    OutputSpec(name="n_c4_air_required_total_total_kg", desc='n-C4', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=219, excel_formula='=IF(C140="","",C140*C200)', computed_snapshot=20.460645516240806),
    OutputSpec(name="c4_air_required_total_total_kg", desc='C4=', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=220, excel_formula='=IF(C141="","",C141*C201)', computed_snapshot=0),
    OutputSpec(name="c5_air_required_total_total_kg", desc='C5', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=221, excel_formula='=IF(C142="","",C142*C202)', computed_snapshot=5.431869521370787),
    OutputSpec(name="c6_air_required_total_total_kg", desc='C6+', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=222, excel_formula='=IF(C143="","",C143*C203)', computed_snapshot=0),
    OutputSpec(name="n2_air_required_total_total_kg", desc='N2', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=223, excel_formula='=IF(C144="","",C144*C204)', computed_snapshot=0),
    OutputSpec(name="h2_air_required_total_total_kg", desc='H2', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=224, excel_formula='=IF(C145="","",C145*C205)', computed_snapshot=32.11620714034845),
    OutputSpec(name="v_02_argon_air_required_total_total_kg", desc='02/Argon', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=225, excel_formula='=IF(C146="","",C146*C206)', computed_snapshot=0),
    OutputSpec(name="co_air_required_total_total_kg", desc='CO', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=226, excel_formula='=IF(C147="","",C147*C207)', computed_snapshot=0),
    OutputSpec(name="co2_air_required_total_total_kg", desc='CO2', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=227, excel_formula='=IF(C148="","",C148*C208)', computed_snapshot=0),
    OutputSpec(name="h2s_air_required_total_total_kg", desc='H2S', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=228, excel_formula='=IF(C149="","",C149*C209)', computed_snapshot=0.00012096531030934796),
    OutputSpec(name="total_air_required_total", desc='Total', uom='kg of Air', section='( 3 X 6 ) - Air Required ( kg )', row=229, excel_formula='=IF(C213="","",SUM(C213:C228))', computed_snapshot=256.18631724201674),
    OutputSpec(name='total_per_kg_of_fuel', desc='Total per kg of Fuel', uom='kg of Air/kg Fuel', section='( 3 X 6 ) - Air Required ( kg )', row=230, excel_formula='=IF(C229="","",C229/C150)', computed_snapshot=17.40265125591057),
    OutputSpec(name="c1_co2_formed_total", desc='C1', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=234, excel_formula='=2.74', computed_snapshot=2.74),
    OutputSpec(name="c2_co2_formed_total", desc='C2', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=235, excel_formula='=2.93', computed_snapshot=2.93),
    OutputSpec(name="c2_unsat_co2_formed_kg", desc='C2=', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=236, excel_formula='=3.14', computed_snapshot=3.14),
    OutputSpec(name="c3_co2_formed_total", desc='C3', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=237, excel_formula='=2.99', computed_snapshot=2.99),
    OutputSpec(name="c3_unsat_co2_formed_kg", desc='C3=', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=238, excel_formula='=3.14', computed_snapshot=3.14),
    OutputSpec(name="i_c4_co2_formed_total", desc='i-C4', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=239, excel_formula='=3.03', computed_snapshot=3.03),
    OutputSpec(name="n_c4_co2_formed_total", desc='n-C4', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=240, excel_formula='=3.03', computed_snapshot=3.03),
    OutputSpec(name="c4_co2_formed_total", desc='C4=', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=241, excel_formula='=3.14', computed_snapshot=3.14),
    OutputSpec(name="c5_co2_formed_total", desc='C5', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=242, excel_formula='=3.05', computed_snapshot=3.05),
    OutputSpec(name="c6_co2_formed_total", desc='C6+', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=243, excel_formula='=3.06', computed_snapshot=3.06),
    OutputSpec(name="n2_co2_formed_total", desc='N2', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=244, excel_formula='=0', computed_snapshot=0),
    OutputSpec(name="h2_co2_formed_total", desc='H2', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=245, excel_formula='=0', computed_snapshot=0),
    OutputSpec(name="v_02_argon_co2_formed_total", desc='02/Argon', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=246, excel_formula='=0', computed_snapshot=0),
    OutputSpec(name="co_co2_formed_total", desc='CO', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=247, excel_formula='=1.57', computed_snapshot=1.57),
    OutputSpec(name="co2_co2_formed_total", desc='CO2', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=248, excel_formula='=1', computed_snapshot=1),
    OutputSpec(name="h2s_co2_formed_total", desc='H2S', uom='kg of CO2/kg', section='CO2 Formed ( kg of CO2 / kg )', row=249, excel_formula='=1.88', computed_snapshot=1.88),
    OutputSpec(name="c1_co2_formed_total_co2_total_kg", desc='C1', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=253, excel_formula='=IF(C134="","",C134*C234)', computed_snapshot=14.713882941286514),
    OutputSpec(name="c2_co2_formed_total_co2_total_kg", desc='C2', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=254, excel_formula='=IF(C135="","",C135*C235)', computed_snapshot=7.753362888841799),
    OutputSpec(name="c2_unsat_co2_formed_total", desc='C2=', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=255, excel_formula='=IF(C136="","",C136*C236)', computed_snapshot=0),
    OutputSpec(name="c3_co2_formed_total_co2_total_kg", desc='C3', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=256, excel_formula='=IF(C137="","",C137*C237)', computed_snapshot=7.83782742466516),
    OutputSpec(name="c3_unsat_co2_formed_total", desc='C3=', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=257, excel_formula='=IF(C138="","",C138*C238)', computed_snapshot=0),
    OutputSpec(name="i_c4_co2_formed_total_co2_total_kg", desc='i-C4', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=258, excel_formula='=IF(C139="","",C139*C239)', computed_snapshot=4.295718982068663),
    OutputSpec(name="n_c4_co2_formed_total_co2_total_kg", desc='n-C4', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=259, excel_formula='=IF(C140="","",C140*C240)', computed_snapshot=4.010074768060131),
    OutputSpec(name="c4_co2_formed_total_co2_total_kg", desc='C4=', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=260, excel_formula='=IF(C141="","",C141*C241)', computed_snapshot=0),
    OutputSpec(name="c5_co2_formed_total_co2_total_kg", desc='C5', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=261, excel_formula='=IF(C142="","",C142*C242)', computed_snapshot=1.0807046340626811),
    OutputSpec(name="c6_co2_formed_total_co2_total_kg", desc='C6+', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=262, excel_formula='=IF(C143="","",C143*C243)', computed_snapshot=0),
    OutputSpec(name="n2_co2_formed_total_co2_total_kg", desc='N2', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=263, excel_formula='=IF(C144="","",C144*C244)', computed_snapshot=0),
    OutputSpec(name="h2_co2_formed_total_co2_total_kg", desc='H2', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=264, excel_formula='=IF(C145="","",C145*C245)', computed_snapshot=0),
    OutputSpec(name="v_02_argon_co2_formed_total_co2_total_kg", desc='02/Argon', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=265, excel_formula='=IF(C146="","",C146*C246)', computed_snapshot=0),
    OutputSpec(name="co_co2_formed_total_co2_total_kg", desc='CO', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=266, excel_formula='=IF(C147="","",C147*C247)', computed_snapshot=0),
    OutputSpec(name="co2_co2_formed_total_co2_total_kg", desc='CO2', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=267, excel_formula='=IF(C148="","",C148*C248)', computed_snapshot=0.05139134916219012),
    OutputSpec(name="h2s_co2_formed_total_co2_total_kg", desc='H2S', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=268, excel_formula='=IF(C149="","",C149*C249)', computed_snapshot=3.740374726670628e-05),
    OutputSpec(name="total_co2_formed_total", desc='Total', uom='kg of CO2', section='( 3 X 8 ) - CO2 Formed ( kg )', row=269, excel_formula='=IF(C253="","",SUM(C253:C268))', computed_snapshot=39.7430003918944),
    OutputSpec(name="total_per_kg_of_fuel_co2_formed_total", desc='Total per kg of Fuel', uom='kg of CO2/kg Fuel', section='( 3 X 8 ) - CO2 Formed ( kg )', row=270, excel_formula='=IF(C269="","",C269/C150)', computed_snapshot=2.6997287877411336),
    OutputSpec(name="c1_h2o_formed_total", desc='C1', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=274, excel_formula='=2.25', computed_snapshot=2.25),
    OutputSpec(name="c2_h2o_formed_total", desc='C2', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=275, excel_formula='=1.8', computed_snapshot=1.8),
    OutputSpec(name="c2_unsat_h2o_formed_total", desc='C2=', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=276, excel_formula='=1.28', computed_snapshot=1.28),
    OutputSpec(name="c3_h2o_formed_total", desc='C3', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=277, excel_formula='=1.63', computed_snapshot=1.63),
    OutputSpec(name="c3_unsat_h2o_formed_total", desc='C3=', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=278, excel_formula='=1.28', computed_snapshot=1.28),
    OutputSpec(name="i_c4_h2o_formed_total", desc='i-C4', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=279, excel_formula='=1.55', computed_snapshot=1.55),
    OutputSpec(name="n_c4_h2o_formed_total", desc='n-C4', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=280, excel_formula='=1.55', computed_snapshot=1.55),
    OutputSpec(name="c4_h2o_formed_total", desc='C4=', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=281, excel_formula='=1.28', computed_snapshot=1.28),
    OutputSpec(name="c5_h2o_formed_total", desc='C5', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=282, excel_formula='=1.5', computed_snapshot=1.5),
    OutputSpec(name="c6_h2o_formed_total", desc='C6+', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=283, excel_formula='=1.46', computed_snapshot=1.46),
    OutputSpec(name="n2_h2o_formed_total", desc='N2', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=284, excel_formula='=0', computed_snapshot=0),
    OutputSpec(name="h2_h2o_formed_total", desc='H2', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=285, excel_formula='=8.94', computed_snapshot=8.94),
    OutputSpec(name="v_02_argon_h2o_formed_total", desc='02/Argon', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=286, excel_formula='=0', computed_snapshot=0),
    OutputSpec(name="co_h2o_formed_total", desc='CO', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=287, excel_formula='=0', computed_snapshot=0),
    OutputSpec(name="co2_h2o_formed_total", desc='CO2', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=288, excel_formula='=0', computed_snapshot=0),
    OutputSpec(name="h2s_h2o_formed_total", desc='H2S', uom='kg of H2O/kg', section='H2O Formed ( kg of H2O / kg )', row=289, excel_formula='=0.53', computed_snapshot=0.53),
    OutputSpec(name="c1_h2o_formed_total_h2o_total_kg", desc='C1', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=293, excel_formula='=IF(C134="","",C134*C274)', computed_snapshot=12.082568108720675),
    OutputSpec(name="c2_h2o_formed_total_h2o_total_kg", desc='C2', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=294, excel_formula='=IF(C135="","",C135*C275)', computed_snapshot=4.7631580887082725),
    OutputSpec(name="c2_unsat_h2o_formed_total_2", desc='C2=', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=295, excel_formula='=IF(C136="","",C136*C276)', computed_snapshot=0),
    OutputSpec(name="c3_h2o_formed_total_h2o_total_kg", desc='C3', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=296, excel_formula='=IF(C137="","",C137*C277)', computed_snapshot=4.2727955525766586),
    OutputSpec(name="c3_unsat_h2o_formed_total_2", desc='C3=', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=297, excel_formula='=IF(C138="","",C138*C278)', computed_snapshot=0),
    OutputSpec(name="i_c4_h2o_formed_total_h2o_total_kg", desc='i-C4', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=298, excel_formula='=IF(C139="","",C139*C279)', computed_snapshot=2.197480007328854),
    OutputSpec(name="n_c4_h2o_formed_total_h2o_total_kg", desc='n-C4', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=299, excel_formula='=IF(C140="","",C140*C280)', computed_snapshot=2.0513583797007273),
    OutputSpec(name="c4_h2o_formed_total_h2o_total_kg", desc='C4=', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=300, excel_formula='=IF(C141="","",C141*C281)', computed_snapshot=0),
    OutputSpec(name="c5_h2o_formed_total_h2o_total_kg", desc='C5', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=301, excel_formula='=IF(C142="","",C142*C282)', computed_snapshot=0.5314940823259088),
    OutputSpec(name="c6_h2o_formed_total_h2o_total_kg", desc='C6+', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=302, excel_formula='=IF(C143="","",C143*C283)', computed_snapshot=0),
    OutputSpec(name="n2_h2o_formed_total_h2o_total_kg", desc='N2', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=303, excel_formula='=IF(C144="","",C144*C284)', computed_snapshot=0),
    OutputSpec(name="h2_h2o_formed_total_h2o_total_kg", desc='H2', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=304, excel_formula='=IF(C145="","",C145*C285)', computed_snapshot=8.373254355051477),
    OutputSpec(name="v_02_argon_h2o_formed_total_h2o_total_kg", desc='02/Argon', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=305, excel_formula='=IF(C146="","",C146*C286)', computed_snapshot=0),
    OutputSpec(name="co_h2o_formed_total_h2o_total_kg", desc='CO', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=306, excel_formula='=IF(C147="","",C147*C287)', computed_snapshot=0),
    OutputSpec(name="co2_h2o_formed_total_h2o_total_kg", desc='CO2', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=307, excel_formula='=IF(C148="","",C148*C288)', computed_snapshot=0),
    OutputSpec(name="h2s_h2o_formed_total_h2o_total_kg", desc='H2S', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=308, excel_formula='=IF(C149="","",C149*C289)', computed_snapshot=1.054467343157145e-05),
    OutputSpec(name="total_h2o_formed_total", desc='Total', uom='kg of H2O', section='( 3 X 10 ) - H2O Formed ( kg )', row=309, excel_formula='=IF(C293="","",SUM(C293:C308))', computed_snapshot=34.272119119086),
    OutputSpec(name="total_per_kg_of_fuel_h2o_formed_total", desc='Total per kg of Fuel', uom='kg of H2O/kg Fuel', section='( 3 X 10 ) - H2O Formed ( kg )', row=310, excel_formula='=IF(C309="","",C309/C150)', computed_snapshot=2.32809364392026),
    OutputSpec(name="c1_n2_formed_total", desc='C1', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=314, excel_formula='=13.25', computed_snapshot=13.25),
    OutputSpec(name="c2_n2_formed_total", desc='C2', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=315, excel_formula='=12.37', computed_snapshot=12.37),
    OutputSpec(name="c2_unsat_n2_formed_total", desc='C2=', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=316, excel_formula='=11.36', computed_snapshot=11.36),
    OutputSpec(name="c3_n2_formed_total", desc='C3', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=317, excel_formula='=12.05', computed_snapshot=12.05),
    OutputSpec(name="c3_unsat_n2_formed_total", desc='C3=', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=318, excel_formula='=11.36', computed_snapshot=11.36),
    OutputSpec(name="i_c4_n2_formed_total", desc='i-C4', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=319, excel_formula='=11.88', computed_snapshot=11.88),
    OutputSpec(name="n_c4_n2_formed_total", desc='n-C4', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=320, excel_formula='=11.88', computed_snapshot=11.88),
    OutputSpec(name="c4_n2_formed_total", desc='C4=', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=321, excel_formula='=11.36', computed_snapshot=11.36),
    OutputSpec(name="c5_n2_formed_total", desc='C5', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=322, excel_formula='=11.78', computed_snapshot=11.78),
    OutputSpec(name="c6_n2_formed_total", desc='C6+', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=323, excel_formula='=11.71', computed_snapshot=11.71),
    OutputSpec(name="n2_n2_formed_total", desc='N2', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=324, excel_formula='=1', computed_snapshot=1),
    OutputSpec(name="h2_n2_formed_total", desc='H2', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=325, excel_formula='=26.36', computed_snapshot=26.36),
    OutputSpec(name="v_02_argon_n2_formed_total", desc='02/Argon', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=326, excel_formula='=-3.32', computed_snapshot=-3.32),
    OutputSpec(name="co_n2_formed_total", desc='CO', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=327, excel_formula='=1.9', computed_snapshot=1.9),
    OutputSpec(name="co2_n2_formed_total", desc='CO2', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=328, excel_formula='=0', computed_snapshot=0),
    OutputSpec(name="h2s_n2_formed_total", desc='H2S', uom='kg of N2/kg', section='N2 Formed ( kg of N2 / kg )', row=329, excel_formula='=4.68', computed_snapshot=4.68),
    OutputSpec(name="c1_n2_formed_total_n2_total_kg", desc='C1', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=333, excel_formula='=IF(C134="","",C134*C314)', computed_snapshot=71.15290108468842),
    OutputSpec(name="c2_n2_formed_total_n2_total_kg", desc='C2', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=334, excel_formula='=IF(C135="","",C135*C315)', computed_snapshot=32.733480865178514),
    OutputSpec(name="c2_unsat_n2_formed_total_2", desc='C2=', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=335, excel_formula='=IF(C136="","",C136*C316)', computed_snapshot=0),
    OutputSpec(name="c3_n2_formed_total_n2_total_kg", desc='C3', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=336, excel_formula='=IF(C137="","",C137*C317)', computed_snapshot=31.587230925490026),
    OutputSpec(name="c3_unsat_n2_formed_total_2", desc='C3=', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=337, excel_formula='=IF(C138="","",C138*C318)', computed_snapshot=0),
    OutputSpec(name="i_c4_n2_formed_total_n2_total_kg", desc='i-C4', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=338, excel_formula='=IF(C139="","",C139*C319)', computed_snapshot=16.84262095939793),
    OutputSpec(name="n_c4_n2_formed_total_n2_total_kg", desc='n-C4', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=339, excel_formula='=IF(C140="","",C140*C320)', computed_snapshot=15.722669387641705),
    OutputSpec(name="c4_n2_formed_total_n2_total_kg", desc='C4=', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=340, excel_formula='=IF(C141="","",C141*C321)', computed_snapshot=0),
    OutputSpec(name="c5_n2_formed_total_n2_total_kg", desc='C5', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=341, excel_formula='=IF(C142="","",C142*C322)', computed_snapshot=4.17400019319947),
    OutputSpec(name="c6_n2_formed_total_n2_total_kg", desc='C6+', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=342, excel_formula='=IF(C143="","",C143*C323)', computed_snapshot=0),
    OutputSpec(name="n2_n2_formed_total_n2_total_kg", desc='N2', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=343, excel_formula='=IF(C144="","",C144*C324)', computed_snapshot=0),
    OutputSpec(name="h2_n2_formed_total_n2_total_kg", desc='H2', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=344, excel_formula='=IF(C145="","",C145*C325)', computed_snapshot=24.68892447417863),
    OutputSpec(name="v_02_argon_n2_formed_total_n2_total_kg", desc='02/Argon', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=345, excel_formula='=IF(C146="","",C146*C326)', computed_snapshot=0),
    OutputSpec(name="co_n2_formed_total_n2_total_kg", desc='CO', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=346, excel_formula='=IF(C147="","",C147*C327)', computed_snapshot=0),
    OutputSpec(name="co2_n2_formed_total_n2_total_kg", desc='CO2', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=347, excel_formula='=IF(C148="","",C148*C328)', computed_snapshot=0),
    OutputSpec(name="h2s_n2_formed_total_n2_total_kg", desc='H2S', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=348, excel_formula='=IF(C149="","",C149*C329)', computed_snapshot=9.311145596180073e-05),
    OutputSpec(name="total_n2_formed_total", desc='Total', uom='kg of N2', section='( 3 X 12 ) - N2 Formed ( kg )', row=349, excel_formula='=IF(C333="","",SUM(C333:C348))', computed_snapshot=196.90192100123065),
    OutputSpec(name="total_per_kg_of_fuel_n2_formed_total", desc='Total per kg of Fuel', uom='kg of N2/kg Fuel', section='( 3 X 12 ) - N2 Formed ( kg )', row=350, excel_formula='=IF(C349="","",C349/C150)', computed_snapshot=13.375481952715607),
    OutputSpec(name='moisture_in_air', desc='Moisture in Air', uom='kg of Moisture/ kg of Air', section='Correction for RH', row=353, excel_formula='=IF(C43="","",C43*C88*18.015/(1013.25*100*28.85))', computed_snapshot=0.004880080654747985),
    OutputSpec(name='wet_air_required', desc='Wet Air Required', uom='kg of Wet Air / kg of Fuel', section='Wet Air Required', row=356, excel_formula='=IF(C230="","",C230/(1-C353))', computed_snapshot=17.487994077498517),
    OutputSpec(name='moisture', desc='Moisture', uom='kg of Moisture / kg of Fuel', section='Moisture', row=359, excel_formula='=IF(C356="","",(C356-C230))', computed_snapshot=0.08534282158794682),
    OutputSpec(name='total_h2o_formed', desc='Total H2O Formed', uom='kg of H2O / kg of Fuel', section='Total H2O Formed', row=362, excel_formula='=IF(C310="","",(C310+C359))', computed_snapshot=2.413436465508207),
    OutputSpec(name='excess_air_wet_ea_wet', desc='Excess Air (Wet) Ea (wet)', uom='%', section='Correction for Excess Air', row=365, excel_formula='=IF(C6="","",(28.85*C6)*(C350/28.013+C270/44.01+C362/18.015)/(20.95-C6*((1.6028*C359/C230)+1)))', computed_snapshot=25.5864389),
    OutputSpec(name='excess_air_wet_m_ea_wet', desc='Excess Air (Wet) m ea (wet)', uom='kg of Excess Air / kg of Fuel', section='Correction for Excess Air', row=366, excel_formula='=IF(C365="","",C365*100/C230)', computed_snapshot=4.45176635),
    OutputSpec(name='excess_air_dry_ea_dry', desc='Excess Air (Dry) Ea (dry)', uom='%', section='Correction for Excess Air', row=369, excel_formula='=IF(C37="","",(28.85*C37)*(C350/28.013+C270/44.01)/(20.95-C37))', computed_snapshot=31.11948499),
    OutputSpec(name='excess_air_dry_m_ea_dry', desc='Excess Air (Dry) m ea (dry)', uom='kg of Excess Air / kg of Fuel', section='Correction for Excess Air', row=370, excel_formula='=IF(C369="","",C369*100/C230)', computed_snapshot=5.414187255),
    OutputSpec(name='total_h2o_formed_wet_m_h2o', desc='Total H2O Formed ( Wet ) m H2O', uom='kg of H2O / kg of Fuel', section='Correction for Excess Air', row=373, excel_formula='=IF(C366="","",(C366*C359/100)+C362)', computed_snapshot=2.4352726544101335),
    OutputSpec(name='total_h2o_formed_dry_m_h2o', desc='Total H2O Formed ( Dry ) m H2O', uom='kg of H2O / kg of Fuel', section='Correction for Excess Air', row=374, excel_formula='=IF(C370="","",(C370*C359/100)+C362)', computed_snapshot=2.439994712062943),
    OutputSpec(name='h2o_enthalpy_stack_temp', desc='H2O enthalpy @ stack Temp.', uom='kcal / kg H2O', section='Stack Loss', row=377, excel_formula='=IF(C89="","",((-1.93001+0.447642*C89-0.021898/1000*C89^2+0.030496/1000000*C89^3-0.056618/10000000000*C89^4+0.027722/100000000000000*C89^5)-(-1.93001+0.447642*519.67-0.021898/1000*519.67^2+0.030496/1000000*519.67^3-0.056618/10000000000*519.67^4+0.027722/100000000000000*519.67^5))*5/9)', computed_snapshot=102.88896865271408),
    OutputSpec(name='co2_enthalpy_stack_temp', desc='CO2 enthalpy @ stack Temp.', uom='kcal / kg CO2', section='Stack Loss', row=378, excel_formula='=IF(C89="","",((0.09688+0.158843*C89-0.033712/1000*C89^2+0.148105/1000000*C89^3-0.966203/10000000000*C89^4+2.073832/100000000000000*C89^5)-(0.09688+0.158843*519.67-0.033712/1000*519.67^2+0.148105/1000000*519.67^3-0.966203/10000000000*519.67^4+2.073832/100000000000000*519.67^5))*5/9)', computed_snapshot=50.44006371857576),
    OutputSpec(name='n2_enthalpy_stack_temp', desc='N2 enthalpy @ stack Temp.', uom='kcal / kg N2', section='Stack Loss', row=379, excel_formula='=IF(C89="","",((-0.65665+0.254098*C89-0.016624/1000*C89^2+0.015302/1000000*C89^3-0.030995/10000000000*C89^4+0.015167/100000000000000*C89^5)-(-0.65665+0.254098*519.67-0.016624/1000*519.67^2+0.015302/1000000*519.67^3-0.030995/10000000000*519.67^4+0.015167/100000000000000*519.67^5))*5/9)', computed_snapshot=56.34831890435834),
    OutputSpec(name='o2_enthalpy_stack_temp', desc='O2 enthalpy @ stack Temp.', uom='kcal / kg O2', section='Stack Loss', row=380, excel_formula='=IF(C89="","",((-0.34466+0.221724*C89-0.020517/1000*C89^2+0.030639/1000000*C89^3-0.108606/10000000000*C89^4+0.130606/100000000000000*C89^5)-(-0.34466+0.221724*519.67-0.020517/1000*519.67^2+0.030639/1000000*519.67^3-0.108606/10000000000*519.67^4+0.130606/100000000000000*519.67^5))*5/9)', computed_snapshot=50.90069471817905),
    OutputSpec(name='excess_air_enthalpy_stack_temp', desc='Excess air enthalpy @ stack Temp.', uom='kcal / kg Excess Air', section='Stack Loss', row=381, excel_formula='=IF(C89="","",0.21*C380+0.79*C379)', computed_snapshot=55.20431782526069),
    OutputSpec(name='stack_massic_heat_loss_wet_hs', desc='Stack Massic Heat Loss (Wet) hs', uom='kcal / kg of fuel', section='Stack Loss', row=382, excel_formula='=IF(C89="","",(C377*C373)+(C378*C270)+(C379*C350)+(C381*C365))', computed_snapshot=1386.232406446038),
    OutputSpec(name='stack_massic_heat_loss_dry_hs', desc='Stack Massic Heat Loss (Dry) hs', uom='kcal / kg of fuel', section='Stack Loss', row=383, excel_formula='=IF(C89="","",(C377*C374)+(C378*C270)+(C379*C350)+(C381*C369))', computed_snapshot=1439.874310366739),
    OutputSpec(name="h2o_enthalpy_stack_temp_bwt", desc='H2O enthalpy @ stack Temp.', uom='kcal / kg H2O', section='BWT Loss', row=386, excel_formula='=IF(C90="","",((-1.93001+0.447642*C90-0.021898/1000*C90^2+0.030496/1000000*C90^3-0.056618/10000000000*C90^4+0.027722/100000000000000*C90^5)-(-1.93001+0.447642*519.67-0.021898/1000*519.67^2+0.030496/1000000*519.67^3-0.056618/10000000000*519.67^4+0.027722/100000000000000*519.67^5))*5/9)', computed_snapshot=319.4528036331904),
    OutputSpec(name="co2_enthalpy_stack_temp_bwt", desc='CO2 enthalpy @ stack Temp.', uom='kcal / kg CO2', section='BWT Loss', row=387, excel_formula='=IF(C90="","",((0.09688+0.158843*C90-0.033712/1000*C90^2+0.148105/1000000*C90^3-0.966203/10000000000*C90^4+2.073832/100000000000000*C90^5)-(0.09688+0.158843*519.67-0.033712/1000*519.67^2+0.148105/1000000*519.67^3-0.966203/10000000000*519.67^4+2.073832/100000000000000*519.67^5))*5/9)', computed_snapshot=166.96308834561552),
    OutputSpec(name="n2_enthalpy_stack_temp_bwt", desc='N2 enthalpy @ stack Temp.', uom='kcal / kg N2', section='BWT Loss', row=388, excel_formula='=IF(C90="","",((-0.65665+0.254098*C90-0.016624/1000*C90^2+0.015302/1000000*C90^3-0.030995/10000000000*C90^4+0.015167/100000000000000*C90^5)-(-0.65665+0.254098*519.67-0.016624/1000*519.67^2+0.015302/1000000*519.67^3-0.030995/10000000000*519.67^4+0.015167/100000000000000*519.67^5))*5/9)', computed_snapshot=170.34043453364504),
    OutputSpec(name="o2_enthalpy_stack_temp_bwt", desc='O2 enthalpy @ stack Temp.', uom='kcal / kg O2', section='BWT Loss', row=389, excel_formula='=IF(C90="","",((-0.34466+0.221724*C90-0.020517/1000*C90^2+0.030639/1000000*C90^3-0.108606/10000000000*C90^4+0.130606/100000000000000*C90^5)-(-0.34466+0.221724*519.67-0.020517/1000*519.67^2+0.030639/1000000*519.67^3-0.108606/10000000000*519.67^4+0.130606/100000000000000*519.67^5))*5/9)', computed_snapshot=157.4701198512647),
    OutputSpec(name="excess_air_enthalpy_stack_temp_bwt", desc='Excess air enthalpy @ stack Temp.', uom='kcal / kg Excess Air', section='BWT Loss', row=390, excel_formula='=IF(C90="","",0.21*C389+0.79*C388)', computed_snapshot=167.63766845034516),
    OutputSpec(name='bw_massic_heat_loss_wet_hbw', desc='BW Massic Heat Loss (Wet) hbw', uom='kcal / kg of fuel', section='BWT Loss', row=391, excel_formula='=IF(C90="","",(C386*C373)+(C387*C270)+(C388*C350)+(C390*C365))', computed_snapshot=4253.538527367456),
    OutputSpec(name='bw_massic_heat_loss_dry_hbw', desc='BW Massic Heat Loss (Dry) hbw', uom='kcal / kg of fuel', section='BWT Loss', row=392, excel_formula='=IF(C90="","",(C386*C374)+(C387*C270)+(C388*C350)+(C390*C369))', computed_snapshot=4416.46476215771),
    OutputSpec(name='specific_heat_capacity_of_oxygen_cp_oxygen', desc='Specific Heat Capacity of Oxygen Cp oxygen', uom='kcal / kg.K', section='Air Sensible massic heat correction', row=395, excel_formula='=IF(C92="","",0.0286895*(C92/100)-0.00121326*(C92/100)^2+0.0000186119*(C92/100)^3+0.518105*(100/C92))', computed_snapshot=0.2184417940713817),
    OutputSpec(name='specific_heat_capacity_of_nitrogen_cp_nitrogen', desc='Specific Heat Capacity of Nitrogen Cp nitrogen', uom='kcal / kg.K', section='Air Sensible massic heat correction', row=396, excel_formula='=IF(C92="","",0.0288541*(C92/100)-0.00118902*(C92/100)^2+0.0000185046*(C92/100)^3+0.663371*(100/C92))', computed_snapshot=0.2470747458937616),
    OutputSpec(name='specific_heat_capacity_of_the_air_cp_air', desc='Specific Heat Capacity of the Air Cp air', uom='kcal / kg.K', section='Air Sensible massic heat correction', row=397, excel_formula='=IF(C92="","",C395*0.21+C396*0.79)', computed_snapshot=0.24106182601106182),
    OutputSpec(name='air_sensible_massic_heat_correction_wet_ha_wet', desc='Air Sensible Massic Heat Correction (Wet) Δha (wet)', uom='kcal / kg fuel', section='Air Sensible massic heat correction', row=398, excel_formula='=IF(C91="","",C397*(C5-15.6)*(C356+C365))', computed_snapshot=49.717241959248035),
    OutputSpec(name='air_sensible_massic_heat_correction_dry_ha_dry', desc='Air Sensible Massic Heat Correction (Dry) Δha (dry)', uom='kcal / kg of fuel', section='Air Sensible massic heat correction', row=399, excel_formula='=IF(C91="","",C397*(C5-15.6)*(C356+C369))', computed_snapshot=51.89914777843651),
    OutputSpec(name='specific_heat_capacity_of_the_fuel_cpf', desc='Specific Heat Capacity of the Fuel Cpf', uom='kcal / kg.K', section='Air Sensible massic heat correction', row=401, excel_formula='=IF(C499="","",C499)', computed_snapshot=1.8373577004818964),
    OutputSpec(name='fuel_sensible_massic_heat_correction_hf', desc='Fuel Sensible Massic Heat Correction Δhf', uom='kcal / kg of fuel', section='Air Sensible massic heat correction', row=402, excel_formula='=IF(C401="","",C401*(C4-15.6))', computed_snapshot=26.28179955720196),
    OutputSpec(name='assumed_radiation_massic_heat_loss_hr', desc='Assumed Radiation Massic Heat Loss hr', uom='kcal / kg of fuel', section='Air Sensible massic heat correction', row=404, excel_formula='=IF(C45="","",C45*C190/100)', computed_snapshot=249.62113092482323),
    OutputSpec(name='higher_massic_heat_value_wet_hh', desc='Higher Massic Heat Value (Wet) hH', uom='kcal / kg of fuel', section='Air Sensible massic heat correction', row=406, excel_formula='=IF(C190="","",C190+(C373*588.73125))', computed_snapshot=13914.777660162858),
    OutputSpec(name='higher_massic_heat_value_dry_hh', desc='Higher Massic Heat Value (Dry) hH', uom='kcal / kg of fuel', section='Air Sensible massic heat correction', row=407, excel_formula='=IF(C190="","",C190+(C374*588.73125))', computed_snapshot=13917.557683067367),
    OutputSpec(name='net_thermal_efficiency_wet_e', desc='Net Thermal Efficiency Wet E', uom='%', section='Air Sensible massic heat correction', row=409, excel_formula='=IF(C190="","",((C190+C398+C402)-(C404+C382))/(C190+C398+C402)*100)', computed_snapshot=86.97263442103639),
    OutputSpec(name='gross_thermal_efficiency_eg', desc='Gross Thermal Efficiency Eg', uom='%', section='Air Sensible massic heat correction', row=410, excel_formula='=IF(C190="","",((C190+C398+C402)-(C404+C382))/(C406+C398+C402)*100)', computed_snapshot=78.0600125586729),
    OutputSpec(name='fuel_thermal_efficiency_ef', desc='Fuel Thermal Efficiency Ef', uom='%', section='Air Sensible massic heat correction', row=411, excel_formula='=IF(C190="","",((C190+C398+C402)-(C404+C382))/C190*100)', computed_snapshot=87.50222394974901),
    OutputSpec(name='net_thermal_efficiency_dry_e', desc='Net Thermal Efficiency Dry E', uom='%', section='Air Sensible massic heat correction', row=413, excel_formula='=IF(C194="","",((C190+C399+C402)-(C404+C382))/(C190+C399+C402)*100)', computed_snapshot=86.97489765435608),
    OutputSpec(name="gross_thermal_efficiency_eg_row_414", desc='Gross Thermal Efficiency Eg', uom='%', section='Air Sensible massic heat correction', row=414, excel_formula='=IF(C194="","",((C190+C399+C402)-(C404+C382))/(C407+C399+C402)*100)', computed_snapshot=78.04792762046172),
    OutputSpec(name="fuel_thermal_efficiency_ef_row_415", desc='Fuel Thermal Efficiency Ef', uom='%', section='Air Sensible massic heat correction', row=415, excel_formula='=IF(C194="","",((C190+C399+C402)-(C404+C382))/C190*100)', computed_snapshot=87.51970568946476),
    OutputSpec(name='gap_between_dry_wet', desc='Gap between ( Dry - Wet )', uom='%', section='Air Sensible massic heat correction', row=417, excel_formula='=C413-C409', computed_snapshot=0.002263233319695246),
    OutputSpec(name='fuel_gas_flow', desc='Fuel Gas Flow', uom='kg/hr', section='Air Sensible massic heat correction', row=419, excel_formula="=C3*C464/22.414", computed_snapshot=580.1537858544909),
    OutputSpec(name='heater_librated_heat_wet', desc='Heater Librated Heat wet', uom='Gcal/hr', section='Air Sensible massic heat correction', row=420, excel_formula='=C419*C190/1000000', computed_snapshot=7.240932206765787),
    OutputSpec(name='absorbed_duty_wet', desc='Absorbed Duty Wet', uom='Gcal/hr', section='Air Sensible massic heat correction', row=421, excel_formula='=C420*C409/100', computed_snapshot=6.297629496865491),
    OutputSpec(name="absorbed_duty_dry_row_422", desc='Absorbed Duty Dry', uom='Gcal/hr', section='Air Sensible massic heat correction', row=422, excel_formula='=C420*C413/100', computed_snapshot=6.297793376055851),
    OutputSpec(name='radiant_duty_wet', desc='Radiant Duty wet', uom='Gcal/hr', section='Air Sensible massic heat correction', row=423, excel_formula='=C421-C425', computed_snapshot=4.6341509956091755),
    OutputSpec(name="radiant_duty_dry_row_424", desc='Radiant Duty Dry', uom='Gcal/hr', section='Air Sensible massic heat correction', row=424, excel_formula='=C422-C426', computed_snapshot=4.57091315651099),
    OutputSpec(name='convection_duty_wet', desc='Convection Duty wet', uom='Gcal/hr', section='Air Sensible massic heat correction', row=425, excel_formula='=C419*(C391-C382)/1000000', computed_snapshot=1.6634785012563151),
    OutputSpec(name="convection_duty_dry_row_426", desc='Convection Duty Dry', uom='Gcal/hr', section='Air Sensible massic heat correction', row=426, excel_formula='=C419*(C392-C383)/1000000', computed_snapshot=1.726880219544861),
    OutputSpec(name='fuel_gas_temp', desc='Fuel Gas Temp.', uom='°C', section='Air Sensible massic heat correction', row=428, excel_formula="=C4", computed_snapshot=132.84264437357584),
    OutputSpec(name='temperature_in_rankine', desc='Temperature', uom='°R', section='Air Sensible massic heat correction', row=429, excel_formula='=IF(C4="","",C4*9/5+491.67)', computed_snapshot=730.49336),
    OutputSpec(name='c1_mole_fraction', desc='C1 Mole Fraction', uom=None, section='Fuel Gas', row=431, excel_formula='=C95/$C$111', computed_snapshot=0.33472731225721636),
    OutputSpec(name='c2_mole_fraction', desc='C2 Mole Fraction', uom=None, section='Fuel Gas', row=432, excel_formula='=C96/$C$111', computed_snapshot=0.08800129491756775),
    OutputSpec(name="c2_mole_fraction_composition", desc='C2= Mole Fraction', uom=None, section='Fuel Gas', row=433, excel_formula='=C97/$C$111', computed_snapshot=0),
    OutputSpec(name='c3_mole_fraction', desc='C3 Mole Fraction', uom=None, section='Fuel Gas', row=434, excel_formula='=C98/$C$111', computed_snapshot=0.05944501813662962),
    OutputSpec(name="c3_mole_fraction_composition", desc='C3= Mole Fraction', uom=None, section='Fuel Gas', row=435, excel_formula='=C99/$C$111', computed_snapshot=0),
    OutputSpec(name='i_c4_mole_fraction', desc='i-C4 Mole Fraction', uom=None, section='Fuel Gas', row=436, excel_formula='=C100/$C$111', computed_snapshot=0.02439145683343124),
    OutputSpec(name='n_c4_mole_fraction', desc='n-C4 Mole Fraction', uom=None, section='Fuel Gas', row=437, excel_formula='=C101/$C$111', computed_snapshot=0.022769544751939978),
    OutputSpec(name='c4_mole_fraction', desc='C4= Mole Fraction', uom=None, section='Fuel Gas', row=438, excel_formula='=C102/$C$111', computed_snapshot=0),
    OutputSpec(name='c5_mole_fraction', desc='C5 Mole Fraction', uom=None, section='Fuel Gas', row=439, excel_formula='=C103/$C$111', computed_snapshot=0.004910942165975141),
    OutputSpec(name='c6_mole_fraction', desc='C6+ Mole Fraction', uom=None, section='Fuel Gas', row=440, excel_formula='=C104/$C$111', computed_snapshot=0),
    OutputSpec(name='n2_mole_fraction', desc='N2 Mole Fraction', uom=None, section='Fuel Gas', row=441, excel_formula='=C105/$C$111', computed_snapshot=0),
    OutputSpec(name='h2_mole_fraction', desc='H2 Mole Fraction', uom=None, section='Fuel Gas', row=442, excel_formula='=C106/$C$111', computed_snapshot=0.46458612725996706),
    OutputSpec(name='v_02_argon_mole_fraction', desc='02/Argon Mole Fraction', uom=None, section='Fuel Gas', row=443, excel_formula='=C107/$C$111', computed_snapshot=0),
    OutputSpec(name='co_mole_fraction', desc='CO Mole Fraction', uom=None, section='Fuel Gas', row=444, excel_formula='=C108/$C$111', computed_snapshot=0),
    OutputSpec(name='co2_mole_fraction', desc='CO2 Mole Fraction', uom=None, section='Fuel Gas', row=445, excel_formula='=C109/$C$111', computed_snapshot=0.0011677198173640107),
    OutputSpec(name='h2s_mole_fraction', desc='H2S Mole Fraction', uom=None, section='Fuel Gas', row=446, excel_formula='=C110/$C$111', computed_snapshot=5.838599086820054e-07),
    OutputSpec(name='c1_kg_kg_mole', desc='C1 kg / kg mole', uom='kg / kg mole', section='Mw', row=448, excel_formula='=IF(C431="","",C431*16.043)', computed_snapshot=5.370030270542522),
    OutputSpec(name='c2_kg_kg_mole', desc='C2 kg / kg mole', uom='kg / kg mole', section='Mw', row=449, excel_formula='=IF(C432="","",C432*30.07)', computed_snapshot=2.6461989381712625),
    OutputSpec(name="c2_kg_kg_mole_composition", desc='C2= kg / kg mole', uom='kg / kg mole', section='Mw', row=450, excel_formula='=IF(C433="","",C433*28.054)', computed_snapshot=0),
    OutputSpec(name='c3_kg_kg_mole', desc='C3 kg / kg mole', uom='kg / kg mole', section='Mw', row=451, excel_formula='=IF(C434="","",C434*44.097)', computed_snapshot=2.6213469647709564),
    OutputSpec(name="c3_kg_kg_mole_composition", desc='C3= kg / kg mole', uom='kg / kg mole', section='Mw', row=452, excel_formula='=IF(C435="","",C435*42.081)', computed_snapshot=0),
    OutputSpec(name='i_c4_kg_kg_mole', desc='i-C4 kg / kg mole', uom='kg / kg mole', section='Mw', row=453, excel_formula='=IF(C436="","",C436*58.124)', computed_snapshot=1.4177290369863573),
    OutputSpec(name='n_c4_kg_kg_mole', desc='n-C4 kg / kg mole', uom='kg / kg mole', section='Mw', row=454, excel_formula='=IF(C437="","",C437*58.124)', computed_snapshot=1.3234570191617594),
    OutputSpec(name='c4_kg_kg_mole', desc='C4= kg / kg mole', uom='kg / kg mole', section='Mw', row=455, excel_formula='=IF(C438="","",C438*56.108)', computed_snapshot=0),
    OutputSpec(name='c5_kg_kg_mole', desc='C5 kg / kg mole', uom='kg / kg mole', section='Mw', row=456, excel_formula='=IF(C439="","",C439*72.151)', computed_snapshot=0.3543293882172724),
    OutputSpec(name='c6_kg_kg_mole', desc='C6+ kg / kg mole', uom='kg / kg mole', section='Mw', row=457, excel_formula='=IF(C440="","",C440*86.178)', computed_snapshot=0),
    OutputSpec(name='n2_kg_kg_mole', desc='N2 kg / kg mole', uom='kg / kg mole', section='Mw', row=458, excel_formula='=IF(C441="","",C441*28.013)', computed_snapshot=0),
    OutputSpec(name='h2_kg_kg_mole', desc='H2 kg / kg mole', uom='kg / kg mole', section='Mw', row=459, excel_formula='=IF(C442="","",C442*2.016)', computed_snapshot=0.9366056325560936),
    OutputSpec(name='v_02_argon_kg_kg_mole', desc='02/Argon kg / kg mole', uom='kg / kg mole', section='Mw', row=460, excel_formula='=IF(C443="","",C443*31.999)', computed_snapshot=0),
    OutputSpec(name='co_kg_kg_mole', desc='CO kg / kg mole', uom='kg / kg mole', section='Mw', row=461, excel_formula='=IF(C444="","",C444*28.01)', computed_snapshot=0),
    OutputSpec(name='co2_kg_kg_mole', desc='CO2 kg / kg mole', uom='kg / kg mole', section='Mw', row=462, excel_formula='=IF(C445="","",C445*44.01)', computed_snapshot=0.051391349162190104),
    OutputSpec(name='h2s_kg_kg_mole', desc='H2S kg / kg mole', uom='kg / kg mole', section='Mw', row=463, excel_formula='=IF(C446="","",C446*34.076)', computed_snapshot=1.9895610248248017e-05),
    OutputSpec(name='avg_mw_kg_kg_mole', desc='AVG. MW kg / kg mole', uom='kg / kg mole', section='Mw', row=464, excel_formula='=IF(C448="","",SUM(C448:C463))', computed_snapshot=14.721108495178662),
    OutputSpec(name="c1_cp_total", desc='C1', uom='kcal / kg.K', section='CP', row=466, excel_formula='=IF(C429="","",0.0776543*(C429/100)-0.00112162*(C429/100)^2-0.0000012072*(C429/100)^3+0.798622*(100/C429))', computed_snapshot=0.5364330184499105),
    OutputSpec(name="c2_cp_total", desc='C2', uom='kcal / kg.K', section='CP', row=467, excel_formula='=IF(C429="","",0.0830087*(C429/100)-0.00189188*(C429/100)^2+0.0000147441*(C429/100)^3+0.143728*(100/C429))', computed_snapshot=0.42525549300367865),
    OutputSpec(name="c2_unsat_cp_total", desc='C2=', uom='kcal / kg.K', section='CP', row=468, excel_formula='=IF(C429="","",0.0773807*(C429/100)-0.00233748*(C429/100)^2+0.0000280498*(C429/100)^3+0.101394*(100/C429))', computed_snapshot=0.3756944805676734),
    OutputSpec(name="c3_cp_total", desc='C3', uom='kcal / kg.K', section='CP', row=469, excel_formula='=IF(C429="","",0.088012*(C429/100)-0.00241553*(C429/100)^2+0.0000255127*(C429/100)^3-0.033623*(100/C429))', computed_snapshot=0.4062024364210942),
    OutputSpec(name="c3_unsat_cp_total", desc='C3=', uom='kcal / kg.K', section='CP', row=470, excel_formula='=IF(C429="","",0.0761423*(C429/100)-0.00212824*(C429/100)^2+0.0000230049*(C429/100)^3+0.066058*(100/C429))', computed_snapshot=0.36786868461121097),
    OutputSpec(name="i_c4_cp_total", desc='i-C4', uom='kcal / kg.K', section='CP', row=471, excel_formula='=IF(C429="","",0.0904328*(C429/100)-0.00268123*(C429/100)^2+0.0000310858*(C429/100)^3-0.072466*(100/C429))', computed_snapshot=0.4052854526196019),
    OutputSpec(name="n_c4_cp_total", desc='n-C4', uom='kcal / kg.K', section='CP', row=472, excel_formula='=IF(C429="","",0.0873284*(C429/100)-0.00244614*(C429/100)^2+0.0000263297*(C429/100)^3-0.000166*(100/C429))', computed_snapshot=0.4078284804555893),
    OutputSpec(name="c4_cp_total", desc='C4=', uom='kcal / kg.K', section='CP', row=473, excel_formula='=IF(C429="","",0.0810215*(C429/100)-0.00244194*(C429/100)^2+0.0000289049*(C429/100)^3-0.021342*(100/C429))', computed_snapshot=0.370085532225647),
    OutputSpec(name="c5_cp_total", desc='C5', uom='kcal / kg.K', section='CP', row=474, excel_formula='=IF(C429="","",0.0872614*(C429/100)-0.00249277*(C429/100)^2+0.0000274194*(C429/100)^3-0.004821*(100/C429))', computed_snapshot=0.4053989731858856),
    OutputSpec(name="c6_cp_total", desc='C6+', uom='kcal / kg.K', section='CP', row=475, excel_formula='=IF(C429="","",0.08763*(C429/100)-0.00258687*(C429/100)^2+0.0000295908*(C429/100)^3-0.021653*(100/C429))', computed_snapshot=0.4018764095677318),
    OutputSpec(name="n2_cp_total", desc='N2', uom='kcal / kg.K', section='CP', row=476, excel_formula='=IF(C429="","",0.0288541*(C429/100)-0.00118902*(C429/100)^2+0.0000185046*(C429/100)^3+0.663371*(100/C429))', computed_snapshot=0.24662917387447642),
    OutputSpec(name="h2_cp_total", desc='H2', uom='kcal / kg.K', section='CP', row=477, excel_formula='=IF(C429="","",0.4383729*(C429/100)-0.021712*(C429/100)^2+0.0003856489*(C429/100)^3+8.629312*(100/C429))', computed_snapshot=3.3897500322044243),
    OutputSpec(name="v_02_argon_cp_total", desc='02/Argon', uom='kcal / kg.K', section='CP', row=478, excel_formula='=IF(C429="","",0.0286895*(C429/100)-0.00121326*(C429/100)^2+0.0000186119*(C429/100)^3+0.518105*(100/C429))', computed_snapshot=0.21839739250139317),
    OutputSpec(name="co_cp_total", desc='CO', uom='kcal / kg.K', section='CP', row=479, excel_formula='=IF(C429="","",0.0292794*(C429/100)-0.00119378*(C429/100)^2+0.0000182626*(C429/100)^3+0.653378*(100/C429))', computed_snapshot=0.24693634437793316),
    OutputSpec(name="co2_cp_total", desc='CO2', uom='kcal / kg.K', section='CP', row=480, excel_formula='=IF(C429="","",0.0341626*(C429/100)-0.00143219*(C429/100)^2+0.0000219472*(C429/100)^3+0.297697*(100/C429))', computed_snapshot=0.20187480513197617),
    OutputSpec(name="h2s_cp_total", desc='H2S', uom='kcal / kg.K', section='CP', row=481, excel_formula='=IF(C429="","",0.0323884*(C429/100)-0.00122936*(C429/100)^2+0.0000187648*(C429/100)^3+0.502249*(100/C429))', computed_snapshot=0.23521382763360787),
    OutputSpec(name="c1_cp_total_cp_specific", desc='C1', uom='kcal / kg.K', section='CP', row=483, excel_formula='=IF(C466="","",C431*C466)', computed_snapshot=0.1795587824717643),
    OutputSpec(name="c2_cp_total_cp_specific", desc='C2', uom='kcal / kg.K', section='CP', row=484, excel_formula='=IF(C467="","",C432*C467)', computed_snapshot=0.03742303405513239),
    OutputSpec(name="c2_unsat_cp_total_2", desc='C2=', uom='kcal / kg.K', section='CP', row=485, excel_formula='=IF(C468="","",C433*C468)', computed_snapshot=0),
    OutputSpec(name="c3_cp_total_cp_specific", desc='C3', uom='kcal / kg.K', section='CP', row=486, excel_formula='=IF(C469="","",C434*C469)', computed_snapshot=0.024146711200195084),
    OutputSpec(name="c3_unsat_cp_total_2", desc='C3=', uom='kcal / kg.K', section='CP', row=487, excel_formula='=IF(C470="","",C435*C470)', computed_snapshot=0),
    OutputSpec(name="i_c4_cp_total_cp_specific", desc='i-C4', uom='kcal / kg.K', section='CP', row=488, excel_formula='=IF(C471="","",C436*C471)', computed_snapshot=0.009885502622788662),
    OutputSpec(name="n_c4_cp_total_cp_specific", desc='n-C4', uom='kcal / kg.K', section='CP', row=489, excel_formula='=IF(C472="","",C437*C472)', computed_snapshot=0.009286068836849218),
    OutputSpec(name="c4_cp_total_cp_specific", desc='C4=', uom='kcal / kg.K', section='CP', row=490, excel_formula='=IF(C473="","",C438*C473)', computed_snapshot=0),
    OutputSpec(name="c5_cp_total_cp_specific", desc='C5', uom='kcal / kg.K', section='CP', row=491, excel_formula='=IF(C474="","",C439*C474)', computed_snapshot=0.001990890911461591),
    OutputSpec(name="c6_cp_total_cp_specific", desc='C6+', uom='kcal / kg.K', section='CP', row=492, excel_formula='=IF(C475="","",C440*C475)', computed_snapshot=0),
    OutputSpec(name="n2_cp_total_cp_specific", desc='N2', uom='kcal / kg.K', section='CP', row=493, excel_formula='=IF(C476="","",C441*C476)', computed_snapshot=0),
    OutputSpec(name="h2_cp_total_cp_specific", desc='H2', uom='kcal / kg.K', section='CP', row=494, excel_formula='=IF(C477="","",C442*C477)', computed_snapshot=1.574830839841202),
    OutputSpec(name="v_02_argon_cp_total_cp_specific", desc='02/Argon', uom='kcal / kg.K', section='CP', row=495, excel_formula='=IF(C478="","",C443*C478)', computed_snapshot=0),
    OutputSpec(name="co_cp_total_cp_specific", desc='CO', uom='kcal / kg.K', section='CP', row=496, excel_formula='=IF(C479="","",C444*C479)', computed_snapshot=0),
    OutputSpec(name="co2_cp_total_cp_specific", desc='CO2', uom='kcal / kg.K', section='CP', row=497, excel_formula='=IF(C480="","",C445*C480)', computed_snapshot=0.00023573321057910647),
    OutputSpec(name="h2s_cp_total_cp_specific", desc='H2S', uom='kcal / kg.K', section='CP', row=498, excel_formula='=IF(C481="","",C446*C481)', computed_snapshot=1.3733192392290324e-07),
    OutputSpec(name='cpf_kcal_kg_k', desc='Cpf kcal / kg.K', uom='kcal / kg.K', section='CP', row=499, excel_formula='=IF(C483="","",SUM(C483:C498))', computed_snapshot=1.8373577004818964),
    OutputSpec(name='weight_h2s_in_fuel', desc='Weight % H2S in Fuel', uom=None, section='Acid dewpoint', row=502, excel_formula='=34.08/C464*C25', computed_snapshot=0.0001345412245986086),
    #OutputSpec(name='entec_flue_gas_acid_dewpoint', desc='ENTEC, Flue Gas Acid dewpoint', uom='°F', section='Acid dewpoint', row=503, excel_formula='=IF(C502<1.1,279*C502^0.0363,43.442*(LOG(C502))^2+13.516*LOG(C502)+277.8)', computed_snapshot=201.87458804519386),
    OutputSpec(name='entec_flue_gas_acid_dewpoint', desc='ENTEC, Flue Gas Acid dewpoint', uom='°F', section='Acid dewpoint', row=503, excel_formula='=((279*C502^0.0363) if (C502<1.1) else (43.442*(LOG(C502))^2+13.516*LOG(C502)+277.8))', computed_snapshot=201.87458804519386),
    OutputSpec(name='api_533_flue_gas_acid_dewpoint', desc='API 533, Flue Gas Acid dewpoint', uom='°F', section='Acid dewpoint', row=504, excel_formula='=IF(C502>0.5,-0.4468*C502^2+11.561*C502+269.07,151*C502+199.3)', computed_snapshot=199.3203157249144),
    OutputSpec(name="flue_gas_acid_dewpoint_acid_dewpoint", desc='Flue Gas Acid dewpoint', uom='°C', section='Acid dewpoint', row=505, excel_formula='=(MAX(C503,C504)-32)/1.8', computed_snapshot=94.37477113621881),
    OutputSpec(name='ghg_Ton CO2/Kg Fuel',       desc='GHG', uom='Ton CO2/Kg Fuel',  section='Fuel data', row=508, excel_formula='=C270/1000'),
    OutputSpec(name='ghg_Ton CO2/Nm3 Fuel',   desc='GHG', uom='Ton CO2/Nm3 Fuel', section='Fuel data', row=509, excel_formula='=C508*C464/22.414'),
    OutputSpec(name='ghg_Ton CO2/Gcal Fuel',  desc='GHG', uom='Ton CO2/Gcal Fuel',section='Fuel data', row=510, excel_formula='=C508*1000000/C190'),
    OutputSpec(name='ghg_Ton CO2/h',  desc='GHG Rate', uom='Ton CO2/h',   section='Fuel data', row=511, excel_formula='=C508*C419'),
    OutputSpec(name='h2o', desc='H2O', uom='Kg/Kg Fuel', section='Flue Gas- From Wet Analyzer Calcs', row=515, excel_formula='=C373', computed_snapshot=2.4352726544101335),
    OutputSpec(name="co2_wet", desc='CO2', uom='Kg/Kg Fuel', section='Flue Gas- From Wet Analyzer Calcs', row=516, excel_formula='=C270', computed_snapshot=2.6997287877411336),
    OutputSpec(name="n2_wet", desc='N2', uom='Kg/Kg Fuel', section='Flue Gas- From Wet Analyzer Calcs', row=517, excel_formula='=C350+0.79*C365', computed_snapshot=16.893129749996127),
    OutputSpec(name='o2', desc='O2', uom='Kg/Kg Fuel', section='Flue Gas- From Wet Analyzer Calcs', row=518, excel_formula='=0.21*C365', computed_snapshot=0.9350709334543161),
    OutputSpec(name="h2o_wet", desc='H2O', uom='Kg/h', section='Flue Gas- From Wet Analyzer Calcs', row=520, excel_formula='=C515*$C$419', computed_snapshot=1412.8326500439543),
    OutputSpec(name="co2_wet_wet_kg_hr", desc='CO2', uom='Kg/h', section='Flue Gas- From Wet Analyzer Calcs', row=521, excel_formula='=C516*$C$419', computed_snapshot=1566.257876988374),
    OutputSpec(name="n2_wet_wet_kg_hr", desc='N2', uom='Kg/h', section='Flue Gas- From Wet Analyzer Calcs', row=522, excel_formula='=C517*$C$419', computed_snapshot=9800.613179391383),
    OutputSpec(name="o2_wet", desc='O2', uom='Kg/h', section='Flue Gas- From Wet Analyzer Calcs', row=523, excel_formula='=C518*$C$419', computed_snapshot=542.4849420860143),
    OutputSpec(name="h2o_wet_wet_nm3_hr", desc='H2O', uom='Nm3/h', section='Flue Gas- From Wet Analyzer Calcs', row=525, excel_formula='=C520/18.015*22.414', computed_snapshot=1757.825757318079),
    OutputSpec(name="co2_wet_wet_nm3_hr", desc='CO2', uom='Nm3/h', section='Flue Gas- From Wet Analyzer Calcs', row=526, excel_formula='=C521/44.01*22.414', computed_snapshot=797.6847092664717),
    OutputSpec(name="n2_wet_wet_nm3_hr", desc='N2', uom='Nm3/h', section='Flue Gas- From Wet Analyzer Calcs', row=527, excel_formula='=C522/28.013*22.414', computed_snapshot=7841.7500375853515),
    OutputSpec(name="o2_wet_wet_nm3_hr", desc='O2', uom='Nm3/h', section='Flue Gas- From Wet Analyzer Calcs', row=528, excel_formula='=C523/31.999*22.414', computed_snapshot=379.9886712683498),
    OutputSpec(name='total_flue_gases', desc='Total Flue Gases', uom='Nm3/h', section='Flue Gas- From Wet Analyzer Calcs', row=529, excel_formula='=SUM(C525:C528)', computed_snapshot=10777.249175438252),
    OutputSpec(name="h2o_dry", desc='H2O', uom='Kg/Kg Fuel', section='Flue Gas- From Dry Analyzer Calcs', row=532, excel_formula='=C373', computed_snapshot=2.4352726544101335),
    OutputSpec(name="co2_dry", desc='CO2', uom='Kg/Kg Fuel', section='Flue Gas- From Dry Analyzer Calcs', row=533, excel_formula='=C270', computed_snapshot=2.6997287877411336),
    OutputSpec(name="n2_dry", desc='N2', uom='Kg/Kg Fuel', section='Flue Gas- From Dry Analyzer Calcs', row=534, excel_formula='=C350+0.79*C369', computed_snapshot=17.653818154719126),
    OutputSpec(name="o2_dry", desc='O2', uom='Kg/Kg Fuel', section='Flue Gas- From Dry Analyzer Calcs', row=535, excel_formula='=0.21*C369', computed_snapshot=1.137279243570556),
    OutputSpec(name="h2o_dry_dry_kg_hr", desc='H2O', uom='Kg/h', section='Flue Gas- From Dry Analyzer Calcs', row=537, excel_formula='=C532*$C$419', computed_snapshot=1412.8326500439543),
    OutputSpec(name="co2_dry_dry_kg_hr", desc='CO2', uom='Kg/h', section='Flue Gas- From Dry Analyzer Calcs', row=538, excel_formula='=C533*$C$419', computed_snapshot=1566.257876988374),
    OutputSpec(name="n2_dry_dry_kg_hr", desc='N2', uom='Kg/h', section='Flue Gas- From Dry Analyzer Calcs', row=539, excel_formula='=C534*$C$419', computed_snapshot=10241.929437247043),
    OutputSpec(name="o2_dry_dry_kg_hr", desc='O2', uom='Kg/h', section='Flue Gas- From Dry Analyzer Calcs', row=540, excel_formula='=C535*$C$419', computed_snapshot=659.7968587311898),
    OutputSpec(name="h2o_dry_dry_nm3_hr", desc='H2O', uom='Nm3/h', section='Flue Gas- From Dry Analyzer Calcs', row=542, excel_formula='=C537/18.015*22.414', computed_snapshot=1757.825757318079),
    OutputSpec(name="co2_dry_dry_nm3_hr", desc='CO2', uom='Nm3/h', section='Flue Gas- From Dry Analyzer Calcs', row=543, excel_formula='=C538/44.01*22.414', computed_snapshot=797.6847092664717),
    OutputSpec(name="n2_dry_dry_nm3_hr", desc='N2', uom='Nm3/h', section='Flue Gas- From Dry Analyzer Calcs', row=544, excel_formula='=C539/28.013*22.414', computed_snapshot=8194.859758199951),
    OutputSpec(name="o2_dry_dry_nm3_hr", desc='O2', uom='Nm3/h', section='Flue Gas- From Dry Analyzer Calcs', row=545, excel_formula='=C540/31.999*22.414', computed_snapshot=462.16090476580166),
    OutputSpec(name="total_flue_gases_dry", desc='Total Flue Gases', uom='Nm3/h', section='Flue Gas- From Dry Analyzer Calcs', row=546, excel_formula='=SUM(C542:C545)', computed_snapshot=11212.531129550303),
]


ROW_TO_INPUT = {s.row: s.name for s in INPUT_SPECS}
ROW_TO_OUTPUT = {s.row: s.name for s in OUTPUT_SPECS}
OUTPUT_SECTIONS: Dict[Optional[str], List[str]] = {}
for o in OUTPUT_SPECS:
    OUTPUT_SECTIONS.setdefault(o.section, []).append(o.name)


class Heater:
    """
    Heater calculation model.
    - Set inputs using numbers or callables (e.g., get_tag_average, extract_lab).
    - Compute outputs using auto-translated formulas; falls back to snapshot values when needed.
    """
    def __init__(self, **input_sources: Any):
        self._input_sources: Dict[str, Any] = {}
        self._input_values: Dict[str, Any] = {}
        self._output_values: Dict[str, Any] = {}
        self._output_errors: Dict[str, str] = {} 
        self.set_inputs(**input_sources)
        # Determine the correct calculation order once during initialization
        self._calculation_order = self._get_calculation_order()

    def _get_calculation_order(self) -> List[OutputSpec]:
        """
        Determines the correct calculation order based on formula dependencies (topological sort).
        This resolves all forward-reference issues automatically.
        """
        # Create a mapping from row number to its OutputSpec object
        row_to_spec = {s.row: s for s in OUTPUT_SPECS if s.row is not None}
        
        # Build dependency graphs
        # - `deps`: maps a node to the set of nodes it depends on
        # - `rev_deps`: maps a node to the set of nodes that depend on it
        deps = collections.defaultdict(set)
        rev_deps = collections.defaultdict(set)
        
        for spec in OUTPUT_SPECS:
            if not spec.excel_formula or spec.row is None:
                continue
            
            # Find all cell references like C123 in the formula
            dependencies = re.findall(r'\bC(\d+)\b', spec.excel_formula.upper())
            for row_str in dependencies:
                dep_row = int(row_str)
                # Only consider dependencies on other calculated outputs
                if dep_row in row_to_spec:
                    deps[spec.row].add(dep_row)
                    rev_deps[dep_row].add(spec.row)

        # Find initial nodes (those with no dependencies on other outputs)
        queue = collections.deque([s for s in OUTPUT_SPECS if not deps.get(s.row)])
        
        # Perform the topological sort
        ordered_specs = []
        processed_rows = set()

        while queue:
            spec = queue.popleft()
            if spec.row in processed_rows:
                continue
                
            ordered_specs.append(spec)
            processed_rows.add(spec.row)

            # For each downstream node that depended on the one just processed...
            for dependent_row in sorted(list(rev_deps.get(spec.row, []))):
                # ...remove the dependency we just satisfied
                deps[dependent_row].remove(spec.row)
                # If it has no other dependencies, add it to the queue
                if not deps[dependent_row]:
                    queue.append(row_to_spec[dependent_row])

        # Check for circular dependencies
        if len(ordered_specs) != len(OUTPUT_SPECS):
            print("Warning: Circular dependency detected or some outputs could not be ordered.")
            # Fallback to original row order if sort fails
            return sorted(OUTPUT_SPECS, key=lambda x: x.row or 0)

        return ordered_specs

    # --------------------
    # Input management
    # --------------------
    def set_inputs(self, **kwargs):
        known = {s.name for s in INPUT_SPECS}
        for k, v in kwargs.items():
            if k not in known:
                raise KeyError(f"Unknown input: {k}")
            self._input_sources[k] = v

    def set(self, name: str, value_or_callable: Any):
        known = {s.name for s in INPUT_SPECS}
        if name not in known:
            raise KeyError(f"Unknown input: {name}")
        self._input_sources[name] = value_or_callable

    def get(self, name: str) -> Any:
        # Return input if set, else output if computed
        if name in self._input_values:
            return self._input_values[name]
        if name in self._output_values:
            return self._output_values[name]
        raise KeyError(f"Unknown name: {name}")

    def _resolve_inputs(self, context: Any = None):
        self._input_values = {}
        for s in INPUT_SPECS:
            src = self._input_sources.get(s.name, None)
            if callable(src):
                try:
                    self._input_values[s.name] = src() if context is None else src(context)
                except TypeError:
                    self._input_values[s.name] = src()
            elif src is not None:
                self._input_values[s.name] = src
            else:
                self._input_values[s.name] = None

    # --------------------
    # Computation
    # --------------------
    def compute(self, context: Any = None) -> Dict[str, Any]:
        """
        Evaluate outputs. Returns a dict of output_name -> value.
        Strategy:
        1) Resolve inputs (numbers/callables).
        2) For each output in the dependency-sorted order: try to evaluate.
           - If evaluation fails, fall back to the spreadsheet snapshot.
        """
        self._resolve_inputs(context)
        self._output_values = {}

        def v(row: int):
            if row in ROW_TO_INPUT:
                name = ROW_TO_INPUT[row]
                val = self._input_values.get(name, None)
                if val is None:
                    # Allow formulas with empty inputs to proceed if possible
                    # A proper fix might be to handle this in the formula translation
                    return ""
                return val
            elif row in ROW_TO_OUTPUT:
                name = ROW_TO_OUTPUT[row]
                if name in self._output_values:
                    return self._output_values[name]
                # With the new order, this fallback should ideally not be needed
                # for forward references, but is kept for safety.
                snap = next((o.computed_snapshot for o in OUTPUT_SPECS if o.row == row), None)
                if snap is None:
                    raise ValueError(f"Output '{name}' (row {row}) not yet computed and no snapshot available.")
                return snap
            else:
                raise KeyError(f"No mapping for row {row}")

        def IF_(cond, a, b):
            return a if cond else b

        env = {"math": math, "min": min, "max": max, "abs": abs, "IF_": IF_, "v": v, "sum": sum, "range": range}

        # **MODIFIED LOOP**
        # Iterate through the pre-calculated, dependency-aware order
        for o in self._calculation_order:
            value = None
            # --- START of the new code ---
            
            # Manually handle the special case for row 503 to avoid translation errors
            if o.row == 503:
                try:
                    # Get the value of the dependency, C502
                    c502_val = v(502) 
                    
                    # This is the Python logic from the formula, written directly
                    if c502_val < 1.1:
                        value = 279 * (c502_val**0.0363)
                    else:
                        value = 43.442 * (math.log10(c502_val)**2) + 13.516 * math.log10(c502_val) + 277.8
                except Exception as e:
                    self._output_errors[o.name] = str(e)
                    value = o.computed_snapshot
            
            # Use the normal process for all other rows
            else:
                expr = _translate_formula(o.excel_formula) if o.excel_formula else None
                if expr:
                    try:
                        value = eval(expr, {"__builtins__": {}}, env)
                    except Exception as e:
                        self._output_errors[o.name] = str(e)
                        value = o.computed_snapshot
                else:
                    value = o.computed_snapshot
            
            # --- END of the new code ---

            self._output_values[o.name] = value

        return dict(self._output_values)

    # --------------------
    # Convenience methods (no changes needed below this line)
    # --------------------
    def to_dataframe(self):
        import pandas as pd
        rows = []
        for s in INPUT_SPECS:
            rows.append({
                "kind": "input",
                "name": s.name, "desc": s.desc, "uom": s.uom,
                "row": s.row, "value": self._input_values.get(s.name, None)                
            })
        for s in OUTPUT_SPECS:
            rows.append({
                "kind": "output",
                "name": s.name, "desc": s.desc, "uom": s.uom,
                "section": s.section, "row": s.row,
                "value": self._output_values.get(s.name, None),
                "error": self._output_errors.get(s.name, None)
            })
        return pd.DataFrame(rows)

    def outputs_df(self):
        """Return a pandas DataFrame of outputs (name/desc/section/uom/value/row)."""
        df = self.to_dataframe()
        return df[df["kind"] == "output"].reset_index(drop=True)

    def search_outputs(self, query: str, in_fields=("name","desc","section","uom"),
                       regex=False, case=False, limit=50):
        """
        Search outputs by substring/regex across name/desc/section/uom.
        Returns a list of dicts [{name, desc, section, uom, row, value}]
        """
        import re
        flags = 0 if case else re.I
        pat = re.compile(query if regex else re.escape(query), flags)
        rows = []
        for s in OUTPUT_SPECS:
            hay = " | ".join(str(getattr(s, f) or "") for f in in_fields)
            if pat.search(hay):
                rows.append({
                    "name": s.name, "desc": s.desc, "section": s.section, "uom": s.uom,
                    "row": s.row, "value": self._output_values.get(s.name, None)
                })
        rows.sort(key=lambda r: (r["section"] or "", r["name"]))
        return rows[:limit]

    def pick(self, query: str):
        """
        Fuzzy-pick a single output by name/desc using difflib.
        If exactly one good match is found, return its value.
        If multiple, raise with suggestions.
        """
        import difflib
        names = [s.name for s in OUTPUT_SPECS]
        descs = {s.desc: s.name for s in OUTPUT_SPECS if s.desc}
        cand_names = difflib.get_close_matches(query, names, n=6, cutoff=0.4)
        cand_from_desc = difflib.get_close_matches(query, list(descs.keys()), n=6, cutoff=0.4)
        for d in cand_from_desc:
            cand_names.append(descs[d])
        ql = query.lower()
        cand_names += [s.name for s in OUTPUT_SPECS
                       if ql in s.name.lower() or ql in (s.desc or "").lower()]
        cand = sorted(set(cand_names))
        if not cand:
            raise KeyError(f"No output matching '{query}'. Try H.search_outputs('{query}').")
        if len(cand) == 1:
            return self._output_values.get(cand[0], None)
        raise KeyError(f"Ambiguous match for '{query}': {cand[:10]} (use exact key or H.search_outputs).")

    def info(self, name_or_query: str):
        """
        Return a small info dict about an output (desc, uom, section, row, value).
        Accepts exact output name or fuzzy query.
        """
        name = None
        if name_or_query in {s.name for s in OUTPUT_SPECS}:
            name = name_or_query
        else:
            # Try fuzzy via pick() then resolve to a single name via search
            _ = self.pick(name_or_query)  # may raise if ambiguous
            hits = self.search_outputs(name_or_query, limit=5)
            if len(hits) == 1:
                name = hits[0]["name"]
            else:
                for h in hits:
                    if h["value"] == _:
                        name = h["name"]
                        break
        if not name:
            raise KeyError(f"Could not resolve '{name_or_query}' to a single output name.")
        s = next(x for x in OUTPUT_SPECS if x.name == name)
        return {
            "name": s.name, "desc": s.desc, "uom": s.uom, "section": s.section,
            "row": s.row, "value": self._output_values.get(s.name, None)
        }

    def __getitem__(self, key):
        """
        Wildcard/glob indexing:
          H['*duty*'] -> dict of {name: value, ...} for matches in name or description.
        Exact name still returns a single value.
        """
        import fnmatch
        if isinstance(key, str) and any(ch in key for ch in "*?["):
            matches = []
            kl = key.lower()
            for s in OUTPUT_SPECS:
                if (fnmatch.fnmatch(s.name, key) or
                    fnmatch.fnmatch((s.desc or ""), key) or
                    fnmatch.fnmatch(s.name.lower(), kl) or
                    fnmatch.fnmatch((s.desc or "").lower(), kl)):
                    matches.append(s.name)
            return {n: self._output_values.get(n, None) for n in sorted(set(matches))}
        if key in self._output_values:
            return self._output_values[key]
        if key in self._input_values:
            return self._input_values[key]
        raise KeyError(f"{key} not found. Use wildcards (e.g., H['*duty*']) or H.search_outputs('duty').")


# --- Formula translation helpers ---
import re as _re
from typing import Optional

def _translate_formula(expr: Optional[str]) -> Optional[str]:
    if not isinstance(expr, str) or not expr.startswith("="):
        return None
    s = expr[1:]
    s = s.replace("$", "")
    s = s.replace("^", "**")
    s = s.replace("<>", "!=")
    s = _re.sub(r"\bPI\(\)", "math.pi", s, flags=_re.I)
    s = _re.sub(r"\bPOWER\s*\(\s*([^,]+)\s*,\s*([^)]+)\)", r"(\1**\2)", s, flags=_re.I)
    s = _re.sub(r"\bLOG10\s*\(", "math.log10(", s, flags=_re.I)
    s = _re.sub(r"\bLOG\s*\(", "math.log10(", s, flags=_re.I)
    s = _re.sub(r"\bLN\s*\(", "math.log(", s, flags=_re.I)
    s = _re.sub(r"\bSQRT\s*\(", "math.sqrt(", s, flags=_re.I)
    s = _re.sub(r"\bABS\s*\(", "abs(", s, flags=_re.I)
    s = _re.sub(r"\bEXP\s*\(", "math.exp(", s, flags=_re.I)
    s = _re.sub(r"\bMIN\s*\(", "min(", s, flags=_re.I)
    s = _re.sub(r"\bMAX\s*\(", "max(", s, flags=_re.I)
    s = _re.sub(r"\bIF\s*\(", "IF_(", s, flags=_re.I)
    
    # Handle SUM with ranges - this is the critical fix
    # Pattern: SUM(C10:C25) or SUM($C$10:$C$25)
    def replace_sum_range(match):
        start = int(match.group(1))
        end = int(match.group(2))
        cells = [f'v({i})' for i in range(start, end + 1)]
        return f'sum([{", ".join(cells)}])'
    
    s = _re.sub(r'\bSUM\s*\(\s*C(\d+):C(\d+)\s*\)', replace_sum_range, s, flags=_re.I)
    
    # Convert cell references
    s = _re.sub(r"\bC(\d+)\b", r"v(\1)", s, flags=_re.I)
    
    # Convert single '=' (not part of '==', '>=', '<=', '!=') into '=='
    s = _re.sub(r'(?<![<>=!])=(?![=])', '==', s)
    return s
