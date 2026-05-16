# Applications (concise)

Contains ArgoCD Application and ApplicationSet manifests that drive the platform:

- `vcluster-tenants.yaml` — ApplicationSet that generates per-tenant bootstrap Applications from `tenants/tenants.yaml`.
- `metrics-app.yaml` — Deploys the metrics demo into a tenant vCluster.
- `metrics-scraper.yaml` — Deploys the host-cluster scraper.
- `tenant-rbac.yaml` — Deploys tenant RBAC and ExternalSecrets.

Workflow: edit `tenants/tenants.yaml`, push to Git; ApplicationSet creates Applications and ArgoCD syncs them.

