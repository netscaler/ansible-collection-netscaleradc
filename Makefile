




.PHONY: install docker_image clean clean_docker_image

install:
	python install.py

DOCKERBUILD=utils/dockerbuild

docker_image:
	rsync -avP ansible-modules $(DOCKERBUILD)
	rsync -avP documentation_fragments $(DOCKERBUILD)
	rsync -avP test/integration $(DOCKERBUILD)/test
	rsync -avP test/units $(DOCKERBUILD)/test
	rsync -avP install.py $(DOCKERBUILD)
	rsync -avP deps/nitro-python-1.0.tar.gz $(DOCKERBUILD)
	cd $(DOCKERBUILD) && docker build -t netscaler-ansible . --no-cache

clean: clean_docker_image

clean_docker_image:
	-rm -rf $(DOCKERBUILD)/ansible-modules
	-rm -rf $(DOCKERBUILD)/documentation_fragments
	-rm -rf $(DOCKERBUILD)/test
	-rm $(DOCKERBUILD)/install.py
	-rm $(DOCKERBUILD)/nitro-python-1.0.tar.gz

import_docker_prebuilt_image:
	cat utils/netscaler-ansible-docker-image.tar.gz | docker import - netscaler-ansible
