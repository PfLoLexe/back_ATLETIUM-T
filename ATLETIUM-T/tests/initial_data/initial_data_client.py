from uuid import UUID

from src.models.client import Client

def get_client_items():
    client_items = [
        Client(
            firstname='Александр',
            lastname='Александров',
            middle_name='Александрович',
            phone_number='+7idi45',
            age=22,
            parent_phone_number=None,
            is_parent=False,
            id=UUID("6f793564-ce9d-417e-b5df-6324eca497d0"),
            parent_firstname=None,
            parent_lastname=None,
            parent_middle_name=None
        ),
        Client(
            firstname='Анастасия',
            lastname='Анастасьевна',
            middle_name='Александровна',
            phone_number='+79995556545',
            age=34,
            parent_phone_number=None,
            is_parent=True,
            id=UUID("82f2d1f9-3681-4d72-b3cf-4589a62d4631"),
            parent_firstname=None,
            parent_lastname=None,
            parent_middle_name=None
        ),
        Client(
            firstname='Евгений',
            lastname='Евгеньев',
            middle_name='Евгеньевич',
            phone_number='+78885554445',
            age=17,
            parent_phone_number='+79995556545',
            is_parent=False,
            id=UUID("26e49df1-ed81-48de-9ed6-604a32b5f4cf"),
            parent_firstname='Анатолий',
            parent_lastname='Анкиражев',
            parent_middle_name=None
        ),
        Client(
            firstname='Яна',
            lastname='Дождева',
            middle_name='Романовна',
            phone_number='+76665559945',
            age=17,
            parent_phone_number='+79995556545',
            is_parent=False,
            id=UUID("91b6a9fa-b306-4b81-9006-203cc787518f"),
            parent_firstname='Антонина',
            parent_lastname='Павлова',
            parent_middle_name='Анатольевна'
        ),
        Client(
            firstname='Максимильян',
            lastname='Моррель',
            middle_name='Ишакович',
            phone_number='+74445557645',
            age=39,
            parent_phone_number=None,
            is_parent=False,
            id=UUID("6f75c0bc-7ae1-46c3-b0f8-1589fc11d5cf"),
            parent_firstname=None,
            parent_lastname=None,
            parent_middle_name=None
        )
    ]
    return client_items