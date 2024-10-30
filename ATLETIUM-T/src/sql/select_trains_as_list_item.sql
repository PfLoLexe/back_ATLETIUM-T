SELECT
    train.id as train_id,
    train.label as train_label,
    train.start_time as train_start_time,
    train.end_time as train_end_time,
    place.label as train_place,
    train.train_type_id as train_type
FROM train, place
WHERE
    train.week_day_number={week_day_number} AND
    train.place_id=place.id;
