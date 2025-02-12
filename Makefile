fmt:
	autoflake plugins/modules/*.py
	autoflake plugins/module_utils/*.py
	autoflake --recursive tests/

	black plugins/modules/*.py
	black plugins/module_utils/*.py
	black tests/

	isort plugins/modules/*.py
	isort plugins/module_utils/*.py
	isort tests/

	yamlfmt .

install:
	ansible-galaxy collection install . --force

line_length:
	grep -l '.\{159,\}' -R plugins --include='*.py'

lint:
	yamllint .
	echo "\n\n\n\n\n\n\n\n\n\n"
	ansible-lint
	python3 -m pycodestyle --max-line-length 160 --config /dev/null --ignore E203,E402,E741,W503,W504 plugins tests

test_sanity: galaxy_importer install
	cd ~/.ansible/collections/ansible_collections/netscaler/adc && \
	ansible-test sanity --docker default
	# ansible-test sanity --test shellcheck --docker default

test_int: install
	cd ~/.ansible/collections/ansible_collections/netscaler/adc && \
	ansible-test integration
	# ansible-test integration nsip

build:
	ansible-galaxy collection build --force

galaxy_importer: build
	python3 -m galaxy_importer.main netscaler-adc-2.7.1.tar.gz

# build_docs:
# 	rm -rf _built_docs
#   mkdir -p _built_docs
#   make install
# 	antsibull-docs sphinx-init --use-current --dest-dir _built_docs netscaler.adc
# 	cd _built_docs
# 	pip3 install -r requirements.txt
# 	./build.sh
# 	cd ..
# 	rsync -cprv _built_docs/build/html/ docs/ --delete-after # Do not use --delete-after as this will delete .nojekyll file
# 	git restore docs/.nojekyll


# Run examples/*.yaml playbooks individually
# ansible-playbook -i examples/inventory examples/playbook.yaml
# Run the playbook. if the return code is non-zero, save the output to a file
# skip the playbook which contains "password" in the file name
run_examples:
	@for playbook in examples/*.yaml; do \
		if [[ $$playbook == *"password"* || $$playbook == *"login"* || $$playbook == *"logout"* || $$playbook == *"route"* || $$playbook == locationfile.yaml || $$playbook == nsip6.yaml || $$playbook == hanode.yaml ]]; then \
			continue; \
		fi; \
		echo "Running $$playbook"; \
		ansible-playbook -i examples/inventory.ini $$playbook || \
		ansible-playbook -i examples/inventory.ini $$playbook -vvv > $$playbook.out; \
	done

action:
	act -list
	act --remote-name gh -j ansible-sanity-test
