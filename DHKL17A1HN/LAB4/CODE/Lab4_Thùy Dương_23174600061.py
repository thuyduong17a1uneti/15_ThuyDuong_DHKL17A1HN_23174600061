import sqlite3

conn = sqlite3.connect('D:\KHDL\Lập trình python nâng cao\DHKL17A1HN\LAB4\DATA/product.db')
c = conn.cursor()

def create_table():
    c.execute('''
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            amount INTEGER NOT NULL
        )
    ''')
    conn.commit()

def display_products():
    c.execute("SELECT * FROM product")
    products = c.fetchall()
    if products:
        print("ID | Name | Price | Amount")
        for product in products:
            print(f"{product[0]} | {product[1]} | {product[2]:.2f} | {product[3]}")
    else:
        print("No products found.")

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    amount = int(input("Enter product amount: "))
    
    c.execute("INSERT INTO product (name, price, amount) VALUES (?, ?, ?)", (name, price, amount))
    conn.commit()
    print("Product added successfully.")

# Tìm kiếm sản phẩm theo tên
def search_product():
    search_name = input("Enter product name to search: ")
    c.execute("SELECT * FROM product WHERE name LIKE ?", ('%' + search_name + '%',))
    products = c.fetchall()
    if products:
        print("ID | Name | Price | Amount")
        for product in products:
            print(f"{product[0]} | {product[1]} | {product[2]:.2f} | {product[3]}")
    else:
        print("No products found matching that name.")

# Cập nhật thông tin sản phẩm
def update_product():
    product_id = int(input("Enter product ID to update: "))
    new_price = float(input("Enter new price: "))
    new_amount = int(input("Enter new amount: "))
    
    c.execute("UPDATE product SET price = ?, amount = ? WHERE id = ?", (new_price, new_amount, product_id))
    conn.commit()
    print("Product updated successfully.")

# Xóa sản phẩm
def delete_product():
    product_id = int(input("Enter product ID to delete: "))
    
    c.execute("DELETE FROM product WHERE id = ?", (product_id,))
    conn.commit()
    print("Product deleted successfully.")

# Menu giao diện console
def menu():
    while True:
        print("\n--- Product Management ---")
        print("1. Display Products")
        print("2. Add New Product")
        print("3. Search Product by Name")
        print("4. Update Product Information")
        print("5. Delete Product")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_products()
        elif choice == '2':
            add_product()
        elif choice == '3':
            search_product()
        elif choice == '4':
            update_product()
        elif choice == '5':
            delete_product()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Tạo bảng nếu chưa có và chạy menu
create_table()
menu()

# Đóng kết nối khi thoát
conn.close()
