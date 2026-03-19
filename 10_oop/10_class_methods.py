class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
    @classmethod
    def from_dict(cls,order_data):
        return cls(order_data["tea_type"],
                   order_data["sweetness"],
                   order_data["size"])
    
    @classmethod
    def from_string(cls,order_string):
        order_data = order_string.split(",")
        return cls(order_data[0],order_data[1],order_data[2])
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["small", "medium", "large"]

print(ChaiUtils.is_valid_size("small")) 

order1 = ChaiOrder.from_dict({"tea_type":"Masala","sweetness":"low","size":200})
print(order1.tea_type)
print(order1.sweetness)
print(order1.size)

order2 = ChaiOrder.from_string("Masala,low,200")
print(order2.tea_type)
print(order2.sweetness)
print(order2.size)

print(order1.__dict__)
    