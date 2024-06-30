

import os

dim_folder_path = '/home/rohitgupta/PycharmProjects/DSARevision/extraTest/dim_folder/'

schema_folder_path = '/home/rohitgupta/PycharmProjects/DSARevision/extraTest/schema_folder/'
# match file with schema:


def dim_file_with_schema(dim_folder_path, schema_folder_path):
    file_schema_dict = dict()
    for file in os.listdir(dim_folder_path):
        for schema in os.listdir(schema_folder_path):
            if file.split(".")[0] == schema.split(".")[0]:
                file_schema_dict[file] = schema
    return file_schema_dict


files_to_load = dim_file_with_schema(dim_folder_path=dim_folder_path,schema_folder_path=schema_folder_path)

print(files_to_load)