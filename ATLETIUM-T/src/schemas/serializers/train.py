import datetime

class TrainListItemSerializer:
    train_id: str
    train_label: str
    train_start_time: datetime.time
    train_end_time: datetime.time
    train_place: str
    train_type: int

    def __init__(self,
                 train_id: str,
                 train_label: str,
                 train_start_time: datetime.time,
                 train_end_time: datetime.time,
                 train_place: str,
                 train_type: int
                 ):
        self.train_id = train_id
        self.train_label = train_label
        self.train_start_time = train_start_time
        self.train_end_time = train_end_time
        self.train_place = train_place
        self.train_type = train_type