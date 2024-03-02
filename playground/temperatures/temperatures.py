# Nayeel Imtiaz
# temperatures.py

"""
Exercise: Temperature Converter Function

Write a Python function named convert_temperature that converts a temperature from one unit to another. The function should take three parameters:

The temperature value (a number).
The unit of the input temperature ('C' for Celsius, 'F' for Fahrenheit).
The unit of the output temperature ('C' for Celsius, 'F' for Fahrenheit).
The function should return the converted temperature.

Here are the formulas for the conversion:

From Celsius to Fahrenheit: (Celsius * 9/5) + 32
From Fahrenheit to Celsius: (Fahrenheit - 32) * 5/9
Your function should be able to handle incorrect input gracefully, such as invalid temperature units, and return a helpful message in such cases.

Bonus Challenge:

Extend your function to also support conversion to and from Kelvin. The Kelvin to Celsius formula is Kelvin - 273.15, and Celsius to Kelvin is Celsius + 273.15.
Implement error handling to ensure the temperature value is a valid number.
Once you've written your function, test it with a few different temperatures and units to ensure it works as expected.
"""

def convert_temperature(temperature_to_convert, input_type, output_type):
    if not isinstance(temperature_to_convert, (float, int)):
        raise TypeError("temperature_to_convert is not a number")
    
    if not isinstance(input_type, str):
        raise TypeError("input_type is not a string. Please enter \"c\" or \"f\" or \"k\"")
    input_type = input_type.lower()

    if not isinstance(output_type, str):
        raise TypeError("output_type is not a string. Please enter \"c\" or \"f\" or \"k\"")
    output_type = output_type.lower()

    if not (input_type == "c" or input_type == "f" or input_type == "k"):
        raise ValueError("input_type is not c or f or k")

    if not (output_type == "c" or output_type == "f" or output_type == "k"):
        raise ValueError("output_type is not c or f or k")
    
    if input_type == output_type:
        return temperature_to_convert

    elif input_type == "c" and output_type == "f":
        return (temperature_to_convert * 9/5) + 32

    elif input_type == "f" and output_type == "c":
        return (temperature_to_convert - 32) * 5/9
    
    elif input_type == "c" and output_type == "k":
        return temperature_to_convert + 273
    
    elif input_type == "k" and output_type == "c":
        return temperature_to_convert - 273
    
    elif input_type == "f" and output_type == "k":
        celcius = (temperature_to_convert - 32) * 5/9
        return celcius + 273
    
    elif input_type == "k" and output_type == "f":
        celcius = temperature_to_convert - 273
        return (celcius * 9/5) + 32 
    
    else:
        raise Exception(f"Input_type: '{input_type}' and Output_type: '{output_type}' is not covered")


def main():
    print(convert_temperature(4.44, "c", "f"))

    print(convert_temperature(40, "f", "c"))

    print(convert_temperature(27, "c", "k"))

    print(convert_temperature(330, "k", "c"))


if __name__ == '__main__':
    main()
