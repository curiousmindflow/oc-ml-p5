/* Retrieve dataset: Id, Title, Tags */
SELECT Id
FROM posts
WHERE Id < 500000
    and Title IS NOT NULL
    and Tags IS NOT NULL

    /* Retrieve dataset: Body */
SELECT Body
FROM posts as p
    JOIN (
        SELECT Id
        FROM posts
        WHERE Id < 500000
            and Title IS NOT NULL
            and Tags IS NOT NULL
    ) as sub ON p.Id = sub.Id