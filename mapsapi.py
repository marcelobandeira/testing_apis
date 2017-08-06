import httplib2
import json

#googlemaps API
def geoLocation(inputStr):
	key = "AIzaSyDIMfJqw8gfEHg-j6FQTZHY1tdMUGxlTJU"
	location = inputStr.replace(" ", "+")
	url = ("https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (location, key))

	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	results = json.loads(content)

	latitude = results['results'][0]['geometry']['location']['lat']
	longitude = results['results'][0]['geometry']['location']['lng']	

	print ('latitude: %f - longitude: %f' % (latitude, longitude))	

# IBM Watson
# def textToSpeech(text, voice):
# 	text = text.replace(" ", "+")
# 	url = ("https://watson-api-explorer.mybluemix.net/text-to-speech/api/v1/synthesize?voice=%s&text=%s" % (voice, text))

# 	h = httplib2.Http()
# 	response, content = h.request(url, 'GET')
# 	results = content

# 	print (results)

###################################################################################
###################################################################################

# API Jarbas - Serenata de Amor
# https://jarbas.serenatadeamor.org/
#lista dos deputados federais, mostra 7 por pagina. 
# ?page=<numero_page> para ver os demais
def listaDeputados(page=1):
	url = ("https://jarbas.serenatadeamor.org/api/applicant?page=%s" %(page))

	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	results = json.loads(content)

	for deputado in results['results']:
		nome = deputado['congressperson_name']
		applicant_id = deputado['applicant_id']

		print ("nome: %s \n applicant_id: %i" % (nome, applicant_id))


# lista dos pedidos de reembolsos de um deputado, mostra 7 por pagina
# ?page=<numero_page> para ver os demais
# aplicant_id eh o id do deputado
def reembolsosDeputado(applicant_id):
	url = ("https://jarbas.serenatadeamor.org/api/reimbursement/?applicant_id=%i" %(applicant_id))

	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	results = json.loads(content)
	for reembolso in results['results']:
		valor = reembolso['document_value']
		ano = reembolso['year']
		mes = reembolso['month']
		nome = reembolso['congressperson_name']
		partido = reembolso['party']
		estado = reembolso['state']
		descricao = reembolso['subquota_description']
		fornecedor = reembolso['supplier']

		print ("deputado: %s \n partido: %s-%s \n ano: %i mes: %i \n descricao: %s \n fornecedor: %s \n valor: %f" 
			%(nome, partido, estado, ano, mes, descricao, fornecedor, valor))

####################################################################################
####################################################################################

# API tabela FIPE
# https://deividfortuna.github.io/fipe/
# lista de marcas de automoveis
def getMarcas():
	url = ("https://fipe-parallelum.rhcloud.com/api/v1/carros/marcas")

	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	results = json.loads(content)

	for marca in results:
		nome = marca['nome']
		codigo = marca['codigo']
		print("\n nome: %s \n codigo: %i" % (nome, codigo))

# lista de modelos de uma marca de automovel
def getModelos(cod_marca):
	url = ("https://fipe-parallelum.rhcloud.com/api/v1/carros/marcas/%i/modelos" % (cod_marca))

	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	results = json.loads(content)

	for modelo in results['modelos']:
		nome = modelo['nome']
		codigo = modelo['codigo']
		print("\n nome: %s \n codigo: %i" % (nome, codigo))

###################################################################################
###################################################################################

#  API Fixer.io para contacao de moedas
# http://fixer.io/
#lista da cotacao de uma moeda em todas as outras moedas
def getTodasCotacoes(moeda):

	url = ("http://api.fixer.io/latest?base=%s" % (moeda))

	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	results = json.loads(content)

	for key in results['rates']:
		print ("1 %s = %f %s" % (moeda, results['rates'][key], key))

# obtem o valor da primeira moeda na segunda moeda
def getCotacao(de, para):

	url = ("http://api.fixer.io/latest?base=%s&symbols=%s" % (de, para))

	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	results = json.loads(content)

	print ("1 %s = %f %s" % (de, results['rates'][para], para))
