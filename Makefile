fmt:
	autoflake plugins/modules/*.py
	autoflake plugins/module_utils/*.py
	autoflake --recursive tests/
	autoflake tools/migrationtool/*.py

	black plugins/modules/*.py
	black plugins/module_utils/*.py
	black tests/
	black tools/migrationtool/*.py

	isort plugins/modules/*.py
	isort plugins/module_utils/*.py
	isort tests/
	isort tools/migrationtool/*.py

	yamlfmt $(shell find . -name '*.yml' -o -name '*.yaml')

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
	python3 -m galaxy_importer.main netscaler-adc-2.17.0.tar.gz

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
		if [[ $$playbook == *"password"* || $$playbook == *"login"* || $$playbook == *"logout"* || $$playbook == *"route"* || $$playbook == *"locationfile.yaml"* || $$playbook == *"nsip6.yaml"* || $$playbook == *"hanode.yaml"* ]]; then \
			continue; \
		fi; \
		echo "Running $$playbook"; \
		ansible-playbook -i examples/inventory.ini $$playbook || \
		ansible-playbook -i examples/inventory.ini $$playbook -vvv > $$playbook.out; \
	done

action:
	act -list
	act --remote-name gh -j ansible-sanity-test

# ---------------------------------------------------------------------------
# Metadata refresh
# ---------------------------------------------------------------------------
# The metadata is produced by an external generator and dropped into the
# collection as a versioned snapshot folder, e.g. 13_4/ .
# Refresh the collection from one snapshot with a single command:
#
#     make refresh_metadata VERSION=13_4
# ---------------------------------------------------------------------------
VERSION ?=

_require_version:
	@if [ -z "$(VERSION)" ]; then \
		echo "ERROR: set VERSION to the snapshot folder, e.g. 'make refresh_metadata VERSION=13_4'"; exit 1; fi
	@if [ ! -d "$(VERSION)" ]; then \
		echo "ERROR: snapshot folder '$(VERSION)/' not found"; exit 1; fi

copy: _require_version
	cp -f $(VERSION)/generated_modules/*.py plugins/modules/.
	cp -f $(VERSION)/nitro_resource_map.py plugins/module_utils/.
	cp -f $(VERSION)/examples/*.yaml examples/.
	cp -f $(VERSION)/supported_modules_matrix.md .

prune_examples:
	python3 tools/prune_examples.py

# CI-friendly: fail (non-zero) if any orphan example exists, deleting nothing.
check_examples:
	python3 tools/prune_examples.py --check

# Reconcile generated docs with the runtime spec where the generator diverges
# (operational-utility modules' state.choices). Safe to run any time.
fix_docs:
	python3 tools/fix_operational_state_docs.py

# Black the copied map only.
fmt_generated:
	python3 -m black plugins/module_utils/nitro_resource_map.py

# Register brand-new modules (present on disk but not yet tracked in git HEAD):
# add each to the default_args action group in meta/runtime.yml and a
# missing-gplv3-license waiver to every tests/sanity/ignore-2.XX.txt, inserted in
# sorted position. Idempotent; detects new modules via git.
register_modules:
	python3 tools/register_new_modules.py

# CI-friendly: fail (non-zero) if any new module is unregistered, writing nothing.
check_modules:
	python3 tools/register_new_modules.py --check

# One-shot refresh: copy -> prune orphans -> fix docs -> black map -> register.
refresh_metadata: copy prune_examples fix_docs fmt_generated register_modules
	@echo "refresh complete: copied $(VERSION)/, pruned orphans, fixed docs, black-formatted map, registered new modules."
	@echo "next (manual): bump galaxy.yml version + CHANGELOG.md; review the git diff."
