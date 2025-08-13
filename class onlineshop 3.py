import datetime

class OnlineShop:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.__products = [] 
        self.order_counter = 0 

    def add_product(self, product):
        """เพิ่มออบเจกต์สินค้า (Product) เข้าไปในร้านค้า"""
        self.__products.append(product)

    def addingItemsToCart(self, customer, product_name, quantity):
        """เพิ่มสินค้าลงในตะกร้า (cart) ของลูกค้า"""
        found_product = None
        for product in self.__products:
            if product.name.lower() == product_name.lower():
                found_product = product
                break

        if found_product:
            customer.add_to_cart(found_product, quantity)
            print(f"เพิ่ม {quantity} ชิ้น ของ {product_name} ลงในตะกร้าของคุณ {customer.name} เรียบร้อยแล้ว")
        else:
            print(f"ไม่พบสินค้าชื่อ '{product_name}' ในร้านค้า")

    def checkOut(self, customer):
        """ดำเนินการชำระเงินและสร้างรายการคำสั่งซื้อ"""
        if not customer.cart:
            print("ตะกร้าสินค้าของคุณว่างเปล่า ไม่สามารถดำเนินการชำระเงินได้")
            return None

        self.order_counter += 1
        order_id = f"ORDER-{self.order_counter}-{datetime.date.today()}"
        
        total_price = sum(item[0].price * item[1] for item in customer.cart)
        
        new_order = {
            "order_id": order_id,
            "items": customer.cart,
            "total_price": total_price,
            "status": "Processing"
        }
        
        customer.past_orders.append(new_order)
        
        customer.cart = []
        
        print(f"\n--- การชำระเงินเสร็จสมบูรณ์ ---")
        print(f"หมายเลขคำสั่งซื้อ: {order_id}")
        print(f"ยอดรวม: {total_price:.2f} บาท")
        return new_order

    def orderTracking(self, customer, order_id):
        """ตรวจสอบสถานะของคำสั่งซื้อ"""
        print(f"\n--- ตรวจสอบสถานะคำสั่งซื้อสำหรับ {customer.name} ---")
        found_order = None
        for order in customer.past_orders:
            if order["order_id"] == order_id:
                found_order = order
                break
        
        if found_order:
            print(f"หมายเลขคำสั่งซื้อ: {found_order['order_id']}")
            print(f"สถานะ: {found_order['status']}")
            print(f"ยอดรวม: {found_order['total_price']:.2f} บาท")
            print("รายการสินค้า:")
            for product, quantity in found_order['items']:
                print(f"- {product.name} ({product.description}): {quantity} ชิ้น")
        else:
            print(f"ไม่พบคำสั่งซื้อหมายเลข '{order_id}' ในประวัติของคุณ")

class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = [] 
        self.past_orders = [] 

    def add_to_cart(self, product, quantity):
        """เพิ่มสินค้าลงในตะกร้าของลูกค้า"""
        for item in self.cart:
            if item[0].name == product.name:
                item[1] += quantity 
                return
        self.cart.append([product, quantity])

    def show_cart(self):
        """แสดงรายการสินค้าในตะกร้า"""
        print(f"\n--- ตะกร้าสินค้าของคุณ {self.name} ---")
        if not self.cart:
            print("ตะกร้าสินค้าว่างเปล่า")
            return
        
        total_price = 0
        for product, quantity in self.cart:
            item_total = product.price * quantity
            total_price += item_total
            print(f"- {product.name} ({product.description}): {quantity} ชิ้น x {product.price:.2f} = {item_total:.2f} บาท")
        print(f"ราคารวมทั้งหมด: {total_price:.2f} บาท")


my_shop = OnlineShop("Candyshop", "www.Candyshop.com")

product1 = Product("Pizza", "ของกิน", 20.00)
product2 = Product("Hamberker", "ของกิน", 20.00)
product3 = Product("Snack", "ของกิน", 20.00)
my_shop.add_product(product1)
my_shop.add_product(product2)
my_shop.add_product(product3)

customer1 = Customer("yoyo", "thanaphon@gmail.com", "chainat")

my_shop.addingItemsToCart(customer1, "Pizza", 1)
my_shop.addingItemsToCart(customer1, "Hamberker", 1)
my_shop.addingItemsToCart(customer1, "Snack", 1) 
customer1.show_cart()

order1 = my_shop.checkOut(customer1)
if order1:
    customer1.show_cart() 

my_shop.orderTracking(customer1, order1['order_id'])
my_shop.orderTracking(customer1, "ORDER-999-2025-08-12")