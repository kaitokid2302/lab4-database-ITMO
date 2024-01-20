CREATE TABLE IF NOT EXISTS dish(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER NOT NULL CHECK(price > 0 AND price <= 100),
    description TEXT NOT NULL,
    time_to_do INTERVAL NOT NULL,
    CONSTRAINT time_To_Do_Check CHECK (time_to_do > INTERVAL '5 minutes' AND time_to_do <= INTERVAL '2 hours')
);

CREATE TABLE IF NOT EXISTS employee(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    salary INTEGER NOT NULL CHECK(salary > 0 AND salary <= 2000),
    status BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS ingredient(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS inventory(
    ingredient_id INTEGER REFERENCES ingredient(id),
    quantity INTEGER NOT NULL CHECK(quantity > 0)
);

CREATE TABLE IF NOT EXISTS expense(
    id SERIAL PRIMARY KEY,
    price INTEGER NOT NULL,
    _time TIMESTAMP NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS supply(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    wait_time INTERVAL NOT NULL,
    address TEXT NOT NULL,
    -- >= 5 minutes
    CONSTRAINT wait_Time_Check CHECK (wait_time > INTERVAL '5 minutes')
);

CREATE TABLE IF NOT EXISTS customer(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE,
    address TEXT NOT NULL,
    -- > 5 minutes
    wait_time INTERVAL NOT NULL CHECK (wait_time > INTERVAL '5 minutes')
);

CREATE TABLE IF NOT EXISTS _order(
    id SERIAL PRIMARY KEY,
    time_delivery TIMESTAMP NOT NULL,
    time_order TIMESTAMP NOT NULL,
    status BOOLEAN NOT NULL,
    interest INTEGER NOT NULL,
    --- customer_id references and not null
    customer_id INTEGER REFERENCES customer(id) NOT NULL,
    -- constraint time_order <= current_timestamp
    CONSTRAINT time_Order_Check CHECK (time_order <= CURRENT_TIMESTAMP)
);

CREATE TABLE IF NOT EXISTS work(
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employee(id) NOT NULL,
    time_end TIMESTAMP NOT NULL,
    time_start TIMESTAMP NOT NULL,
    order_id INTEGER REFERENCES _order(id) NOT NULL,
    dish_id INTEGER REFERENCES dish(id) NOT NULL,
    -- constraint time_start <= current_timestamp and time_start <= time_end
    CONSTRAINT time_Start_Check CHECK (time_start <= CURRENT_TIMESTAMP AND time_start <= time_end)
);

-- association tables
CREATE TABLE IF NOT EXISTS dish_ingredient(
    id SERIAL PRIMARY KEY,
    dish_id INTEGER REFERENCES dish(id) NOT NULL,
    ingredient_id INTEGER REFERENCES ingredient(id) NOT NULL,
    -- quantity > 0 <= 5
    quantity INTEGER NOT NULL CHECK (quantity > 0 AND quantity <= 5)
);

CREATE TABLE expense_list(
    id SERIAL PRIMARY KEY,
    expense_id INTEGER REFERENCES expense(id) NOT NULL,
    ingredient_id INTEGER REFERENCES ingredient(id) NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    price INTEGER NOT NULL CHECK (price > 0)
);

CREATE TABLE IF NOT EXISTS order_dish(
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES _order(id) NOT NULL,
    dish_id INTEGER REFERENCES dish(id) NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0)
);

CREATE TABLE IF NOT EXISTS supply_ingredient(
    id SERIAL PRIMARY KEY,
    supply_id INTEGER REFERENCES supply(id) NOT NULL,
    ingredient_id INTEGER REFERENCES ingredient(id) NOT NULL,
    -- price > 0 <= 90
    price INTEGER NOT NULL CHECK (price > 0 AND price <= 90)
);

CREATE TABLE IF NOT EXISTS salary_employee(
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employee(id) NOT NULL,
    -- <= current date
    _date DATE NOT NULL CHECK (_date <= CURRENT_DATE)
);