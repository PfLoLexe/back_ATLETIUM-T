﻿DELETE FROM train_main
WHERE ID is not NULL;

DELETE FROM train_specific
WHERE ID is not NULL;

DELETE FROM train_type
WHERE ID is not NULL;

DELETE FROM place
WHERE ID is not NULL;

DELETE FROM client
WHERE ID is not NULL;

DELETE FROM "user"
WHERE ID is not NULL;

DELETE FROM dialogue
WHERE ID is not NULL;

DELETE FROM message
WHERE ID is not NULL;

DELETE FROM train_main_to_client_link
WHERE ID is not NULL;

DELETE FROM train_specific_to_client_link
WHERE ID is not NULL;