class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.backpack_add_btn =  page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_backpack(self):
        self.backpack_add_btn.click()

    def get_cart_count(self):
        return self.cart_badge.inner_text()