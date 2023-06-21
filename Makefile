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