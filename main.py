from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import executor
import logging

API_TOKEN = '6892270798:AAESARJjgs0xZ3sCRRZcVwcrSYlrkftUS9Y'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

commands_list = "/start - Start the bot\n" + \
                "/products - View available products\n" + \
                "/cart - View your shopping cart\n" + \
                "/order - Place an order\n" + \
                "/menu - View menu of commands\n" + \
                "/links - View links to our e-shop\n" + \
                "/search - Search for products"

# Example database of products
products_db = {
    1: {"name": "Product 1", "price": 10},
    2: {"name": "Product 2", "price": 20},
    3: {"name": "Product 3", "price": 30}
}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Your existing start functionality
    await message.answer("Welcome to your e-shop bot!")

@dp.message_handler(commands=['products'])
async def show_products(message: types.Message):
    # Your existing show_products functionality
    await message.answer("Here are the products available in our e-shop: [Product 1, Product 2, Product 3]")

@dp.message_handler(commands=['cart'])
async def show_cart(message: types.Message):
    # Your existing show_cart functionality
    await message.answer("Your shopping cart is empty.")

@dp.message_handler(commands=['order'])
async def place_order(message: types.Message):
    # Your existing place_order functionality
    await message.answer("Your order has been placed successfully!")

@dp.message_handler(commands=['menu'])
async def show_menu(message: types.Message):
    # Your existing show_menu functionality
    await message.answer("Menu of Commands:\n" + commands_list)

@dp.message_handler(commands=['links'])
async def show_links(message: types.Message):
    links_list = "Links to our e-shop:\n" \
                 "1. [Link to Product 1](http://your-eshop.com/product1)\n" \
                 "2. [Link to Product 2](http://your-eshop.com/product2)\n" \
                 "3. [Link to Product 3](http://your-eshop.com/product3)"
    await message.answer(links_list)

@dp.message_handler(commands=['search'])
async def search_products(message: types.Message):
    keyword = message.get_args()
    search_results = [product["name"] for product in products_db.values() if keyword.lower() in product["name"].lower()]
    if search_results:
        result_text = "Search results:\n" + "\n".join(search_results)
    else:
        result_text = "No products found matching the search keyword."

    await message.answer(result_text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)