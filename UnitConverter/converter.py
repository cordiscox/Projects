class Converter:
    
    def get_lengths():
        lengths={
            'millimeter': 'Millimeter',
            'centimeter': 'Centimeter',
            'meter':'Meter',
            'kilometer': 'Kilometer',
            'inch': 'Inch',
            'foot': 'Foot',
            'yard':'Yard',
            'mile':'Mile'
            }
        return lengths
    

    def length(unit, unit_from, unit_to):
        conversion_factors = {
            'millimeter': {
                'millimeter': 1,
                'centimeter': 0.1,
                'meter': 0.001,
                'kilometer': 0.000001,
                'inch': 0.0393701,
                'foot': 0.00328084,
                'yard': 0.00109361,
                'mile': 0.000000621371
            },
            'centimeter': {
                'millimeter': 10,
                'centimeter': 1,
                'meter': 0.01,
                'kilometer': 0.00001,
                'inch': 0.393701,
                'foot': 0.0328084,
                'yard': 0.0109361,
                'mile': 0.00000621371
            },
            'meter': {
                'millimeter': 1000,
                'centimeter': 100,
                'meter': 1,
                'kilometer': 0.001,
                'inch': 39.3701,
                'foot': 3.28084,
                'yard': 1.09361,
                'mile': 0.000621371
            },
            'kilometer': {
                'millimeter': 1000000,
                'centimeter': 100000,
                'meter': 1000,
                'kilometer': 1,
                'inch': 39370.1,
                'foot': 3280.84,
                'yard': 1093.61,
                'mile': 0.621371
            },
            'inch': {
                'millimeter': 25.4,
                'centimeter': 2.54,
                'meter': 0.0254,
                'kilometer': 0.0000254,
                'inch': 1,
                'foot': 0.0833333,
                'yard': 0.0277778,
                'mile': 0.0000157828
            },
            'foot': {
                'millimeter': 304.8,
                'centimeter': 30.48,
                'meter': 0.3048,
                'kilometer': 0.0003048,
                'inch': 12,
                'foot': 1,
                'yard': 0.333333,
                'mile': 0.000189394
            },
            'yard': {
                'millimeter': 914.4,
                'centimeter': 91.44,
                'meter': 0.9144,
                'kilometer': 0.0009144,
                'inch': 36,
                'foot': 3,
                'yard': 1,
                'mile': 0.000568182
            },
            'mile': {
                'millimeter': 1609344,
                'centimeter': 160934,
                'meter': 1609.34,
                'kilometer': 1.60934,
                'inch': 63360,
                'foot': 5280,
                'yard': 1760,
                'mile': 1
            }
        }

        unit = float(unit)
        return unit * conversion_factors[unit_from][unit_to]


    def get_weights():
        weights = {
            'milligram': 'milligram',
            'gram': 'gram',
            'kilogram': 'kilogram',
            'ounce': 'ounce',
            'pound': 'pound'
            }
        return weights
    

    def weight(unit, unit_from, unit_to):
        conversion_factors = {
            'milligram': {
                'milligram': 1,
                'gram': 0.001,
                'kilogram': 0.000001,
                'ounce': 0.000035274,
                'pound': 0.00000220462
            },
            'gram': {
                'milligram': 1000,
                'gram': 1,
                'kilogram': 0.001,
                'ounce': 0.035274,
                'pound': 0.00220462
            },
            'kilogram': {
                'milligram': 1000000,
                'gram': 1000,
                'kilogram': 1,
                'ounce': 35.274,
                'pound': 2.20462
            },
            'ounce': {
                'milligram': 28349.5,
                'gram': 28.3495,
                'kilogram': 0.0283495,
                'ounce': 1,
                'pound': 0.0625
            },
            'pound': {
                'milligram': 453592,
                'gram': 453.592,
                'kilogram': 0.453592,
                'ounce': 16,
                'pound': 1
            }
        }

        unit = float(unit)
        return f"{unit} {unit_from} are {unit * conversion_factors[unit_from][unit_to]:.2f} {unit_to}"
    

    def get_temperatures():
        temperatures = {
            'celsius': 'Celsius',
            'fahrenheit': 'Fahrenheit',
            'kelvin': 'Kelvin'
        }
        return temperatures


    def temperature(unit, unit_from, unit_to):
        to_celsius = {
            'celsius': lambda x: x,
            'fahrenheit': lambda x: (x - 32) * 5/9,
            'kelvin': lambda x: x - 273.15
        }
        
        from_celsius = {
            'celsius': lambda x: x,
            'fahrenheit': lambda x: x * 9/5 + 32,
            'kelvin': lambda x: x + 273.15
        }
        
        celsius_value = to_celsius[unit_from](float(unit))
        return from_celsius[unit_to](celsius_value)


#Length: millimeter, centimeter, meter, kilometer, inch, foot, yard, mile.
#Weight: milligram, gram, kilogram, ounce, pound.
#Temperature: Celsius, Fahrenheit, Kelvin.

    
