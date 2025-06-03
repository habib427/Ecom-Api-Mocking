from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()


        def handle_menproducts_api(route, request):
            mock_response = [
                {"id": 101, "name": "Mock Hoodie", "price": "1999", "image": "mock-image.jpg"},
                {"id": 102, "name": "Mock T-shirt", "price": "999", "image": "mock-image2.jpg"},
            ]
            route.fulfill(status=200, content_type="application/json", body=str(mock_response))
            print("Mocked products API with 2 fake items")

        def handle_womenproducts_api(route, request):
            mock_response = [
                {"id": 101, "name": "Mock Hoodie", "price": "1999", "image": "mock-image.jpg"},
                {"id": 102, "name": "Mock T-shirt", "price": "999", "image": "mock-image2.jpg"},
            ]
            route.fulfill(status=200, content_type="application/json", body=str(mock_response))

        print("Mocked products API with 2 fake items")

        def handle_cart_api(route, request):
            route.fulfill(status=200, content_type="application/json", body='{"success": true, "message": "Item added"}')

        print("Mocked cart add API for adding product")
        def handle_login_api(route, request):
            route.fulfill(status=200, content_type="application/json", body='{"token": "mock-token", "user": {"name": "Test User"}}')

        print("Mocked login API")

        page.route("https://hhwears.com/product-category/men-hoodies/", handle_menproducts_api)
        page.route("https://hhwears.com/product-category/women-hoodies/", handle_womenproducts_api)
        page.route("https://hhwears.com/shop-2/", handle_cart_api)
        page.route("https://hhwears.com/my-account-2/", handle_login_api)


        page.goto("https://hhwears.com")


        page.wait_for_timeout(3000)
        page.screenshot(path="mocked_products.png")

        browser.close()

run()
