from main import Base


class MetricReport(Base):
    abstract = True

    def __init__(self, *args, **kwargs):
        super(MetricReport, self).__init__(*args, **kwargs)
        self.project_id = 'Metric_report_test_01'
        self.project_flow_id = 'Metric_report_test_01_flow'
        self.url = f'/project-report/2/{self._request.account_id}/{self.project_id}/projectflow/' \
                   f'{self.project_flow_id}/metric/Metric'

    def _metric_url(self, metric_id):
        return f'{self.url}{metric_id}'
