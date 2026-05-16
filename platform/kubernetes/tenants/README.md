# Tenants (concise)

`tenants.yaml` is the single source of truth for tenant definitions. Each entry should include `name`, `namespace`, `project`, and optional `vclusterOverrides`.

Add a tenant, commit, and push; the ApplicationSet will generate a bootstrap Application automatically.

Example entry:
```yaml
- name: tenant-two
  namespace: tenant-two
  project: tenant-two
  chartVersion: "0.33.1"
  vclusterOverrides: |
    policies:
      resourceQuota:
        enabled: true
```
