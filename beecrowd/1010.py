code_product_1, number_of_unit_product_1, cost_per_unit_product_1 = map(
    float, input("Insira 3 numeros:").split(" ")
)
code_product_2, number_of_unit_product_2, cost_per_unit_product_2 = map(
    float, input("Insira mais 3 numeros:").split(" ")
)

total_cost = (number_of_unit_product_1 * cost_per_unit_product_1) + (
    number_of_unit_product_2 * cost_per_unit_product_2
)

print(f"VALOR A PAGAR: R$ {total_cost:.2f}")
