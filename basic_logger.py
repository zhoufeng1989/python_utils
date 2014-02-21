# -*- coding:utf-8 -*-
# logger common config
import logging
import copy
import logging.config
conf_dict = {
    'version': 1,
    'formatters': {
        'common': {
            'format': '%(asctime)s [%(levelname)s] %(message)s',
            'datefmt': '%Y/%m/%d %H:%M:%S'},
        'smtp': {
            'format': '%(name)s %(asctime)s [%(levelname)s] %(message)s',
            'datefmt': '%Y/%m/%d %H:%M:%S'}},
    'handlers': {
        'smtp': {
            'level': 'ERROR',
            'class': 'logging.handlers.SMTPHandler',
            'formatter': 'smtp',
            'mailhost': ('smtp.example.com', 25),
            'fromaddr': 'service@example.com',
            'toaddrs': ['fengzhou1024@gmail.com'],
            'subject': 'system error message',
            'credentials': ('service@example.com', 'password')},
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'common',
            'filename': 'mylog.log',
            'when': 'd',
            'interval': 1,
            'backupCount': 5,
            'encoding': 'utf8'}},
    'loggers': {
        'root': {
            'level': 'DEBUG',
            'handlers': ['file']},
        'mylogger': {
            'level': 'DEBUG',
            'handlers': ['smtp', 'file'],
            'qualname': 'mylogger',
            'propagate': True}}}


class NameNotFoundError(Exception):
    pass


def get_logger(**kwargs):
    '''
    根据配置项配置log
    kwargs['path']: 日志目录
    kwargs['file_name']: 日志文件名称
    kwargs['mail_list']: list,发送邮件的目标邮箱列表
    '''
    import os
    spe_conf = copy.deepcopy(conf_dict)
    if 'file_name' in kwargs and 'logger_name' in kwargs:
        file_name = kwargs['file_name']
        logger_name = kwargs['logger_name']
    else:
        raise NameNotFoundError
    #log file dir
    path = kwargs.get('path', '')
    if logger_name not in spe_conf['loggers']:
        spe_conf['handlers'][logger_name + '_file'] = spe_conf[
            'handlers']['file']
        spe_conf['handlers'][logger_name + '_file']['filename'] = os.path.join(
            path, file_name + '.log')
        spe_conf['loggers'][logger_name] = spe_conf[
            'loggers'].pop('mylogger')
        spe_conf['loggers'][logger_name]['handlers'] = ['smtp',
                                                        logger_name + '_file']
        spe_conf['loggers'][logger_name]['qualname'] = logger_name
    if kwargs.get('mail_list'):
        spe_conf['handlers']['smtp']['toaddrs'] = kwargs.get('mail_list')

    logging.config.dictConfig(spe_conf)
    return logging.getLogger(logger_name)
if __name__ == '__main__':
    log = get_logger(logger_name='test', file_name='test')
    log.info('test!')
