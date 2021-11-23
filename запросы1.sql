UPDATE The_User SET reg_data = SUBSTR(reg_data, 1, 10)
UPDATE The_User SET date_of_birth = SUBSTR(date_of_birth, 1, 10)
SELECT username, MAX(reg_data) FROM The_User
SELECT DISTINCT(substr(date_of_birth, 1, 4)) FROM The_User
SELECT count(prod_id) as 'total_items' FROM Product
SELECT avg(substr(CURRENT_DATE, 0, 5) - substr(date_of_birth, 0, 5)) as 'Ср возраст зарегистрировавшихся покупателей' FROM The_User WHERE (substr(CURRENT_DATE, 6, 2) - substr(reg_data, 6, 2) <= 2)