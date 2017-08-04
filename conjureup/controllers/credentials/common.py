from conjureup import controllers, juju
from conjureup.app_config import app


class BaseCredentialsController:
    def __init__(self):
        creds = juju.get_credentials().get(app.provider.cloud, {})
        creds.pop('default-region', None)

        self.default_credential = creds.pop('default-credential', None)
        self.credentials = sorted(creds.keys())

        if len(self.credentials) == 1:
            self.default_credential = self.credentials[0]

        self.was_picker = False

    def finish(self):
        controllers.use('regions').render()
