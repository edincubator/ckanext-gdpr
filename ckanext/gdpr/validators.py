import ckan.lib.navl.dictization_functions as df
from ckan.common import _

Missing = df.Missing


def gdpr_accepted(key, data, errors, context):
    value = data[key]

    if not value:
        errors[('terms_of_use',)].append(_('You must accept terms of use'))