Base for the Langato website, which will help users learn vocabulary in the languages they're learning. At present the website can record word lists for different users, and these users can share these word lists with other users.

An alpha version of this website can be seen at: www.testing.langato.com

Future Functionality

    Enable deletion of list entries
    Enable addition of translation of words being learnt

I have used Harry Percival's Test Driven Development book as a preliminary base for this project.

To install on your local machine, make sure you have python 3.6 installed, then run:
	
	git clone https://github.com/gregcodethem/langato.git
	cd langato
	python -m venv env
	source env/bin/activate
	pip install -r requirements.txt

Notes: You may need to change the python -m venv env command, dependent on how you normally create virtual environments.  You may also need to change the source env/bin/activate command if you are on Windows.


To be able to run the functional tests 
	
	download geckodriver from:https://github.com/mozilla/geckodriver/releases
	save it into: env/bin

Then you will be able to run all the tests with the command:
	
	python manage.py test


To set up SASS and gulp in order to make changes to the css:

	install node
	in root folder: npm init -y npm install gulp browser-sync gulp-sass --save-dev npm install bootstrap jquery popper.js --save

Then to make changes through SASS:

	Make changes to: styles.scss file inside of the /src/scss/ folder
	run gulp in lists folder
