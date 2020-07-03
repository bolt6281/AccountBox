# import os
# import json

# cwd = os.getcwd()

# #############################################
# # load config file

# # check if there is config file | if not, make new one
# if not os.path.exists(cwd+"\\config.json"):
#     with open("config.json", "w") as json_file:
#         default_loc = cwd+"\\account_data.json"
#         json.dump({"AccountFileLoc": {"LOC": default_loc}}, json_file)
#     file_loc = default_loc
# else:
#     # load config
#     with open(cwd+'\\config.json', 'r') as json_file:
#         config = json.loads(json_file.read())
#     file_loc = config['AccountFileLoc']['LOC']

# #############################################
# # load account data

# # check if there is account file
# with open(file_loc, "r") as json_file:
#     account_data = json.loads(json_file.read())

print(file_loc)