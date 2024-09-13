def calculate_total_sales(sales_totals):
    total = 0
    
    for item, item_info in sales_totals.items():
        total += item_info["quantity"] * item_info["price"]
    return total

def calculate_average_sales(sales_totals):
    if not sales_totals:
        return 0.0
    
    return calculate_total_sales(sales_totals) / len(sales_totals)

def filter_to_better_than_average_sales(sales_totals):
    filtered_list = {}
    
    if not sales_totals:
        return filtered_list
    
    average_sales = calculate_total_sales(sales_totals) / len(sales_totals)

    for item, item_info in sales_totals.items():
        if item_info["quantity"] * item_info["price"] > average_sales:
            filtered_list[item] = item_info
    return filtered_list
    
def ninety_nine_bottles(count, beverage):
    lines = []
    
    for i in range(count, 0, -1):
        if i == 1:
            lines.append(f"{i} bottle of {beverage} on the wall, {i} bottle of {beverage}")
            lines.append(f"If one of those bottles should happen to fall, {i - 1} bottles of {beverage} on the wall")
        elif i == 2: 
            lines.append(f"{i} bottles of {beverage} on the wall, {i} bottles of {beverage}")
            lines.append(f"If one of those bottles should happen to fall, {i - 1} bottle of {beverage} on the wall")
        else:
            lines.append(f"{i} bottles of {beverage} on the wall, {i} bottles of {beverage}")
            lines.append(f"If one of those bottles should happen to fall, {i - 1} bottles of {beverage} on the wall")

    return lines