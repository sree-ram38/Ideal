class laptop:
    price=0
    processor=""
    ram=""

hp = laptop()
dell = laptop()
lenovo = laptop()

hp.price=50000
hp.processor="intel"
hp.ram="12GB"

dell.price=30000
dell.processor="pentium"
dell.ram="8GB"

lenovo.price=60000
lenovo.processor="snapdragon quad"
lenovo.ram="16GB"

print("The price of hp is ",hp.price)