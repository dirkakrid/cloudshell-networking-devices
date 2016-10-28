import threading
from cloudshell.api.cloudshell_api import CloudShellAPISession
from cloudshell.snmp.quali_snmp import QualiSnmp
from cloudshell.cli.cli import Cli
from cloudshell.cli.session_pool_manager import SessionPoolManager
from cloudshell.networking.cisco.cisco_command_modes import DefaultActions
from cloudshell.shell.core.context_utils import CONTEXT_DICT, get_resource_address, get_attribute_by_name, \
    decrypt_password_from_attribute
from cloudshell.shell.core.session.logging_session import LoggingSessionContext
from cloudshell.snmp.snmp_parameters import SNMPV2Parameters, SNMPV3Parameters


def get_cli(session_pool_size, pool_timeout=100):
    session_pool = SessionPoolManager(max_pool_size=session_pool_size, pool_timeout=pool_timeout)
    return Cli(session_pool=session_pool)

def get_logger(context):
    return LoggingSessionContext.get_logger_for_context(context)


def get_api(context):
    domain = 'Global'
    if hasattr(context, 'reservation') and hasattr(context.reservation, 'domain'):
        domain = context.reservation.domain

    try:
        server_address = context.connectivity['server_address']
        api_port = context.connectivity['cloudshell_api_port']
        token = context.connectivity['admin_auth_token']
        api = CloudShellAPISession(server_address, port=api_port, token_id=token, domain=domain)
    except:
        # raise ValueError('Connectivity context is empty')
        api = CloudShellAPISession('localhost', port=8029, username='admin', password='admin', domain=domain)

    return api


def get_cli_connection_attributes(api, context=None):
    if not context:
        CONTEXT_DICT.get(threading.current_thread(), None)
    default_actions = DefaultActions(context=context, api=api)
    return {'host': get_resource_address(context),
            'username': get_attribute_by_name(context=context, attribute_name='User'),
            'password': decrypt_password_from_attribute(api, 'Password', context),
            'default_actions': default_actions.send_actions}


def get_snmp_parameters_from_command_context(command_context):
    """
    :param ResourceCommandContext command_context: command context
    :return:
    """

    snmp_version = get_attribute_by_name(context=command_context, attribute_name='SNMP Version')
    ip = command_context.resource.address

    if '3' in snmp_version:
        return SNMPV3Parameters(
            ip=ip,
            snmp_user=get_attribute_by_name(context=command_context, attribute_name='SNMP User'),
            snmp_password=get_attribute_by_name(context=command_context, attribute_name='SNMP Password'),
            snmp_private_key=get_attribute_by_name(context=command_context, attribute_name='SNMP Private Key')
        )
    else:
        return SNMPV2Parameters(
            ip=ip,
            snmp_community=get_attribute_by_name(context=command_context, attribute_name='SNMP Read Community'))

def get_snmp_handler(context, logger):
    snmp_handler_params = get_snmp_parameters_from_command_context(context)
    return QualiSnmp(snmp_parameters=snmp_handler_params, logger=logger)
