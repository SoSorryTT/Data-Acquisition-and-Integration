# 1
# Find the input voltage (Va = .... V)
# Example ADC_Value = 108
#         ADC_Voltage = 3.3 v

def find_Va(resolution, ADC_value, ADC_voltage):
    if resolution == 8: # If it was 8-bit resolution
        return (ADC_value*ADC_voltage)/255
    elif resolution == 10: # If it was 10-bit resolution
        return (ADC_value*ADC_voltage)/1023
    elif resolution == 12: # If it was 12-bit resolution
        return (ADC_value*ADC_voltage)/4095
    elif resolution == 14: # If it was 14-bit resolution
        return (ADC_value*ADC_voltage)/16383
    else:
        return print("The resolution not match this function")

# 2
# Find the current(I) passing through R1 and LDR
# Example R1 = 10,000 ohms
#         Va = from the function find_Va

def find_current(ADC_voltage, Va, R):
    return (ADC_voltage-Va)/R # I = (ADC_voltage-Va)/R   mA(unit)

# 3
# Find the resistance of LDR
# Example I = from the function find_current
#         Va = from the function find_Va

def find_resistance_LDR(Va, I):
    return Va/I # R_LDR = V/I   ohms(unit)

# 4
