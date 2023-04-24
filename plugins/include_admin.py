from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

class IncludeAdminPlugin(BasePlugin):
    config_scheme = (
        ('admin_dir', config_options.Type(str, default='admin')),
    )

    def on_post_build(self, config):
        import shutil

        admin_dir = self.config['admin_dir']
        shutil.copytree(admin_dir, config['site_dir'] + '/' + admin_dir)
