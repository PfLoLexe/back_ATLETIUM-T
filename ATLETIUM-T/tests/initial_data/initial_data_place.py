from uuid import UUID

from src.models.place import PLace

def get_place_items():
    place_items = [
        PLace(name='Pool', id=UUID("66c2ae22-3efb-454a-a2f3-1ae9133a575d")),
        PLace(name='Gym', id=UUID("e21622ef-105a-4d2e-85b1-43fc8df4c90e")),
        PLace(name='Boxing hall', id=UUID("5707ca28-8715-4a6a-a1e6-37bbbcaa9b0e"))
    ]
    return place_items