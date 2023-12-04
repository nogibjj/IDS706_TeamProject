install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py --ignore=script.py

build:
	docker build -t ids706-final-project .

deploy:
	aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 057329718388.dkr.ecr.us-east-2.amazonaws.com
	docker tag ids706-final-project:latest 057329718388.dkr.ecr.us-east-2.amazonaws.com/ids706-final-project:latest
	docker push 057329718388.dkr.ecr.us-east-2.amazonaws.com/ids706-final-project:latest
	
all: install lint build deploy