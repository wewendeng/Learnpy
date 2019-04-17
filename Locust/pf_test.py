from locust import HttpLocust, TaskSet, task
import json

'''
locust 单接口压测脚本  可以根据get\post\put等请求切换
'''

class MyTaskSet(TaskSet):

    @task(2)
    def query_user_info(self):
        headers = {"Content-Type":"application/json"}
        params = {'eid':1}
        with self.client.get('/', headers=headers, catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed!")
            else:
                response.success()

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000

