INSERT INTO "user"(
	username,
	firstname,
	lastname,
	middle_name,
	role,
	hashed_password,
	id,
	is_active
)
VALUES
	('admin', NULL, NULL, NULL, 'admin',
		'$2b$12$uD5GmGwZt/adbsvdU/xAvueWFLpP0eViBkg06EPc/YKwY3e9KI/NS',
		'74bbfdef-f556-4845-9afc-88292985228c',
		true
	),
	('user', 'Иванонов', 'Иван', 'Иванович', 'trainer',
		'$2b$12$uD5GmGwZt/adbsvdU/xAvuKN5vwsXzoXCZ9Q6.xdZqmU88cF.qAiu',
		'5c5d9856-6a9e-432d-9e5d-2d0ee07b9614',
		true
	);

INSERT INTO place(name, id)
VALUES
    ('Pool', '66c2ae22-3efb-454a-a2f3-1ae9133a575d'),
    ('Gym', 'e21622ef-105a-4d2e-85b1-43fc8df4c90e'),
    ('Boxing hall', '5707ca28-8715-4a6a-a1e6-37bbbcaa9b0e');

INSERT INTO train_type(name, id)
VALUES
	('Group', '47d9badb-dcda-49c9-9088-9e2606992b55'),
	('personal', '751bf1ed-6a88-4e16-8e7c-1496821c50dd');

INSERT INTO train_main(
	name,
	place_id,
	train_type_id,
	start_time,
	end_time,
	week_day_number,
    "date",
	id,
    trainer_user_id)
VALUES
	(
	 'Плавание 10+',
	 '66c2ae22-3efb-454a-a2f3-1ae9133a575d',
	 '47d9badb-dcda-49c9-9088-9e2606992b55',
	 '11:30:00.343', '13:00:00.343', 1, NULL,
	 '41e5c441-16b4-4c98-a3a7-7bd32589e048',
	 '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614'
    ),
	(
	 'Функциональный фитнес',
	 'e21622ef-105a-4d2e-85b1-43fc8df4c90e',
	 '47d9badb-dcda-49c9-9088-9e2606992b55',
	 '11:30:00.343', '13:00:00.343', 1, NULL,
	 'd6ab1705-4e24-4e0e-bb42-eba1def3cfd3',
	 '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614'
	 ),
	(
	 'Бокс',
	 '5707ca28-8715-4a6a-a1e6-37bbbcaa9b0e',
	 '47d9badb-dcda-49c9-9088-9e2606992b55',
	 '11:30:00.343', '13:00:00.343', 3, NULL,
	 '54626715-00a1-463e-9f64-6f5d3b160d2d',
	 '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614'
    ),
	(
	 'Фитнес',
	 'e21622ef-105a-4d2e-85b1-43fc8df4c90e',
	 '751bf1ed-6a88-4e16-8e7c-1496821c50dd',
	 '11:30:00.343', '13:00:00.343', 4, NULL,
	 '1b0f1ae3-7d52-4bc8-b26a-ae90b903cee0',
	 '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614'
	),
	(
	 'Плавание 6+',
	 '66c2ae22-3efb-454a-a2f3-1ae9133a575d',
	 '751bf1ed-6a88-4e16-8e7c-1496821c50dd',
	 '11:30:00.343', '13:00:00.343', 5, '31.10.24',
	 '38b40437-0541-44ed-871a-f1a04fba179b',
	 '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614'
    );


INSERT INTO train_specific(
	clients_amount,
    description,
    "date",
    is_over,
    train_main_id,
    id)
VALUES
    (
     3,
     'Абракадабра',
     '31.10.2024',
     true,
     '38b40437-0541-44ed-871a-f1a04fba179b',
     '953d1949-23ab-4364-8c70-68a09e2387c1'
    );