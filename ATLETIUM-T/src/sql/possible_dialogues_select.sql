with exist_dialogues AS (
		SELECT
			first_user_id
		FROM
			dialogue
		WHERE
			dialogue.second_user_id = '74bbfdef-f556-4845-9afc-88292985228c'
	UNION
		SELECT
			second_user_id
		FROM
			dialogue
		WHERE
			dialogue.first_user_id = '74bbfdef-f556-4845-9afc-88292985228c'
)

SELECT
	us.firstname AS recipient_user_firstname,
	us.lastname AS recipient_user_lastname,
	us.middle_name AS recipient_user_middle_name,
	us.id AS recipient_user_id
FROM
	public."user" AS us
WHERE
	us.role != 'admin' AND
	us.id NOT IN (SELECT * FROM exist_dialogues)