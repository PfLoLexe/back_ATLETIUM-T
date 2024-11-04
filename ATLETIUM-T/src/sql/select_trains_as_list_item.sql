SELECT
    train_main.id as train_id,
    train_main.name as train_name,
    train_main.start_time as train_start_time,
    train_main.end_time as train_end_time,
    place.name as train_place,
    train_main.train_type_id as train_type
FROM train_main, place
WHERE
    train_main.week_day_number={week_day_number} AND
    train_main.place_id=place.id;
