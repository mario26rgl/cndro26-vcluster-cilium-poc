# vCluster Tenant Bootstrap Chart

Helm chart for deploying isolated Kubernetes virtual clusters (vClusters) and their bootstrap resources on a host cluster. This chart acts as a wrapper around the official [vCluster Helm chart](https://charts.loft.sh) with additional tenant-specific resources.

## Purpose

This chart enables multi-tenant Kubernetes by:
1. Deploying lightweight virtual Kubernetes clusters (vClusters) as tenants
2. Creating ArgoCD AppProject resources for tenant isolation
3. Bridging vCluster kubeconfigs into ArgoCD via External Secrets Operator (ESO)
4. Establishing RBAC policies and local user accounts per tenant
5. Enforcing Pod Security Admission (PSA) policies per tenant

**Used by**: [vcluster-tenants ApplicationSet](../apps/vcluster-tenants.yaml) to provision multi-tenant environments.

---

## Chart Structure

```
vcluster/
├── Chart.yaml                 # Chart metadata
├── values.yaml               # Default values (tenant configuration)
├── vcluster-defaults.yaml    # vCluster upstream sync/policy defaults
└── templates/
    ├── vcluster.yaml         # Multi-source Application (wraps vcluster upstream chart)
    ├── appproject.yaml       # ArgoCD AppProject (per-tenant isolation)
    ├── eso-secret.yaml       # ExternalSecret (kubeconfig injection)
    └── cnp-app.yaml       # Cilium NetworkPolicy (Kustomize-dependent)
```
## vCluster chart (concise)

Deploys tenant vClusters and bootstrap resources (AppProject, ESO bridge, Cilium policies).

Quick usage (via ArgoCD ApplicationSet):

1. Add tenant to `platform/kubernetes/tenants/tenants.yaml` (name, namespace, overrides).
2. Ensure `platform/kubernetes/apps/vcluster-tenants.yaml` ApplicationSet is applied in ArgoCD.
3. ArgoCD will create `{tenant}-bootstrap` Application which deploys this chart.
