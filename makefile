all:	download	extrair	execute
download:
	wget	-O	aTribuna-21dir.tar.gz	http://eliasdeoliveira.com.br/dataSets/aTribuna-21dir.tar.gz
extrair:
	tar	-xzf	aTribuna-21dir.tar.gz
execute:
	python3	__init__.py	
clean:
	rm	-rf	__pycache__	aTribuna-21dir.tar.gz	aTribuna-21dir