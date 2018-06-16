import boto3

class sqs_queue:

    def __init_queue_client(self, region_name, access_key, secret_key):
          """Initiate a SQS.Client object"""
          sqs_client = boto3.client('sqs',
                                    region_name=region_name,
                                    aws_access_key_id=access_key,
                                    aws_secret_access_key=secret_key)
          return sqs_client

    def read_message_from_queue(self,sqs_client,queue_url,wait_time):
        """Read messages from SQS Queue"""
        try:
            # receive_message allows only ten messages to be retrieved per api call.
            messages = sqs_client.receive_message(QueueUrl=queue_url,
                                                  MaxNumberOfMessages=10,
                                                  WaitTimeSeconds=wait_time)

        except Exception as e:
            raise Exception('SQS receive operation error %s' % e)
        # If no messages are present in the queue then the Messages key in
        # messages object will not be present
        messages = messages.get('Messages')
        message_ids = []
        if messages is not None:
            for msg in messages:
                # message_ids are used for deleting the messages from the sqs queue
                message_ids.append({'Id': msg['MessageId'],
                                    'ReceiptHandle': msg['ReceiptHandle']})
        return messages, message_ids

    def delete_message_from_queue(self,sqs_client,message_ids,queue_url):
        """Delete messages from the SQS Queue"""
        # delete_message_batch allows only ten messages to be deleted for a api call
        delete_msg_list = message_ids[0:10]
        sqs_client.delete_message_batch(QueueUrl=queue_url,
                                        Entries=delete_msg_list)
