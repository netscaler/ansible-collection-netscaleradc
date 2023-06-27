# `netscaler.adc` collection features

## 4 modes of operation (`state` option in the module task)

The `netscaler.adc` collection supports 4 modes of operation.

| Mode (`state` option) | Description |
| ---- | ----------- |
| `present` | Default. Resource will be created if needed and configured according to the module's parameters |
| `absent` | Resource will be deleted from the target NetScaler ADC nodes |
| `enabled` | Resource will be enalbed on the NetScaler ADC nodes |
| `disabled` | Resource will be disabled on the NetScaler ADC nodes |

> NOTE: The `enabled` and `disabled` modes are supported only for the modules that have `enable` and `disable` operations in the NetScaler ADC NITRO API.


## `--diff` support

> `--diff` mode is not supported for `enabled` and `disabled` states.

<kbd>
    <img src="assets/module-option-diff-example.png" />
</kbd>

</hr>

<kbd>
    <img src="assets/module-option-and-binding-diff-example.png" />
</kbd>

## `--check` support

`--check` mode is support for all the modules.


## in-built bindings support

The `netscaler.adc` collection provides in-built bindings support for all the modules.

In the below example (screenshot), the desired state is to create a `lbvserver` with three bindings

- 2 `service` bindings and
- 1 `servicegroup` binding

Every binding is defined as a separate module option. The available bindings are documented in the module documentation.

> TIP: Usually the name of the built-in bindings ends with `_binding` suffix. Eg: `lbvserver_service_binding`, `lbvserver_servicegroup_binding`, etc.

<kbd>
    <img src="assets/module-in-built-bindings-support.png" />
</kbd>

## Explicit bindings support

Apart from the in-built bindings, the `netscaler.adc` collection also supports explicit bindings.

This support will be helpful if the parent resources are already present in the target Netscaler ADC. And the user wants to create a binding between these resources.

<kbd>
    <img src="assets/explicit-binding-module-support.png" />
</kbd>
