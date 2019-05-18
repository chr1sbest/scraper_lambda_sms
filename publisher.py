import boto3
import os
import logging
import datetime

## Publisher
class Publisher:
    def publish(name, output):
        return


## Publisher that writes to an SNS Topic
class SNS_Publisher(Publisher):
    rate_limit = 1 * time.hour

    def __init__(keystore):
        sns_env = os.environ['SNS_TOPIC']
        self.sns_topic = boto3.resource('sns').Topic(sns_env)
        self.keystore = keystore

    def publish(name, output)
        if __should_rate_limit(name):
            return
        message = self.__format_output(output, name)
        self.sns_topic.publish(Message=message)
        self.keystore.set(name, datetime.datetime.now()) ## TODO
        return

    def __format_output(output, name):
        return "testing"

    # Don't want to publish more than once per hour
    def __should_rate_limit(name):
        last = self.keystore.get(name)
        now = datetime.datetime.now()
        if now - last < self.rate_limit:
            return True
        return False


## Publisher that writes to CloudWatch logs
class Logger(Publisher):
    def __init__():
        self.logger = logging.getLogger()
        self.message_length = 20
        logger.setLevel(logging.INFO)

    def publish(name, output)
        logger.info("%s: %s".format(name, output[:self.message_length]))
        return