-- 코드를 입력하세요
SELECT 
    a.rest_id, 
    a.rest_name, 
    a.food_type, 
    a.favorites, 
    a.address, 
    ROUND(AVG(b.review_score), 2) score
FROM
    rest_info a
JOIN
    rest_review b
USING
    (rest_id)
WHERE
    a.address like '서울%'
GROUP BY
    a.rest_id
ORDER BY
    score DESC, a.favorites DESC