from sqlalchemy import text
from sqlmodel import Session

from src.models.user import User
from tests.initial_data.initial_data_client import get_client_items
from tests.initial_data.initial_data_dialogue import get_dialogue_items
from tests.initial_data.initial_data_message import get_message_items
from tests.initial_data.initial_data_pincode import get_pincode_items
from tests.initial_data.initial_data_place import get_place_items
from tests.initial_data.initial_data_train_main import get_train_main_items
from tests.initial_data.initial_data_train_main_to_client_link import get_train_main_to_client_link_items
from tests.initial_data.initial_data_train_specific import get_train_specific_items
from tests.initial_data.initial_data_train_type import get_train_type_items
from tests.initial_data.initial_data_user import get_user_items


def initial_data(session: Session):
    session.add_all(get_client_items())
    session.add_all(get_dialogue_items())
    session.add_all(get_message_items())
    session.add_all(get_pincode_items())
    session.add_all(get_place_items())
    session.add_all(get_train_main_items())
    session.add_all(get_train_main_to_client_link_items())
    session.add_all(get_train_specific_items())
    session.add_all(get_train_type_items())
    session.add_all(get_user_items())
    session.commit()
