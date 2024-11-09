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
		'$2b$12$uD5GmGwZt/adbsvdU/xAvuX1e2UkhqNywMJKOtdO3rZstRHcq2ALS',
		'74bbfdef-f556-4845-9afc-88292985228c',
		true
	),
	('user', 'Иванонов', 'Иван', 'Иванович', 'trainer',
		'$2b$12$uD5GmGwZt/adbsvdU/xAvuOot/.8/lSn6Wn4BtZ/PfZswzpt6zx12',
		'5c5d9856-6a9e-432d-9e5d-2d0ee07b9614',
		true
	);

INSERT INTO public.pincode(
	id,
    hashed_pincode,
    user_id
)
VALUES
    (
     'a4c3d3ee-0626-4f83-9374-c9fc92b1514d',
     '$2b$12$NpA38wo6r6O/6xlxv0pLK.TOCEp4a24xQAV7FUu0krG726ZlUA51.',
     '74bbfdef-f556-4845-9afc-88292985228c'
    ),
    (
     'a851abe9-16dc-4efd-a3e2-843a57bfa0d6',
     '$2b$12$NpA38wo6r6O/6xlxv0pLK.IoBufuAI2giawjGtWtJfTxRJuqkzjqi',
     '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614'
    );

INSERT INTO place(name, id)
VALUES
    ('Pool', '66c2ae22-3efb-454a-a2f3-1ae9133a575d'),
    ('Gym', 'e21622ef-105a-4d2e-85b1-43fc8df4c90e'),
    ('Boxing hall', '5707ca28-8715-4a6a-a1e6-37bbbcaa9b0e');

INSERT INTO train_type(name, id)
VALUES
	('Group', '47d9badb-dcda-49c9-9088-9e2606992b55'),
	('Personal', '751bf1ed-6a88-4e16-8e7c-1496821c50dd');

INSERT INTO train_main(
	name,
	place_id,
	train_type_id,
	start_time,
	end_time,
	week_day_number,
    "date",
	id,
    trainer_id)
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
    trainer_id,
    id)
VALUES
    (
     3,
     'Абракадабра',
     '31.10.2024',
     true,
     '38b40437-0541-44ed-871a-f1a04fba179b',
     '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614',
     '953d1949-23ab-4364-8c70-68a09e2387c1'
    );

INSERT INTO client(
    firstname,
    lastname,
    middle_name,
    phone_number,
    age,
    parent_phone_number,
    is_parent,
    id)
VALUES
    (
     'Александр',
     'Александров',
     'Александрович',
     '+7idinahoi45',
     NULL,
     NULL,
     FALSE,
     '6f793564-ce9d-417e-b5df-6324eca497d0'
    ),
    (
     'Анастасия',
     'Анастасьевна',
     'Александровна',
     '+79995556545',
     NULL,
     NULL,
     TRUE,
     '82f2d1f9-3681-4d72-b3cf-4589a62d4631'
    ),
    (
     'Евгений',
     'Евгеньев',
     'Евгеньевич',
     '+78885554445',
     17,
     '+79995556545',
     FALSE,
     '26e49df1-ed81-48de-9ed6-604a32b5f4cf'
    ),
    (
     'Яна',
     'Дождева',
     'Романовна',
     '+76665559945',
     17,
     NULL,
     FALSE,
     '91b6a9fa-b306-4b81-9006-203cc787518f'
    ),
    (
     'Максимильян',
     'Моррель',
     'Ишакович',
     '+74445557645',
     39,
     NULL,
     FALSE,
     '6f75c0bc-7ae1-46c3-b0f8-1589fc11d5cf'
    );

INSERT INTO dialogue(
	first_user_id,
    second_user_id,
    id)
VALUES
    (
     '74bbfdef-f556-4845-9afc-88292985228c',
     '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614',
     '5f092ba3-70b4-409a-a153-a698a3bd41ed'
    );

INSERT INTO message(
	text,
    sender_user_id,
    dialogue_id,
    parent_message_id,
    id,
    send_date,
    is_read,
    read_date)
VALUES
    (
     'Hi, User!',
     '74bbfdef-f556-4845-9afc-88292985228c',
     '5f092ba3-70b4-409a-a153-a698a3bd41ed',
     NULL,
     '369f50dc-07c4-4b8c-a9c1-aabfa12de715',
     '1.11.2024 10:00:00',
     FALSE,
     NULL
    ),
    (
     'Hi, Admin',
     '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614',
     '5f092ba3-70b4-409a-a153-a698a3bd41ed',
     NULL,
     '077ddf22-2ce5-4088-bf2e-250d6f6021fc',
     '1.11.2024 10:10:00',
     FALSE,
     NULL
    ),
    (
     'How are you, Admin?',
     '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614',
     '5f092ba3-70b4-409a-a153-a698a3bd41ed',
     NULL,
     '13b2bea7-4aed-4295-a347-de799bc520cd',
     '1.11.2024 10:20:00',
     FALSE,
     NULL
    ),
    (
     'I''m fine!',
     '74bbfdef-f556-4845-9afc-88292985228c',
     '5f092ba3-70b4-409a-a153-a698a3bd41ed',
     NULL,
     '7d164d7a-066e-4f4f-a15d-917cc56eb918',
     '1.11.2024 10:30:00',
     FALSE,
     NULL
    );

INSERT INTO train_main_to_client_link(
	train_main_id,
    client_id,
    id)
VALUES
    (
     '41e5c441-16b4-4c98-a3a7-7bd32589e048',
     '6f793564-ce9d-417e-b5df-6324eca497d0',
     '659ab3e7-6eb1-49f0-916b-cc7dbbcde30d'
    );