products=["P234HF22222 r1011",
"P234HF22223 r1112",
"P234HF22225 r1114",
"P111TG11115 r1015",
"P111TG11116 r1216",
"P331LS00110 r1017",
"P331LS00120 r1318",
"P331LS00130 r1019"]

purchases=["P234HF22223 r1112",
"P111TG11115 r1015",
"P111TG11115 r1216",
"P234HF22222 r1011",
"P331LS00110 r1014",
"P331LS00120 r1318",
"P331LS00130 r1019",
"P234HF22225 r1114",
"P234HF22223 r1114"
]

for i in range(len(products)):
    products[i]=products[i].split(" ")

for i in range(len(purchases)):
    purchases[i] = purchases[i].split(" ")

print(products)
print(purchases)

print("Suspicious transactions list\n")
for i in range(len(products)):
    product=products[i][0]
    reseller=products[i][1]
    sus_transaction=list(filter(lambda x:x[0]==product and x[1]!=reseller,purchases))
    sus_transaction=list(map(lambda x: x[1],sus_transaction))
    if len(sus_transaction) != 0:
        print(f"Product code: {product}")
        print(f"Official dealer: {reseller}")
        print("Non official dealers: ",end=" ")
        for element in sus_transaction:
            print(element,end=" ")
        print('\n')
