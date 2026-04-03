import random
from faker import Faker
from datetime import datetime

fake = Faker()
Faker.seed(42) # Щоб результати були однаковими при кожному запуску

now = datetime.now()
# Кількість записів
NUM_USERS = 200
NUM_HOTELS = 20
NUM_ROOMS = 100
NUM_REQUESTS = 500
NUM_ACTIVITIES = 1500
NUM_ORDERS = 150

sql_output = "insert_data.sql"

with open(sql_output, "w", encoding="utf-8") as f:
    f.write("USE wwt_test_db;\n\n")

    # 1. USERS
    for i in range(1, NUM_USERS + 1):
        email = fake.unique.email()
        reg_date = fake.date_between(start_date='-1y', end_date='today')
        country = fake.country().replace("'", "")
        device = random.choice(['iOS', 'Android', 'Web'])
        source = random.choice(['Google', 'Facebook', 'Instagram', 'Referral', 'Direct'])
        f.write(f"INSERT INTO users (user_id, email, registration_date, country, device_type, referral_source) VALUES ({i}, '{email}', '{reg_date}', '{country}', '{device}', '{source}');\n")

    # 2. HOTEL
        # 2. HOTEL
        for i in range(1, NUM_HOTELS + 1):
            country = fake.country().replace("'", "")
            city = fake.city().replace("'", "")
            street = fake.street_name().replace("'", "")
            f.write(
                f"INSERT INTO hotel (hotel_id, country, city, street, house, email, phone_number, rating) VALUES ({i}, '{country}', '{city}', '{street}', {random.randint(1, 200)}, '{fake.company_email()}', '{fake.phone_number()}', {round(random.uniform(3.0, 5.0), 1)});\n")
    for i in range(1, NUM_ROOMS + 1):
        h_id = random.randint(1, NUM_HOTELS)
        f.write(f"INSERT INTO room (room_id, hotel_id, beds, animals_places, price_day, is_extra_beds, size) VALUES ({i}, {h_id}, {random.randint(1, 4)}, {random.randint(0, 2)}, {random.uniform(50, 500):.2f}, {random.choice([True, False])}, {random.uniform(15, 60):.2f});\n")

    # 4. REQUESTS
        # 4. REQUESTS
        for i in range(1, NUM_REQUESTS + 1):
            u_id = random.randint(1, NUM_USERS)
            # Використовуємо об'єкт now замість рядка 'today'
            request_date = fake.date_time_between(start_date='-6m', end_date=now)
            f.write(
                f"INSERT INTO requests (request_id, user_id, people_amount, animals_amount, kids, highest_price, request_date, is_ai_used) VALUES ({i}, {u_id}, {random.randint(1, 5)}, {random.randint(0, 2)}, {random.randint(0, 3)}, {random.randint(200, 2000)}, '{request_date}', {random.choice([True, False])});\n")

    # 5. ACTIVITIES (Likes)
    for i in range(1, NUM_ACTIVITIES + 1):
        req_id = random.randint(1, NUM_REQUESTS)
        rm_id = random.randint(1, NUM_ROOMS)
        f.write(f"INSERT INTO activities (activity_id, request_id, room_id, is_liked) VALUES ({i}, {req_id}, {rm_id}, {random.choice([True, False])});\n")

    # 6. ORDERS (Final Bookings)
    for i in range(1, NUM_ORDERS + 1):
        req_id = random.randint(1, NUM_REQUESTS)
        rm_id = random.randint(1, NUM_ROOMS)
        # Аналогічно виправляємо тут
        order_date = fake.date_time_between(start_date='-5m', end_date=now)
        f.write(
            f"INSERT INTO orders (order_id, request_id, room_id, total_price, order_date) VALUES ({i}, {req_id}, {rm_id}, {random.uniform(200, 3000):.2f}, '{order_date}');\n")

print(f"Файл {sql_output} згенеровано!")