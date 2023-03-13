INSERT INTO charges (id, amount) VALUES (
    {{ .charge_id | required "charge_id is required" | type "text" | description "the id of the charge" | squote }}
    {{ .amount | required "amount is required" | type "number" | description "the amount to charge" }}
)