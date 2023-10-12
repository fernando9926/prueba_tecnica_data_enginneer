CREATE VIEW monto_total_por_dia AS
SELECT
    c.company_name,
    c.company_id,
    CAST(CONVERT(VARCHAR(10), ch.created_at, 120) AS DATE) AS transaction_date,
    SUM(ch.amount) AS total_amount
FROM
    companies c
JOIN
    charges ch ON c.company_id = ch.company_id
GROUP BY
    c.company_id,
    c.company_name,
    CAST(CONVERT(VARCHAR(10), ch.created_at, 120) AS DATE);