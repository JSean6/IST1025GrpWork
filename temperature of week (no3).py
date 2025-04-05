def get_temperature(day_name):
    while True:
        try:
            temp = float(input(f"Enter Temperature For {day_name}: "))
            return temp
        except ValueError:
            print("Please enter a valid number.")

def display_statistics(temperatures):
    """Display temperature statistics in a formatted manner."""
    print("\nTemperature Statistics:")
    print("-" * 50)
    
    # Headers
    print(f"{'Day':<15} {'Temperature':<15}")
    print("-" * 50)
    
    # Display Daily Temperatures
    for day, temp in zip(["Monday", "Tuesday", "Wednesday", "Thursday", 
                         "Friday", "Saturday", "Sunday"], temperatures):
        print(f"{day:<15} {temp:>10.1f}°C")
    
    print("-" * 50)
    
    # Display Summary Statistics
    print(f"Highest Temperature: {max(temperatures):.1f}°C")
    print(f"Lowest Temperature: {min(temperatures):.1f}°C")
    print(f"Total Temperature: {sum(temperatures):.1f}°C")
    print(f"Average Temperature: {(sum(temperatures)/len(temperatures)):.1f}°C")

def main():
    """Main program function."""
    print("Weekly Temperature Recorder")
    print("=" * 25)
    
    # Get temperatures for each day
    temperatures = [
        get_temperature("Monday"),
        get_temperature("Tuesday"),
        get_temperature("Wednesday"),
        get_temperature("Thursday"),
        get_temperature("Friday"),
        get_temperature("Saturday"),
        get_temperature("Sunday")
    ]
    
    # Displaying the results
    display_statistics(temperatures)

if __name__ == "__main__":
    main()
