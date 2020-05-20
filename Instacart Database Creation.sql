# Untar file using tar zxvf instacart_online_grocery_shopping_2017_05_01.tar.gz
# Create database, tables, foreign keys and import data.
create database instacart;
use instacart;
# Create Orders table
create table orders (order_id bigint, user_id int, order_number int, order_dow int, order_hour int, day_since_last_order int);
# Load data
LOAD DATA LOCAL INFILE '/Users/wright/Downloads/instacart_2017_05_01/orders.csv' INTO TABLE orders FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
# Create Product table
create table products (product_id int, product_name VARCHAR(255), aisle_id int NOT NULL, foreign key (aisle_id) references aisles(aisle_id), department_id int NOT NULL, foreign key (department_id) references departments(department_id));
# Load data
LOAD DATA LOCAL INFILE '/Users/wrigh/Downloads/instacart_2017_05_01/products.csv' INTO TABLE products FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
# Create Product table
create table order_products_prior (order_id bigint NOT NULL, foreign key (order_id) references orders(order_id), product_id bigint NOT NULL, foreign key (product_id) references products(product_id), add_to_cart int, reordered int);
# Create Product table
LOAD DATA LOCAL INFILE '/Users/wrigh/Downloads/instacart_2017_05_01/order_products_prior.csv' INTO TABLE order_products_prior FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
# Create Product table
create table order_products_train (order_id bigint NOT NULL, foreign key (order_id) references orders(order_id), product_id bigint NOT NULL, foreign key (product_id) references products(product_id), add_to_cart int, reordered int);
# Create Product table
LOAD DATA LOCAL INFILE '/Users/wrigh/Downloads/instacart_2017_05_01/order_products_train.csv' INTO TABLE order_products_train FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
# Create Departments table
create table departments (department_id int, department VARCHAR(255));
# Load data
LOAD DATA LOCAL INFILE '/Users/wrigh/Downloads/instacart_2017_05_01/departments.csv' INTO TABLE departments FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
# Create aisles table
create table aisles (aisle_id int, aisle VARCHAR(255));
# Load Data
LOAD DATA LOCAL INFILE '/Users/wrigh/Downloads/instacart_2017_05_01/aisles.csv' INTO TABLE aisles FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
# View all tables
show tables;
# Test Database
select * from aisles;         
# Export dataset using mysqldump -u root -p instacart > instacart.sql
