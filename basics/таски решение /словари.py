##====================14

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91}, 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# new_dict = {}

# for k1, v1 in dict_.items():
#     for k2, v2 in v1.items():
#         max_num = max(v1.values())
#         if max_num == v2:
#             new_dict[k1] = k2
# print(new_dict)

# res = {k1: k2 for k1, v1 in dict_.items() for k2, v2 in v1.items() if max(v1.values()) == v2}


##====================15

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {k : v2 for k,v in my_dict.items() for v2 in v.values()}
# print(dict_)

##====================28

# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}

# for k, v in dict1.items():
#     mul_ = 1
#     for v2 in v.values():
#         mul_ = mul_ * v2
#         dict2[k] = mul_
# print(dict2)