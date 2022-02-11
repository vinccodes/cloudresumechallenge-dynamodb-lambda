import db_operations


def main():
    
    response = db_operations.delete_table()
    print(response)

    #response = db_operations.initialize_count("count")
    #response = db_operations.update_count("count",)
    #response = db_operations.initialize_count("count")

    

    # db_operations.update_count("count",)
    # response = db_operations.get_count("count",)

    # print(response)

    
if __name__ == '__main__': 
    main()