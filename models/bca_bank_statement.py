from odoo import api, fields, models
from odoo import http
import hashlib
import base64
import ast
import requests
import json
import logging

_logger = logging.getLogger(__name__)


class AccountBankStatement(models.Model):
    _inherit = 'account.bank.statement'

    @api.model
    def bca_import_statement(self):
        
        api_key = 'ecc4260d-720c-44e3-871a-9b8bcb9e254b'
        api_secret_key = 'bbe2f4a1-0276-4551-ac6d-df494bed62a9'
        client_key ='de083498-91b0-4d93-b03d-307d163aff78'
        client_secret_key = '9b133ff5-6577-4234-ac5c-4f850e540191'
        # curl https://sandbox.bca.co.id/api/oauth/token \
        # -H "Content-Type: application/x-www-form-urlencoded" \
        # -H "Authorization: Basic       jk5ZTkyYzgtYzAzNC00YmNhLWE0OTAtYWM4NGI0YTZiMjQxOjNmYWIwNGI1LWM4ODctNGZmMi05OGNkLTE1YjJmYTcyNzA1NA==" \
        # -d "grant_type=client_credentials"
        x = base64.encodestring(b'de083498-91b0-4d93-b03d-307d163aff78:9b133ff5-6577-4234-ac5c-4f850e540191')
        _logger.info(x)

        _logger.info('------------Connecting to BCA API------------')
        URL = 'https://sandbox.bca.co.id/api/oauth/token'
   
        # base64('de083498-91b0-4d93-b03d-307d163aff78':'9b133ff5-6577-4234-ac5c-4f850e540191')
        # Signature = HMAC-SHA256(bbe2f4a1-0276-4551-ac6d-df494bed62a9, StringtoSign)

        HEADERS ={'Authorization':'Basic '+string(x),'Content-Type':'application/x-www-form-urlencoded'}
        PARAMS = {'grant_type':'client_credentials'}
        r = requests.post(url = URL, headers = HEADERS, data=PARAMS)

        _logger.info(dir(r))
        _logger.info('-----------------------------')
        _logger.info('-----------------------------')
        _logger.info(r.url)
        _logger.info('-----------------------------')
        _logger.info(r.text)
        _logger.info('-----------------------------')
        _logger.info(r.status_code)
        _logger.info('-----------------------------')
        _logger.info(r.request)
        _logger.info('-----------------------------')
        _logger.info(r.reason)
        _logger.info('-----------------------------')
        _logger.info(r.ok)
        _logger.info('-----------------------------')
        _logger.info(r.json)
        _logger.info('-----------------------------')

        tokendict = ast.literal_eval(r.text)

        # _logger.info('++++++++++++Saving New Record ++++++++++++')
        # bs_dict = {"StartDate":"2016-09-01","EndDate":"2016-09-01","Currency":"IDR","StartBalance" : "94163880.00", \
        #          "Data":[{ \
        #                   "TransactionDate":"PEND", \
        #                   "BranchCode":"0000", \
        #                   "TransactionType":"D", \
        #                   "TransactionAmount":"100000.00", \
        #                   "TransactionName":"TRSF E-BANKING DB", \
        #                   "Trailer":"0109/FTSCY/WS95051 100000.00 Online Transfer PT DUMMY2" \
        #                  }, \
        #                  { \
        #                   "TransactionDate":"PEND", \
        #                   "BranchCode":"0061", \
        #                   "TransactionType":"C", \
        #                   "TransactionAmount":"3000000.00", \
        #                   "TransactionName":"NK - LLG", \
        #                   "Trailer":"" \
        #                  }, \
        #                  { \
        #                   "TransactionDate":"PEND", \
        #                   "BranchCode":"0000", \
        #                   "TransactionType":"D", \
        #                   "TransactionAmount":"250000.00", \
        #                   "TransactionName":"TRSF E-BANKING DB", \
        #                   "Trailer":"0109/FTSCY/WS95051 250800.00 Transfer DUMMY1" \
        #                  }, \
        #                  { \
        #                   "TransactionDate":"PEND", \
        #                   "BranchCode":"0000", \
        #                   "TransactionType":"D", \
        #                   "TransactionAmount":"100000.00", \
        #                   "TransactionName":"BA JASA E-BANKING", \
        #                   "Trailer":"0109/TRCHG/WS95051BIAYA TRANSFER SME" \
        #                  }, \
        #                  { \
        #                   "TransactionDate":"PEND", \
        #                   "BranchCode":"0101", \
        #                   "TransactionType":"C", \
        #                   "TransactionAmount":"10000.00", \
        #                   "TransactionName":"KR OTOMATIS", \
        #                   "Trailer":"DUMMY7  039903811112"}, \
        #                  { \
        #                   "TransactionDate":"PEND", \
        #                   "BranchCode":"0038", \
        #                   "TransactionType":"D", \
        #                   "TransactionAmount":"100000.00", \
        #                   "TransactionName":"TARIKAN TUNAI", \
        #                   "Trailer":"" \
        #                  } \
        #               ] \
        # }

        # data = bs_dict['Data']

        # self.create({'name':'BCA Import',
        #   'state':'open',
        #   'journal_id':1,
        #   'date':bs_dict['StartDate'],
        #   'currency_id':bs_dict['Currency'],
        #   'balance_start':bs_dict['StartBalance']})
        
        # last_stmnt_id = self.env['account.bank.statement'].search([],limit=1,order='id desc')

        # for i in data :
        #   account_bank_statement_line_vals = {
        #       'statement_id' : last_stmnt_id.id,
        #       'name': i['TransactionName'],
        #       # 'date': i['TransactionDate'],
        #       'amount': i['TransactionAmount'],
        #   }

        #   account_bank_statement_line = self.env['account.bank.statement.line'].create(account_bank_statement_line_vals)
        #   # account_bank_statement_line.post()
          
        #   _logger.info('Success')
    def base64_bca(self,clientkey,clientsecretkey):
        auth_bca = base64.b64encode('de083498-91b0-4d93-b03d-307d163aff78:9b133ff5-6577-4234-ac5c-4f850e540191')
        return auth_bca