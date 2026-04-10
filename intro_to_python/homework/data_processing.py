class ProcessData:
    def __init__(self, data):
        """Initialize the class with a list of sales dictionaries."""
        self.data = data

    def calculate_total_revenue(self):
        """Returns the sum of (qty * price) for all items."""
        total = sum(item['qty'] * item['price'] for item in self.data)
        return round(total, 2)

    def get_most_popular(self):
        """Returns the name of the product with the highest total quantity."""
        counts = {}
        for item in self.data:
            name = item['product']
            counts[name] = counts.get(name, 0) + item['qty']

        # Returns the key with the highest value
        return max(counts, key=counts.get)

    def calculate_average_price(self):
        """Returns the average price of all unique products."""
        # Use a dictionary comprehension to get unique product: price pairs
        unique_products = {item['product']: item['price'] for item in self.data}

        if not unique_products:
            return 0.0

        avg = sum(unique_products.values()) / len(unique_products)
        return round(avg, 2)


# --- Execution ---
sales = [
    {'product': 'Widget', 'qty': 10, 'price': 5.99},
    {'product': 'Gadget', 'qty': 5, 'price': 12.50},
    {'product': 'Widget', 'qty': 3, 'price': 5.99}
]

# Create an instance of the class
processor = ProcessData(sales)

# Access the results
print(f"Total Revenue: ${processor.calculate_total_revenue()}")
print(f"Most Popular Product: {processor.get_most_popular()}")
print(f"Avg Product Price: ${processor.calculate_average_price()}")
