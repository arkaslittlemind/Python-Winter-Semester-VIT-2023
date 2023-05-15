def map_country_capital():
    country_capital = {
        'India': 'New Delhi',
        'United States': 'Washington, D.C.',
        'United Kingdom': 'London',
        'Canada': 'Ottawa',
        'Australia': 'Canberra',
        'Germany': 'Berlin',
        'France': 'Paris',
        'Japan': 'Tokyo',
        'China': 'Beijing',
        'Brazil': 'Brasília'
    }
    return country_capital


def swap_elements(country_capital, key1, key2):
    if key1 not in country_capital or key2 not in country_capital:
        print("Invalid keys!")
        return

    country_capital[key1], country_capital[key2] = country_capital[key2], country_capital[key1]


# Example usage:
country_capital = map_country_capital()
print("Original mapping:")
print(country_capital)

key1 = 'India'
key2 = 'Germany'

swap_elements(country_capital, key1, key2)

print("\nAfter swapping elements:")
print(country_capital)
