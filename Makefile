fmt:
	autoflake plugins/modules/*.py
	autoflake plugins/module_utils/*.py
	black plugins/modules/*.py
	black plugins/module_utils/*.py
	isort plugins/modules/*.py
	isort plugins/module_utils/*.py

generate_modules:
	python3 tools/module_generator.py

install_collection:
	ansible-galaxy collection install . --force

# build_docs:
# 	antsibull-docs sphinx-init --use-current --dest-dir _built_docs netscaler.adc
# 	cd _built_docs
# 	pip3 install -r requirements.txt
# 	./build.sh
# 	rsync -cprv --delete-after _built_docs/rst/ docs/