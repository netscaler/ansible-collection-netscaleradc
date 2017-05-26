# Developing a new module

There is a lot of boilerplate code that goes into each module since the workflow
is roughly similar for configuring a resource using a singular NITRO object.

To aid with this there are some scripts under utils/ to aid with the generation of
this code.

The parts that are not covered by the boilerplate generation code is peculiarities of each
NITRO object. For example having to use a different nitro object to add/update the resource and
a different object to determine its existance and configuration parameters.

Also when adding bindings to an object there is some manual work to be done to configure
how the bindings tie in with the main object and to maintain the correct control flow of
the module. Still in this cases generating a module file for the binding may be beneficial
since some parts of the generated module can be copied to the more complex one that uses
that object combined with that module's main nitro object.

# Getting the spec of a nitro object

To get the specification of a nitro object there is a script named scarp.py.

This script scraps the nitro reference web site for each object defined in a
hardcoded list and produces for each page scrapped a json file.

This json file contains information about the properties of the nitro object
and is used by subsequent scripts.

The operation of scrap.py is based on parsing the HTML DOM for each page and
may fail for some nitro objects.

To add an object to be scrapped just edit the hardcoded list of objects and
run the script.

# Generating the boilerplate

To generate the boilerplate the script compile.py has to be called.

This script has a hardcoded list of objects and generates for each an initial version
of the corresponding module.

This script has as input for each nitro object the json data file which was obtained
by the scrap.py script and the actual class of the Python NITRO SDK that corresponds
to this object. The Python SDK must be importable when this script is run.

The script checks if there are differences between the attributes defined in the SDK
and the attributes from the scrapped json and will output warnings for each attribute
missing. The attributes that will go into the generated code will be the ones present
in both the SDK object and the json data file.

The json data file must be under utils/source/scrap.

The output python file is put under utils/output

The generated code contains the documentation for the attributes of the nitro object,
the instantiation of a ConfigProxy object for the object and the control flow statements
for the main module execution. Placeholders are marked by a single underscore "\_".

Replacing the placemholders, implementing the object bindings if there are any, and
verifying and correcting the control flow are the most common manual steps that follow.
