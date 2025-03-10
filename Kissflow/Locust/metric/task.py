from locust import task

from metric import MetricReport
from metric.mock import load_mock


class TaskMetric(MetricReport):

    @task()
    def step(self):
        self._request.get(self._metric_url('01'), name='Step')

    @task()
    def step_breakdown(self):
        step_preference = load_mock(file_name='step')
        self._request.post(self._metric_url('01'), json=step_preference, name='Step (GroupBy)')

    @task()
    def state(self):
        self._request.get(self._metric_url('02'), name='State')

    @task()
    def state_breakdown(self):
        state_preference = load_mock(file_name='state')
        self._request.post(self._metric_url('01'), json=state_preference, name='State (GroupBy)')
