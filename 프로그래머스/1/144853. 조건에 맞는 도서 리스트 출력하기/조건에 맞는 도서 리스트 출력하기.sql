-- 코드를 입력하세요
SELECT 
    book_id, DATE_FORMAT(published_date, '%Y-%m-%d') published_date
FROM
    book
WHERE
    published_date Like "2021%"
AND
    category = "인문"
ORDER BY
    published_date;