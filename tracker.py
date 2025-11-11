# tracker.py

# Task 1: Setup & Introduction
# Author: [Your Name]
# Date: November 11, 2025
# Project Title: Daily Calorie Tracker

import time

def main():
    """
    Main function to run the Daily Calorie Tracker CLI tool.
    """
    # Print a welcome message describing what the tool does [cite: 34]
    print("\n" + "="*50)
    print("      👋 Welcome to the Daily Calorie Tracker CLI Tool")
    print("="*50)
    print("This tool helps you log your meals, track total calories consumed,")
    print("and compare your intake against a personal daily limit.")
    print("---------------------------------------------------\n")

    # Task 2: Input & Data Collection
    meal_names = []
    calorie_amounts = []

    # Ask the user how many meals they want to enter [cite: 41]
    while True:
        try:
            num_meals = int(input("How many meals did you have today? (Enter a number): "))
            if num_meals >= 0:
                break
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print(f"\n--- Entering details for {num_meals} meals ---")
    
    # Loop accordingly to accept meal data [cite: 41, 37]
    for i in range(num_meals):
        print(f"\nMeal #{i + 1}:")
        
        # Accept Meal name (e.g., "Breakfast") [cite: 38]
        meal_name = input("  Enter meal name: ")
        
        # Accept Calorie amount (e.g., "350") - convert to int or float [cite: 40]
        while True:
            try:
                calorie_amount = float(input("  Enter calorie amount: "))
                if calorie_amount >= 0:
                    break
                else:
                    print("Calorie amount must be non-negative.")
            except ValueError:
                print("Invalid input. Please enter a number for calories.")
        
        # Store data in lists [cite: 39]
        meal_names.append(meal_name)
        calorie_amounts.append(calorie_amount)

    # Handle the case where no meals were entered
    if not calorie_amounts:
        print("\nNo meals entered. Exiting program.")
        return

    # Task 3: Calorie Calculations
    # Use sum() to calculate total calorie intake [cite: 44]
    total_calories = sum(calorie_amounts)
    
    # Compute average calorie per meal (Use arithmetic operators) [cite: 45, 49]
    average_calories = total_calories / len(calorie_amounts)

    # Ask user to input their daily calorie limit [cite: 50]
    while True:
        try:
            daily_limit = float(input("\nEnter your daily calorie limit: "))
            if daily_limit >= 0:
                break
            else:
                print("Limit must be non-negative.")
        except ValueError:
            print("Invalid input. Please enter a number for the limit.")

    # Task 4: Exceed Limit Warning System
    # Compare total calorie intake to daily limit [cite: 50]
    limit_status_message = ""
    # Use if...else with comparison operators [cite: 53]
    if total_calories > daily_limit:
        # If calorie intake > daily limit → show a warning message [cite: 54]
        exceeded_by = total_calories - daily_limit
        limit_status_message = f"🚨 WARNING: You have exceeded your daily limit by {exceeded_by:.2f} calories!"
        limit_met = "Exceeded"
    else:
        # Else → show a success/within-limit message [cite: 55]
        remaining = daily_limit - total_calories
        limit_status_message = f"✅ Success: You are within your daily limit. {remaining:.2f} calories remaining."
        limit_met = "Within Limit"

    # Task 5: Neatly Formatted Output
    # Print a summary report [cite: 58]
    report_lines = []
    report_lines.append("\n" + "="*50)
    report_lines.append("        🍽️  DAILY CALORIE TRACKING REPORT")
    report_lines.append("="*50)
    
    # Use f-strings and escape characters (\t, \n) for neat formatting [cite: 58, 71]
    
    # Table Header
    report_lines.append(f"{'Meal Name':<15}\t{'Calories':>10}")
    report_lines.append("-" * 27)

    # Meal Details
    for meal, cal in zip(meal_names, calorie_amounts):
        report_lines.append(f"{meal:<15}\t{cal:>10.2f}")

    # Summary
    report_lines.append("-" * 27)
    report_lines.append(f"{'Total:':<15}\t{total_calories:>10.2f}")
    report_lines.append(f"{'Average:':<15}\t{average_calories:>10.2f}")
    report_lines.append("-" * 27)
    report_lines.append(f"\nDaily Calorie Limit: {daily_limit:.2f}")
    report_lines.append(limit_status_message)
    report_lines.append("\n" + "="*50 + "\n")

    # Print report to screen [cite: 72]
    final_report = "\n".join(report_lines)
    print(final_report)

    # Task 6 (Bonus): Save Session Log to File
    # Ask user if they want to save the report [cite: 74]
    save_log = input("Do you want to save the session report to a file? (y/n): ").strip().lower()

    if save_log == 'y':
        # Use open("filename.txt", "w") to write session data [cite: 75]
        filename = "calorie_log.txt"
        
        # Include timestamp [cite: 76]
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        log_content = f"Session Timestamp: {timestamp}\n"
        log_content += f"Daily Limit Set: {daily_limit:.2f}\n"
        log_content += f"Limit Status: {limit_met}\n\n"
        log_content += "--- MEAL LOG DETAILS ---\n"
        
        # Include meal details, total & average calories, limit status [cite: 76]
        log_content += f"{'Meal Name':<15}{'Calories':>10}\n"
        log_content += "-" * 25 + "\n"
        for meal, cal in zip(meal_names, calorie_amounts):
            log_content += f"{meal:<15}{cal:>10.2f}\n"
            
        log_content += "-" * 25 + "\n"
        log_content += f"Total Calories Consumed: {total_calories:.2f}\n"
        log_content += f"Average Calories per Meal: {average_calories:.2f}\n"
        
        try:
            with open(filename, "w") as file:
                file.write(log_content)
            print(f"File saved successfully! Check the '{filename}' file.") # Deliverable: A .txt file [cite: 77]
        except IOError:
            print("Error: Could not write the log file.")

if __name__ == "__main__":
    main()

# End of tracker.py