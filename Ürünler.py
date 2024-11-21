from datetime import datetime

# Product class
class Product:
    def _init_(self, name=None, price=0, quantity=1):
        # Default values
        self._name = name if name is not None else "Unknown"
        self._price = price if price >= 0 else 0
        self._quantity = quantity if quantity >= 1 else 1

        # Data validation
        if len(self._name) < 3 or len(self._name) > 10:
            raise ValueError("Product name must be between 3 and 10 characters.")
        if self._price < 0:
            raise ValueError("Price cannot be less than 0.")
        if self._quantity < 1:
            raise ValueError("Quantity cannot be less than 1.")

        # Print product name and timestamp
        print(f"Product Name: {self._name}, Date: {datetime.now()}")

    # Getter and Setter methods
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if 3 <= len(value) <= 10:
            self._name = value
        else:
            raise ValueError("Product name must be between 3 and 10 characters.")
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be less than 0.")
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if value >= 1:
            self._quantity = value
        else:
            raise ValueError("Quantity cannot be less than 1.")
    
    def get_total_price(self):
        """Calculates the total price"""
        return self._price * self._quantity
    
    def _str_(self):
        """Overrides the base class method for string representation"""
        return f"Product: {self._name}, Price: {self._price}, Quantity: {self._quantity}, Total: {self.get_total_price()}"

# ProductHelper class
class ProductHelper:

    @staticmethod
    def create_item_from_text(file_path):
        """Reads a text file and creates products"""
        product_list = []
        
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        name, price, quantity = parts
                        try:
                            product = Product(name.strip(), float(price.strip()), int(quantity.strip()))
                            product_list.append(product)
                        except ValueError as e:
                            print(f"Error: {e} - Line: {line.strip()}")
                    else:
                        print(f"Invalid line format: {line.strip()}")
        except FileNotFoundError:
            print(f"{file_path} not found.")
        
        return product_list
    
    @staticmethod
    def get_total_balance(products):
        """Calculates the total balance of products, including 20% tax"""
        total_balance = 0
        for product in products:
            total_balance += product.get_total_price()
        
        # Add 20% tax
        total_balance_with_tax = total_balance * 1.20
        return total_balance_with_tax

# Main function (test code)
if _name_ == "_main_":
    # File path and content
    file_path = "Products.txt"
    
    # Create products using the text file
    product_list = ProductHelper.create_item_from_text(file_path)
    
    # Calculate and print the total balance of products
    if product_list:
        total_balance = ProductHelper.get_total_balance(product_list)
        print(f"Total Balance (Including Tax): {total_balance:.2f} TL")
    else:
        print("No products were found.")