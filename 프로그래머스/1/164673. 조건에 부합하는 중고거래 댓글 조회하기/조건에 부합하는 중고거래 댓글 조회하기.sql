-- 코드를 입력하세요
SELECT
    a.TITLE, a.BOARD_ID, b.REPLY_ID, b.WRITER_ID, b.CONTENTS, DATE_FORMAT(b.created_date, '%Y-%m-%d') CREATED_DATE
FROM
    used_goods_board a
JOIN
    used_goods_reply b
USING
    (board_id)
WHERE
    a.created_date like "2022-10%"
ORDER BY
    b.created_date, a.title;