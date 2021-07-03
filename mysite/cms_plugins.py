from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from .models import *

@plugin_pool.register_plugin
class FeatureServiceCardPlugin(CMSPluginBase):
    model = FeatureServiceCardPluginModel
    render_template = "feature-service-card.html"
    cache = False

@plugin_pool.register_plugin
class SocialIconPlugin(CMSPluginBase):
    model = SocialIconsPluginModel
    render_template = "plugin-social-icon.html"