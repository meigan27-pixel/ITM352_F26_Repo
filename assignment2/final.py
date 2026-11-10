from os import replace

import pandas as pd
import ssl
import time
import openpyxl


#Temporary fix
ssl._create_default_https_context = ssl._create_unverified_context

#addition requirement 1
def export_to_excel(dataframe, operation_name):
    export_choice = input("Do you want to export the results to an Excel file? (yes/no): ").strip().lower()
    if export_choice == 'yes':
        filename = input(f"Enter a filename for the Excel file (e.g., {operation_name}.xlsx): ")
        if not filename.endswith('.xlsx'):
            filename += '.xlsx'
        dataframe.to_excel(filename, index=True)
        print(f"Results exported to {filename}.")
    else:
        print("Results not exported.")

#additional requirement 2
analytics_history = {}
def show_saved_results(data=None):
    for name, result in analytics_history.items():
        print(f"\n{name}")
        print(result)
    if not analytics_history:
        print("No saved results available.")

#loads the file while measuring load time, prints # of rows, list of columns, replaces missing values with 0
def load_csv(filepath):
    print(f"Loading CSV file from: {filepath}")
    start_time = time.time()

    try:
        df = pd.read_csv(filepath,engine='pyarrow',on_bad_lines='skip')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        print(f"List of columns: {list(df.columns)}")
        df.fillna(0, inplace=True)

        #requirements and missing
        required_fields = [
                "sales_region", "order_type", "unit_price", "quantity", 
                "customer_type", "employee_name", "product_category",
                "order_number", "employee_id", "job_title", 
                "order_date", "customer_name", "customer_state", 
                "product_number", "produce_name"
            ]
        missing_fields = [field for field in required_fields if field not in df.columns]
        if missing_fields:
            print(f"Warning: Missing fields {missing_fields}. Some analytics may not work.")
        else:
            print("All required fields are present.")
            
        return df

    except Exception as e:
        print("Error reading the CSV file:", e)
        return None

#I used copilot with the prompt "explain the algorithm for the analytical tasks 'pasted tasks' and provide a step-by-step breakdown."

#Analytical task #1
def display_initial_rows(data):
    while True:
        response = input(
            f"\nHow many initial rows would you like to see? "
            f"(1-{len(data)}, or 'all' or enter to skip): "
        ).strip().lower()

        if response == "":
            print("Skipping initial rows display.")
            return

        if response == "all":
            print(data)
            return

        try:
            num_rows = int(response)
        except ValueError:
            print(f"Invalid input '{response}'. Please enter a whole number, 'all', or press Enter to skip.")
            continue

        if num_rows < 1:
            print("Please enter a number greater than 0.")
            continue

        if num_rows > len(data):
            print(f"Only {len(data)} rows available; showing all of them.")
            continue

        export_to_excel(data.head(num_rows), "initial_rows")
        analytics_history["initial_rows"] = data.head(num_rows)

        print(data.head(num_rows))
        return

#Analytical task #2
def total_sales_by_region_order_type(data):
    summary = data.groupby(['sales_region', 'order_type']).agg({'unit_price': 'sum'}).reset_index()
    print(summary)
    export_to_excel(summary, "total_sales_by_region_order_type")
    analytics_history["total_sales_by_region_order_type"] = summary

#Analytical task #3
def average_sales_by_region(data):
    summary = data.groupby(['sales_region', 'customer_state', 'order_type']).agg({'unit_price': 'mean'}).reset_index()
    print(summary)
    export_to_excel(summary, "average_sales_by_region")
    analytics_history["average_sales_by_region"] = summary
    

#Analytical task #4
def sales_by_customer_type(data):
    summary = data.groupby(['customer_type', 'order_type', 'customer_state']).agg({'unit_price': 'sum'}).reset_index()
    print(summary)
    export_to_excel(summary, "sales_by_customer_type")
    analytics_history["sales_by_customer_type"] = summary

#Analytical task #5
def total_sales_quantity_price_by_region_product(data):
    summary = data.groupby(['sales_region', 'product_category']).agg({'quantity': 'sum', 'unit_price': 'sum'}).reset_index()
    print(summary)
    export_to_excel(summary, "total_sales_quantity_price_by_region_product")
    analytics_history["total_sales_quantity_price_by_region_product"] = summary

#Analytical task #6
def total_sales_quantity_price_customer_type(data):
    summary = data.groupby(['customer_type']).agg({'quantity': 'sum', 'unit_price': 'sum'}).reset_index()
    print(summary)
    export_to_excel(summary, "total_sales_quantity_price_by_customer_type")
    analytics_history["total_sales_quantity_price_by_customer_type"] = summary

#Analytical task #7
def max_min_sales_price_by_category(data):
    summary = data.groupby(['product_category']).agg({'unit_price': ['max', 'min']}).reset_index()
    print(summary)
    export_to_excel(summary, "max_min_sales_price_by_category")
    analytics_history["max_min_sales_price_by_category"] = summary

#Analytical task #8
def unique_employees_by_region(data):
    summary = data.groupby(['sales_region']).agg({'employee_name': pd.Series.nunique}).reset_index()
    print(summary)
    export_to_excel(summary, "unique_employees_by_region")
    analytics_history["unique_employees_by_region"] = summary


def get_user_selection(options, prompt, required=False, single=False):
    while True:
        print(prompt)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        choice = input("Enter the number(s) of your choice(s), separated by commas: ").strip()
        if not choice:
            if required:
                print("A selection is required.")
                continue
            return []

        try:
            indexes = [int(i) for i in choice.split(',')]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
            continue

        if any(i < 1 or i > len(options) for i in indexes):
            print(f"Each number must be between 1 and {len(options)}.")
            continue

        selected = list(dict.fromkeys(options[i - 1] for i in indexes))
        if single and len(selected) != 1:
            print("Please select exactly one option.")
            continue
        return selected


def generate_custom_pivot_table(data):
    """Interactively build and display a pivot table."""
    row_options = list(data.columns)
    rows = get_user_selection(row_options, "\nSelect rows (required):", required=True)

    col_options = [col for col in row_options if col not in rows]
    cols = get_user_selection(col_options, "\nSelect columns (optional, Enter to skip):")

    value_options = list(data.select_dtypes(include=['number']).columns)
    if not value_options:
        print("No numeric columns available to aggregate.")
        return
    values = get_user_selection(value_options, "\nSelect value to aggregate:", required=True, single=True)

    agg_options = ['sum', 'mean', 'count']
    agg_func = get_user_selection(agg_options, "\nSelect aggregation function:", required=True, single=True)[0]

    try:
        pivot_table = pd.pivot_table(
            data,
            index=rows,
            columns=cols if cols else None,
            values=values,
            aggfunc=agg_func
        )
    except Exception as e:
        print("Could not create the pivot table:", e)
        return

    print("\nCustom pivot table:")
    print(pivot_table)
    analytics_history["generate_custom_pivot_table"] = pivot_table

#Analytical task #3
def average_sales_by_region(data):
    """Pivot average sales (quantity * unit_price) by region, with state and sale type sub-columns."""
    required = ["sales_region", "customer_state", "order_type", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Missing required columns:", ", ".join(missing))
        return

    sales = data.assign(sales=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales,
        index="sales_region",
        columns=["customer_state", "order_type"],
        values="sales",
        aggfunc="mean",
    )
    print("\nAverage sales by region, by state and sale type:")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))
    analytics_history["average_sales_by_region"] = pivot_table


def exit_program(data=None):
    print("Exiting the program. Goodbye!")
    raise SystemExit(0)


menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Total sales by region and order type", total_sales_by_region_order_type),
    ("Average sales by region with average sales by state and sale type", average_sales_by_region),
    ("Sales by customer type and order type by state", sales_by_customer_type),
    ("Total sales quantity and price by region and product", total_sales_quantity_price_by_region_product),
    ("Total sales quantity and price by customer type", total_sales_quantity_price_customer_type),
    ("Max and min sales price of sales by category", max_min_sales_price_by_category),
    ("Number of unique employees by region", unique_employees_by_region),
    ("Create a custom pivot table", generate_custom_pivot_table),
    ("Show saved results", show_saved_results),
    ("Exit the program", exit_program)
)


def display_menu():
    """Show the menu and return a valid selection as an index into menu_options."""
    while True:
        print("\nSales Data Menu")
        for number, (description, _) in enumerate(menu_options, start=1):
            print(f"  {number}. {description}")

        choice = input(f"Select an option (1-{len(menu_options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            return int(choice) - 1
        print(f"Invalid selection '{choice}'. Please enter a number from 1 to {len(menu_options)}.")


def main():
    csv_file = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K&export=download'
    # csv_file = "junk.csv"  # Intentionally incorrect path to test error handling
    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    try:
        while True:
            selection = display_menu()
            _, action = menu_options[selection]
            action(sales_data)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")


if __name__ == "__main__":
    main()