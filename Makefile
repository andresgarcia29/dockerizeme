build:
	docker build -t helloworld .

run:
	docker run --rm  -p 8080:8080 helloworld
