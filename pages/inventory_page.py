class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.backpack_add_btn = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")
        self.item_prices = page.locator(".inventory_item_price")

    def add_backpack(self):
        self.backpack_add_btn.click()

    def get_cart_count(self):
        return self.cart_badge.inner_text()
    
    def select_sort_option(self, option_value):
        self.sort_dropdown.select_option(option_value)

    def get_all_item_prices(self):
        return self.item_prices.all_text_contents()