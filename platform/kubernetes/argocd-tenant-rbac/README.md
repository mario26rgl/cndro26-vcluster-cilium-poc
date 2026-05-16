# ArgoCD Tenant RBAC (concise)

Creates per-tenant ArgoCD local users, AppProject-scoped RBAC policies, and ExternalSecrets references for repository credentials. Secrets are expected to be managed in AWS Secrets Manager and injected via ESO.

Quick notes:
- Edit `platform/kubernetes/tenants/tenants.yaml` to define tenant repo and auth paths.
- Apply `platform/kubernetes/apps/tenant-rbac.yaml` in ArgoCD to provision RBAC and ExternalSecrets.

Verify with:
```bash
kubectl get configmap -n argocd argocd-cm
kubectl get externalsecrets -n argocd
```
