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

fmt_tools:
	# ignore if file not found
	-autoflake tools/generated_modules/*.py
	-autoflake tools/module_generator.py
	-autoflake tools/nitro_resource_map.py

	-black tools/generated_modules/*.py
	-black tools/module_generator.py
	-black tools/nitro_resource_map.py

	-isort tools/generated_modules/*.py
	-isort tools/module_generator.py
	-isort tools/nitro_resource_map.py

generate_modules:
	python3 tools/module_generator.py

install:
	ansible-galaxy collection install . --force

lint: install
	cd ~/.ansible/collections/ansible_collections/netscaler/adc && \
	ansible-test sanity --docker default -v

# build_docs:
# 	antsibull-docs sphinx-init --use-current --dest-dir _built_docs netscaler.adc
# 	cd _built_docs
# 	pip3 install -r requirements.txt
# 	./build.sh
# 	cd ..
# 	rsync -cprv _built_docs/build/html/ docs/ # Do not use --delete-after as this will delete .nojekyll file


# Run examples/*.yaml playbooks individually
# ansible-playbook -i examples/inventory examples/playbook.yaml
# Run the playbook. if the return code is non-zero, save the output to a file
# skip the playbook which contains "password" in the file name
run_examples:
	@for playbook in examples/*.yaml; do \
		if [[ $$playbook == *"password"* ]]; then \
			continue; \
		fi; \
		echo "Running $$playbook"; \
		ansible-playbook -i examples/inventory.ini $$playbook || \
		ansible-playbook -i examples/inventory.ini $$playbook -vvv > $$playbook.out; \
	done
