import db_operations


def main():
    # db_operations.delete_table()
    # db_operations.create_visitor_table()
    # response = db_operations.initialize_count("count")
    # response = db_operations.get_count("count",)
    response = db_operations.update_count("count",)
    print(response)


    #response = db_operations.initialize_count("count")
    #response = db_operations.update_count("count",)
    #response = db_operations.initialize_count("count")

    

    # db_operations.update_count("count",)
    # response = db_operations.get_count("count",)

    # print(response)

    
if __name__ == '__main__': 
    main()