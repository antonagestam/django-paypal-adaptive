__author__ = 'antonagestam'

from django.dispatch import Signal

received_preapproval = Signal(providing_args=['preapproval'])
