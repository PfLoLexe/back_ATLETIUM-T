INSERT INTO "user"(
	username,
	firstname,
	lastname,
	middle_name,
	role,
	hashed_password,
	id,
    phone_number,
	is_active
)
VALUES
	('admin', 'Владимир', 'Ель', NULL, 'admin',
		'$2b$12$uD5GmGwZt/adbsvdU/xAvuX1e2UkhqNywMJKOtdO3rZstRHcq2ALS',
		'74bbfdef-f556-4845-9afc-88292985228c',
	    'gfdh',
		true
	),
	('user', 'Иванонов', 'Иван', 'Иванович', 'trainer',
		'$2b$12$uD5GmGwZt/adbsvdU/xAvuOot/.8/lSn6Wn4BtZ/PfZswzpt6zx12',
		'5c5d9856-6a9e-432d-9e5d-2d0ee07b9614',
	    'gfdh',
		true
	),
    	('user2', 'Иванонов2', 'Иван2', 'Иванович2', 'trainer',
		'$2b$12$uD5GmGwZt/adbsvdU/xAvuj6rNJA2MUfZwBeccVzPD7FPKkqSLoxy',
		'b1c40098-78ef-4af9-9cf8-6da820fdc5b4',
	    'phone_humber',
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
    ),
    (
     'c2aa8912-88f0-464f-927d-4ffc44d33892',
     '$2b$12$NpA38wo6r6O/6xlxv0pLK.IoBufuAI2giawjGtWtJfTxRJuqkzjqi',
     'b1c40098-78ef-4af9-9cf8-6da820fdc5b4'
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
    start_time,
    end_time,
    week_day_number,
    date,
    place_id,
    train_type_id,
    trainer_id,
    id
)
VALUES
	('Фитнес', '11:30:00', '13:00:00', 3, null, 'e21622ef-105a-4d2e-85b1-43fc8df4c90e', '751bf1ed-6a88-4e16-8e7c-1496821c50dd', '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614', '1b0f1ae3-7d52-4bc8-b26a-ae90b903cee0'),
    ('Фитнес', '11:30:00', '11:30:00', 1, null, 'e21622ef-105a-4d2e-85b1-43fc8df4c90e', '751bf1ed-6a88-4e16-8e7c-1496821c50dd', '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614', 'b59eaac5-2f94-4653-8b61-f3de392eaecc'),
    ('Фитнес', '11:30:00', '11:30:00', 3, null, 'e21622ef-105a-4d2e-85b1-43fc8df4c90e', '751bf1ed-6a88-4e16-8e7c-1496821c50dd', '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614', 'bd35454b-6d58-4020-93e7-6d8c1fa76f7f'),
    ('Фитнес', '11:30:00', '11:30:00', 3, null, 'e21622ef-105a-4d2e-85b1-43fc8df4c90e', '751bf1ed-6a88-4e16-8e7c-1496821c50dd', '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614', '8ccb54b8-0469-4313-830f-2528cc9c421e'),
    ('Функциональный фитнес', '14:45:00', '15:45:00', 1, null, 'e21622ef-105a-4d2e-85b1-43fc8df4c90e', '47d9badb-dcda-49c9-9088-9e2606992b55', '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614', 'd6ab1705-4e24-4e0e-bb42-eba1def3cfd3'),
    ('Плавание 6+', '10:00:00', '11:00:00', 6, '2025-04-28', '66c2ae22-3efb-454a-a2f3-1ae9133a575d', '751bf1ed-6a88-4e16-8e7c-1496821c50dd', '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614', '38b40437-0541-44ed-871a-f1a04fba179b'),
    ('Фитнес', '11:30:00', '11:30:00', 1, null, 'e21622ef-105a-4d2e-85b1-43fc8df4c90e', '751bf1ed-6a88-4e16-8e7c-1496821c50dd', '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614', '0938bd36-48ed-4e29-b352-9333a78892b5'),
    ('Фитнес', '11:30:00', '11:30:00', 6, null, 'e21622ef-105a-4d2e-85b1-43fc8df4c90e', '751bf1ed-6a88-4e16-8e7c-1496821c50dd', '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614', '950f9082-3be7-40e6-acc0-6da20127fac6'),
    ('Бокс', '16:15:00', '17:00:00', 6, null, '5707ca28-8715-4a6a-a1e6-37bbbcaa9b0e', '47d9badb-dcda-49c9-9088-9e2606992b55', '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614', '54626715-00a1-463e-9f64-6f5d3b160d2d'),
    ('Плавание 10+', '13:30:00', '14:30:00', 6, null, '66c2ae22-3efb-454a-a2f3-1ae9133a575d', '47d9badb-dcda-49c9-9088-9e2606992b55', '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614', '41e5c441-16b4-4c98-a3a7-7bd32589e048');

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
    is_parent,
    id)
VALUES
    (
     'Александр',
     'Александров',
     'Александрович',
     '+7idinahoi45',
     22,
     FALSE,
     '6f793564-ce9d-417e-b5df-6324eca497d0'
    ),
    (
     'Анастасия',
     'Анастасьевна',
     'Александровна',
     '+79995556545',
     34,
     TRUE,
     '82f2d1f9-3681-4d72-b3cf-4589a62d4631'
    ),
    (
     'Евгений',
     'Евгеньев',
     'Евгеньевич',
     '+78885554445',
     17,
     FALSE,
     '26e49df1-ed81-48de-9ed6-604a32b5f4cf'
    ),
    (
     'Яна',
     'Дождева',
     'Романовна',
     '+76665559945',
     17,
     FALSE,
     '91b6a9fa-b306-4b81-9006-203cc787518f'
    ),
    (
     'Максимильян',
     'Моррель',
     'Ишакович',
     '+74445557645',
     39,
     FALSE,
     '6f75c0bc-7ae1-46c3-b0f8-1589fc11d5cf'
    );

INSERT INTO client_parent_info(
	phone_number,
    firstname,
    lastname,
    middle_name,
    id)
VALUES
    (
     '+79999999999',
     'Акакий',
     'Акакиевич',
     'Акакьев',
     '16b92894-4b3e-4c6d-a813-04974a157187'
    ),
    (
     '+79999999999',
     'Анатолий',
     'Терентьев',
     'Ольгович',
     '530e010d-b60d-4f3a-ba0a-06c559fc9777'
    );

INSERT INTO parent_to_client_link(
    parent_id,
    client_id,
    id)
VALUES
    (
     '16b92894-4b3e-4c6d-a813-04974a157187',
     '26e49df1-ed81-48de-9ed6-604a32b5f4cf',
     'a801adb9-40d1-42cc-a953-89c15e60fc7a'
    ),
    (
     '530e010d-b60d-4f3a-ba0a-06c559fc9777',
     '91b6a9fa-b306-4b81-9006-203cc787518f',
     'd369e27a-a566-4826-956a-39ecedd62c35'
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
    recipient_user_id,
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
     '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614',
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
     '74bbfdef-f556-4845-9afc-88292985228c',
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
     '74bbfdef-f556-4845-9afc-88292985228c',
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
     '5c5d9856-6a9e-432d-9e5d-2d0ee07b9614',
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
    ('41e5c441-16b4-4c98-a3a7-7bd32589e048', '6f793564-ce9d-417e-b5df-6324eca497d0', '659ab3e7-6eb1-49f0-916b-cc7dbbcde30d'),
    ('41e5c441-16b4-4c98-a3a7-7bd32589e048', '26e49df1-ed81-48de-9ed6-604a32b5f4cf', '5b57c98a-eab7-47e4-b61f-4dad8ed53614');