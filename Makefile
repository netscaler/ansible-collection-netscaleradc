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

# ---------------------------------------------------------------------------
# Metadata refresh
# ---------------------------------------------------------------------------
# The netscaler.adc metadata (modules, nitro_resource_map.py, examples, matrix)
# is produced by an external generator and dropped into the collection as a
# versioned snapshot folder, e.g. 13_4/ (these folders are git-ignored and
# ephemeral). Refresh the collection from one snapshot with a single command:
#
#     make refresh VERSION=13_4
#
# `copy` uses paths relative to the collection root (the snapshot's own Makefile
# ships generator-layout paths that are wrong here), `prune_examples` removes any
# orphan example YAMLs the generator emitted for resources with no module, and
# `fmt_generated` black/isort-formats the copied Python. See metadatarefresh.md
# for the full runbook.
#
# NOTE: `refresh` deliberately uses `fmt_generated`, NOT the full `fmt` target.
# The raw generator `nitro_resource_map.py` ships in pprint style and MUST be
# black-formatted or `ansible-test sanity --test pep8` fails on ~25k E201/E128
# issues. The full `fmt` target runs autoflake/yamlfmt first, which are optional
# dev tools that may be absent -- if they are, `fmt` aborts before black ever
# runs and the map stays pep8-dirty. `fmt_generated` calls black/isort directly.
# ---------------------------------------------------------------------------
VERSION ?=

_require_version:
	@if [ -z "$(VERSION)" ]; then \
		echo "ERROR: set VERSION to the snapshot folder, e.g. 'make refresh VERSION=13_4'"; exit 1; fi
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

# Black the copied map. Uses `python3 -m black` directly so a refresh is not
# blocked by optional dev-only formatters (autoflake/yamlfmt); pep8 sanity only
# needs black. Only the MAP is formatted here: the generator ships the map in
# pprint style (pep8-dirty) but already black-formats the generated modules, so
# blacking the module tree would only drift modules the refresh did not touch
# (a locally-installed black version reformats slightly differently than the
# generator's). If a future snapshot ever ships pep8-dirty modules, black those
# specific files by hand.
fmt_generated:
	python3 -m black plugins/module_utils/nitro_resource_map.py

refresh: copy prune_examples fix_docs fmt_generated
	@echo "refresh complete: copied $(VERSION)/, pruned orphans, fixed docs, black-formatted generated Python."
	@echo "next (manual): register any NEW modules in meta/runtime.yml + tests/sanity/ignore-*.txt, bump galaxy.yml + CHANGELOG.md. See metadatarefresh.md."

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
