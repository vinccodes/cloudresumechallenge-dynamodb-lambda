import unittest
from moto import mock_dynamodb
from src import db_operations


class DynamoDBTestCase(unittest.TestCase):
    
    @mock_dynamodb
    def test_delete_table(self):
        result = db_operations.delete_table()
        self.assertEqual(result["message"], "deleted table")

    @mock_dynamodb
    def test_create_table(self):
        result = db_operations.create_visitor_table()
        self.assertEqual(result.table_name, 'Visitors')


    @mock_dynamodb
    def test_delete_table(self):
        result = db_operations.delete_table()
        self.assertEqual(result["message"], "deleted table")

    @mock_dynamodb
    def test_initialize_count(self):
        result = db_operations.initialize_count("count")
        self.assertEqual(result["ResponseMetadata"]["HTTPStatusCode"], 200)

    @mock_dynamodb
    def test_get_count(self):
        result = db_operations.get_count("count",)
        self.assertEqual(result["visitor_total"], 0)


    @mock_dynamodb
    def test_update_count(self):
        result = db_operations.update_count("count",)
        self.assertEqual(result['Attributes']["visitor_total"], 1)


if __name__== '__main__':
    unittest.main()