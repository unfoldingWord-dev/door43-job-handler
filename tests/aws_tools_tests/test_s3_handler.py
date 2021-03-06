import os
import shutil
import tempfile
from unittest import TestCase

from botocore.exceptions import ClientError
from moto import mock_s3

from aws_tools.s3_handler import S3Handler


# Test disabled Oct 2020 coz not working -- see https://stackoverflow.com/questions/61953806/moto-seems-to-stop-mocking-after-upgrading-boto3
# @mock_s3
# class S3HandlerTests(TestCase):
#     MOCK_BUCKET_NAME = 'test-bucket'

#     resources_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources')

#     def setUp(self):
#         """Runs before each test."""
#         self.temp_dir = tempfile.mkdtemp(prefix='Door43_test_s3Handler_')
#         self.handler = S3Handler(bucket_name=self.MOCK_BUCKET_NAME)
#         self.handler_create_bucket()

#     # Stuff removed from S3 handlers
#     def handler_create_bucket(self):
#         self.handler.resource.create_bucket(Bucket=self.MOCK_BUCKET_NAME, CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
#     def handler_put_contents(self, key, body):
#         self.handler.get_object(key).put(Body=body)

#     def tearDown(self):
#         shutil.rmtree(self.temp_dir, ignore_errors=True)

#     def test_setup_resources(self):
#         my_handler = S3Handler(aws_access_key_id='access_key', aws_secret_access_key='secret_key',
#                                aws_region_name='us-west-2')
#         self.assertEqual(my_handler.aws_access_key_id, 'access_key')
#         self.assertEqual(my_handler.aws_secret_access_key, 'secret_key')
#         self.assertEqual(my_handler.aws_region_name, 'us-west-2')

#     # def test_download_dir(self):
#     #     key = 'from_dir/from_subdir/from_file.txt'
#     #     self.handler_put_contents(key, 'this exists')
#     #     self.handler_download_dir(key.split('/')[0], self.temp_dir)
#     #     self.assertTrue(os.path.isfile(os.path.join(self.temp_dir, key)))

#     def test_upload_file(self):
#         self.handler.upload_file(os.path.join(self.resources_dir, 'test_file.zip'), 'test/me/out.zip')

#     # def test_key_exists(self):
#     #     self.handler_put_contents('exists.json', 'this exists')
#     #     self.assertTrue(self.handler.key_exists('exists.json'))

#     # def test_key_does_not_exists(self):
#     #     self.assertFalse(self.handler.key_exists(key='does_not_exists.json', bucket_name=self.MOCK_BUCKET_NAME))

#     def test_copy(self):
#         # test good copy
#         self.handler_put_contents('from/file.txt', 'this exists')
#         ret = self.handler.copy(from_key="from/file.txt", to_key="to/file.txt", from_bucket=self.MOCK_BUCKET_NAME)
#         self.assertTrue(ret)
#         contents = self.handler.get_file_contents('from/file.txt')
#         self.assertEqual(contents.decode(), 'this exists')

#         # Test bad copy
#         ret = self.handler.copy(from_key="from/not_exist.txt")
#         self.assertFalse(ret)
#         self.assertRaises(Exception, self.handler.copy, from_key="from/not_exist.txt", catch_exception=False)

#     # def test_replace(self):
#     #     # Test replace
#     #     self.handler_put_contents('path/file.txt', 'this exists')
#     #     ret = self.handler.replace(key="path/file.txt")
#     #     self.assertTrue(ret)
#     #     contents = self.handler.get_file_contents('path/file.txt')
#     #     self.assertEqual(contents.decode(), 'this exists')
#     #     # Do not catch exception
#     #     ret = self.handler.replace(key="path/file.txt", catch_exception=False)
#     #     self.assertTrue(ret)

#     def test_get_file_contents_good(self):
#         self.handler_put_contents('exists.json', 'this exists')
#         self.assertEqual('this exists', self.handler.get_file_contents('exists.json').decode())

#     def test_get_file_contents_bad(self):
#         ret = self.handler.get_file_contents("from/from_bad.txt")
#         self.assertFalse(ret)
#         self.assertRaises(Exception, self.handler.get_file_contents, key="from_bad_dir/from_bad_file",
#                           catch_exception=False)

#     # def test_create_bucket(self):
#     #     handler = S3Handler()
#     #     bucket_name = "my_test_bucket"
#     #     handler.create_bucket(bucket_name)
#     #     try:
#     #         handler.resource.meta.client.head_bucket(Bucket=bucket_name)
#     #     except ClientError:
#     #         self.fail("Was not able to create bucket!")

#     # def test_put_contents(self):
#     #     bucket_name = "my_test_bucket"
#     #     handler = S3Handler(bucket_name)
#     #     handler.create_bucket()
#     #     key = "contents/goes/here"
#     #     contents = "This is a test"
#     #     handler_put_contents(key, contents)
#     #     file_contents = handler.get_file_contents(key)
#     #     self.assertEqual(file_contents.decode(), contents)
