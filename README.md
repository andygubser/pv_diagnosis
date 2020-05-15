# pv_diagnosis

## Goal
In case of large-scale renewable energy plants, production output is regularly reviewed to ensure ROI. This is different for small plants. By comparing predicted production based on past meteorological data with actual production of a PV power plant, we estimate plant's condition and predict next required maintenance. The analysis detects performance losses and, therby, enhances economic profits. This task was part of the Energy Hackdays 2019 (https://hack.opendata.ch/project/284). 

## Data Sources
- Effective Power Production: https://github.com/zuzfil/PV-Optimisation
- Weather Conditions (Solar): https://www.renewables.ninja/

### Weather Condition Data

#### Air temperature (°C)
Air temperature at 2 meters above ground. T2M variable in MERRA-2, converted from K.

#### Precipitation (mm / hour)
Total bias-corrected precipitation, over land only. PRECTOTLAND variable in MERRA-2, converted from kg m⁻² s⁻¹

#### Snowfall (mm / hour)
Total bias-corrected precipitation in the form of snow, over land only. PRECSNOLAND variable in MERRA-2, converted from kg m⁻² s⁻¹

#### Snow mass (kg / m²)
Amount of snow per land area. SNOMAS variable in MERRA-2, in native units.

#### Air density (kg / m³)
Air density at ground level. RHOA variable in MERRA-2, in native units.

#### Ground-level solar irradiance (W / m²)
Surface-level incident shortwave radiation flux, considering cloud cover and aerosols. SWGDN variable in MERRA-2, in native units. Note, MERRA-2 uses the mean annual climate for aerosols, rather than time-varying quantity.

#### Top of atmosphere solar irradiance (W / m²)
Top of atmosphere incident shortwave radiation flux, before cloud cover and aerosol influences. SWTDN variable in MERRA-2, in native units.

#### Cloud cover fraction
Fraction of cloud cover, averaged over grid cell and summed over all height above ground. CLDTOT variable in MERRA-2, in native units (a [0, 1] scale).
