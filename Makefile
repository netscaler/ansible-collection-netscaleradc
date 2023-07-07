fmt:
	autoflake plugins/modules/*.py
	autoflake plugins/module_utils/*.py
	autoflake tools/module_generator.py

	black plugins/modules/*.py
	black plugins/module_utils/*.py
	black tools/module_generator.py

	isort plugins/modules/*.py
	isort plugins/module_utils/*.py
	isort tools/module_generator.py

generate_modules:
	python3 tools/module_generator.py

install:
	ansible-galaxy collection install . --force

# build_docs:
# 	antsibull-docs sphinx-init --use-current --dest-dir _built_docs netscaler.adc
# 	cd _built_docs
# 	pip3 install -r requirements.txt
# 	./build.sh
# 	rsync -cprv --delete-after _built_docs/rst/ docs/
